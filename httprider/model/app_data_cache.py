import logging
from typing import List, Dict

from httprider.core import json_path, response_code_formatter, response_code_round_up
from ..core.constants import DEFAULT_TAG, AssertionDataSource
from ..model.app_data import ApiCall, AppDataWriter, AppDataReader, AppState, ApiTestCase, HttpExchange, Assertion


def _build_filter_query(query=None, tag=None):
    selected_tag = tag if tag != DEFAULT_TAG else None
    if selected_tag and query:
        return lambda api_call: query.lower() in api_call.title.lower() \
                                and selected_tag in api_call.tags

    if selected_tag:
        return lambda api_call: selected_tag in api_call.tags

    if query:
        return lambda api_call: query.lower() in api_call.title.lower()

    return lambda api_call: api_call


class AppDataCache:
    api_call_list: List[ApiCall] = []
    api_test_cases: Dict[int, ApiTestCase] = {}
    api_http_exchanges: Dict[int, HttpExchange] = {}
    app_state: AppState = None
    search_query = None

    def __init__(self, data_reader: AppDataReader, data_writer: AppDataWriter):
        self.app_data_reader = data_reader
        self.app_data_writer = data_writer

        # API Calls
        self.app_data_writer.signals.api_call_added.connect(self.on_api_call_added)
        self.app_data_writer.signals.api_call_removed.connect(self.on_api_call_removed)
        self.app_data_writer.signals.multiple_api_calls_added.connect(self.on_multiple_api_calls_added)
        self.app_data_writer.signals.api_call_tag_added.connect(lambda c: self.refresh_cache_item(c.id))
        self.app_data_writer.signals.api_call_tag_removed.connect(lambda c: self.refresh_cache_item(c.id))
        self.app_data_writer.signals.api_call_updated.connect(self.refresh_cache_item)

        # AppState
        self.app_data_writer.signals.app_state_updated.connect(self.refresh_app_state)

        # API Test Cases
        self.app_data_writer.signals.api_test_case_changed.connect(self.refresh_api_test_case)

        # API Exchange
        self.app_data_writer.signals.exchange_added.connect(self.on_api_http_exchange_added)
        self.app_data_writer.signals.exchange_changed.connect(self.on_api_http_exchange_updated)

    def load_cache(self):
        self.api_call_list = self.app_data_reader.get_all_api_calls()
        for api_call in self.api_call_list:
            api_test_case = self.app_data_reader.get_api_test_case(api_call.id)
            self.api_test_cases[api_call.id] = api_test_case
            http_exchanges = self.app_data_reader.get_api_call_exchanges(api_call.id)
            self.api_http_exchanges[api_call.id] = http_exchanges

        self.app_state = self.app_data_reader.get_app_state()

    def on_api_http_exchange_added(self, api_call_id, exchange):
        http_exchanges = self.api_http_exchanges.get(api_call_id, [])
        http_exchanges.append(exchange)
        self.api_http_exchanges[api_call_id] = http_exchanges

    def on_api_http_exchange_updated(self, exchange_id, exchange):
        api_call_id = exchange.api_call_id
        http_exchanges = self.app_data_reader.get_api_call_exchanges(api_call_id)
        self.api_http_exchanges[api_call_id] = http_exchanges

    def get_all_api_calls(self):
        return self.api_call_list

    def refresh_api_test_case(self, api_call_id):
        api_test_case = self.app_data_reader.get_api_test_case(api_call_id)
        self.api_test_cases[api_call_id] = api_test_case

    def refresh_app_state(self):
        self.app_state = self.app_data_reader.get_app_state()

    def refresh_cache_item(self, api_call_id):
        refreshed_api_call = self.app_data_reader.get_api_call(api_call_id)
        for ac in self.api_call_list:
            if ac.id == api_call_id:
                self.api_call_list.remove(ac)
        self.api_call_list.append(refreshed_api_call)

    def on_api_call_added(self, doc_id, api_call: ApiCall):
        api_call.id = doc_id
        self.api_call_list.append(api_call)

    def on_api_call_removed(self, doc_ids):
        for api_call in self.api_call_list:
            if api_call.id in doc_ids:
                self.api_call_list.remove(api_call)

    def on_multiple_api_calls_added(self, doc_ids: List[str], api_calls: List[ApiCall]):
        assert len(doc_ids) == len(api_calls)
        for doc_id, api_call in zip(doc_ids, api_calls):
            api_call.id = doc_id
            self.api_call_list.append(api_call)

    def filter_api_calls(self, search_query=None, search_tag=None):
        logging.info(f"Filtering API Calls by Query {search_query} and Tag {search_tag}")
        api_calls_filter = _build_filter_query(query=search_query, tag=search_tag)
        return sorted(
            filter(api_calls_filter, self.api_call_list),
            key=lambda a: a.sequence_number
        )

    def update_search_query(self, search_query):
        self.search_query = search_query

    def get_app_state(self):
        self.app_state.selected_search = self.search_query
        return self.app_state

    @staticmethod
    def get_latest_assertion_value_from_exchange(assertion: Assertion, exchange: HttpExchange):
        if assertion.data_from == AssertionDataSource.REQUEST_HEADER.value:
            return exchange.request.headers.get(assertion.selector, None)
        elif assertion.data_from == AssertionDataSource.RESPONSE_HEADER.value:
            return exchange.response.headers.get(assertion.selector, None)
        elif assertion.data_from == AssertionDataSource.REQUEST_BODY.value:
            return json_path(exchange.request.request_body, assertion.selector)
        elif assertion.data_from == AssertionDataSource.RESPONSE_BODY.value:
            return json_path(exchange.response.response_body, assertion.selector)
        elif assertion.data_from == AssertionDataSource.RESPONSE_CODE.value:
            return response_code_formatter(exchange.response.http_status_code)
        elif assertion.data_from == AssertionDataSource.RESPONSE_TIME.value:
            return response_code_round_up(exchange.response.elapsed_time)

    def __build_assertion(self, api_call: ApiCall, exchange: HttpExchange, api_test_case: ApiTestCase):
        return {
            assertion.var_name: self.get_latest_assertion_value_from_exchange(assertion, exchange)
            for assertion in api_test_case.assertions
        }

    def get_api_call_exchanges(self, doc_id):
        return self.api_http_exchanges.get(doc_id, [])

    def get_last_exchange(self, api_call_id):
        api_call_exchanges = self.get_api_call_exchanges(api_call_id)
        if api_call_exchanges:
            return api_call_exchanges[-1]
        else:
            return HttpExchange(api_call_id)

    def get_api_test_case(self, api_call_id):
        logging.info(f"CACHE API: {api_call_id} - Getting API Test case")
        return self.api_test_cases.get(api_call_id)

    def get_all_api_test_assertions(self):
        api_calls = self.get_all_api_calls()
        return [
            self.__build_assertion(
                api_call,
                self.get_last_exchange(api_call.id),
                self.get_api_test_case(api_call.id)
            )
            for api_call in api_calls
        ]
