import logging

from PyQt5.QtWidgets import QListWidget

from ..core import str_to_bool
from ..core.constants import AssertionMatchers
from ..core.core_settings import app_settings
from ..model.app_data import Assertion, ApiTestCase, HttpExchange, ApiCall


class AssertionResultPresenter:
    view: QListWidget

    def __init__(self, parent=None):
        self.view = parent.list_assertion_results
        self.parent_view = parent
        app_settings.app_data_writer.signals.exchange_changed.connect(self.update_assertion_results)
        app_settings.app_data_reader.signals.api_call_change_selection.connect(self.new_api_call_selected)

    def evaluate(self, api_test_case: ApiTestCase, exchange: HttpExchange):
        logging.info(f"Running {len(api_test_case.assertions)} assertions against exchange {exchange}")
        assertions_with_output = [
            self.__evaluate_assertion(assertion, exchange)
            for assertion in api_test_case.assertions
        ]
        exchange.assertions = assertions_with_output
        app_settings.app_data_writer.update_http_exchange(exchange)

        # Update API Call assertions status
        api_call = app_settings.app_data_reader.get_api_call(api_test_case.api_call_id)
        api_call.last_assertion_result = 1 if all([o.result for o in assertions_with_output]) else 0
        app_settings.app_data_writer.update_api_call(api_call.id, api_call)

    def __get_last_exchange(self, api_call_id):
        api_call_exchanges = app_settings.app_data_reader.get_api_call_exchanges(api_call_id)
        if api_call_exchanges:
            return api_call_exchanges[-1]
        else:
            return HttpExchange(api_call_id)

    def new_api_call_selected(self, api_call: ApiCall):
        last_exchange = self.__get_last_exchange(api_call.id)
        self.update_assertion_results(None, last_exchange)

    def update_assertion_results(self, _, exchange: HttpExchange):
        self.view.clear()
        for assertion in exchange.assertions:
            if assertion.output and assertion.output != "None":
                self.view.addItem(f"{assertion.output}")

    def __evaluate_assertion(self, assertion: Assertion, exchange: HttpExchange):
        current_val = app_settings.app_data_reader.get_latest_assertion_value_from_exchange(assertion, exchange)
        if assertion.expected_value == "None" or assertion.matcher == AssertionMatchers.SKIP.value:
            assertion.output = None
        else:
            res = self.__get_result_for_matcher(
                assertion.matcher,
                current_val,
                assertion.expected_value,
                assertion.var_type
            )
            indicator = "✅" if res else "⛔"
            assertion.result = res
            assertion.output = f"{indicator} [{assertion.data_from}] {assertion.selector} - Actual:({current_val}) {assertion.matcher} Expected:({assertion.expected_value})"
        return assertion

    def __get_result_for_matcher(self, matcher, current_val, expected_val, val_type):
        logging.info(f"get_result_for_matcher({matcher}, {current_val}, {expected_val}, {val_type})")
        if matcher == AssertionMatchers.NOT_NULL.value:
            return current_val is not None

        if val_type == "int":
            current_val = int(current_val)
            expected_val = int(expected_val)
        elif val_type == "float":
            current_val = float(current_val)
            expected_val = float(expected_val)
        elif val_type == "bool":
            current_val = str_to_bool(current_val)
            expected_val = str_to_bool(expected_val)

        if matcher == AssertionMatchers.EQ.value:
            return current_val == expected_val

        if matcher == AssertionMatchers.CONTAINS.value:
            return current_val.find(expected_val) >= 0

        if val_type in ["int", "float"]:
            if matcher == AssertionMatchers.LT.value:
                return current_val < expected_val
            if matcher == AssertionMatchers.GT.value:
                return current_val > expected_val

        return False
