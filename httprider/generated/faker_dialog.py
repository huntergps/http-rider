# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/ui/faker_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DataGeneratorDialog(object):
    def setupUi(self, DataGeneratorDialog):
        DataGeneratorDialog.setObjectName("DataGeneratorDialog")
        DataGeneratorDialog.resize(422, 345)
        self.buttonBox = QtWidgets.QDialogButtonBox(DataGeneratorDialog)
        self.buttonBox.setGeometry(QtCore.QRect(70, 310, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.tabWidget = QtWidgets.QTabWidget(DataGeneratorDialog)
        self.tabWidget.setGeometry(QtCore.QRect(20, 10, 391, 291))
        self.tabWidget.setObjectName("tabWidget")
        self.misc = QtWidgets.QWidget()
        self.misc.setObjectName("misc")
        self.cmb_random_string = QtWidgets.QRadioButton(self.misc)
        self.cmb_random_string.setGeometry(QtCore.QRect(10, 10, 131, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cmb_random_string.setFont(font)
        self.cmb_random_string.setChecked(True)
        self.cmb_random_string.setObjectName("cmb_random_string")
        self.txt_random_string_chars = QtWidgets.QSpinBox(self.misc)
        self.txt_random_string_chars.setGeometry(QtCore.QRect(40, 40, 51, 21))
        self.txt_random_string_chars.setProperty("value", 32)
        self.txt_random_string_chars.setObjectName("txt_random_string_chars")
        self.label = QtWidgets.QLabel(self.misc)
        self.label.setGeometry(QtCore.QRect(100, 40, 60, 21))
        self.label.setObjectName("label")
        self.chk_random_string_letters = QtWidgets.QCheckBox(self.misc)
        self.chk_random_string_letters.setGeometry(QtCore.QRect(160, 40, 87, 20))
        self.chk_random_string_letters.setChecked(True)
        self.chk_random_string_letters.setObjectName("chk_random_string_letters")
        self.chk_random_string_digits = QtWidgets.QCheckBox(self.misc)
        self.chk_random_string_digits.setGeometry(QtCore.QRect(250, 40, 87, 20))
        self.chk_random_string_digits.setObjectName("chk_random_string_digits")
        self.cmb_uuid = QtWidgets.QRadioButton(self.misc)
        self.cmb_uuid.setGeometry(QtCore.QRect(10, 100, 100, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cmb_uuid.setFont(font)
        self.cmb_uuid.setObjectName("cmb_uuid")
        self.lbl_eg_random_string = QtWidgets.QLabel(self.misc)
        self.lbl_eg_random_string.setGeometry(QtCore.QRect(40, 70, 331, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(True)
        self.lbl_eg_random_string.setFont(font)
        self.lbl_eg_random_string.setObjectName("lbl_eg_random_string")
        self.lbl_eg_uuid = QtWidgets.QLabel(self.misc)
        self.lbl_eg_uuid.setGeometry(QtCore.QRect(100, 100, 271, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(True)
        self.lbl_eg_uuid.setFont(font)
        self.lbl_eg_uuid.setObjectName("lbl_eg_uuid")
        self.cmb_custom_string = QtWidgets.QRadioButton(self.misc)
        self.cmb_custom_string.setGeometry(QtCore.QRect(10, 140, 100, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cmb_custom_string.setFont(font)
        self.cmb_custom_string.setObjectName("cmb_custom_string")
        self.txt_custom_string_template = QtWidgets.QLineEdit(self.misc)
        self.txt_custom_string_template.setGeometry(QtCore.QRect(40, 170, 321, 21))
        self.txt_custom_string_template.setObjectName("txt_custom_string_template")
        self.lbl_eg_uuid_2 = QtWidgets.QLabel(self.misc)
        self.lbl_eg_uuid_2.setGeometry(QtCore.QRect(90, 143, 181, 16))
        font = QtGui.QFont()
        font.setItalic(True)
        self.lbl_eg_uuid_2.setFont(font)
        self.lbl_eg_uuid_2.setObjectName("lbl_eg_uuid_2")
        self.lbl_eg_custom_string = QtWidgets.QLabel(self.misc)
        self.lbl_eg_custom_string.setGeometry(QtCore.QRect(40, 200, 331, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(True)
        self.lbl_eg_custom_string.setFont(font)
        self.lbl_eg_custom_string.setObjectName("lbl_eg_custom_string")
        self.chk_custom_string_uppercase = QtWidgets.QCheckBox(self.misc)
        self.chk_custom_string_uppercase.setGeometry(QtCore.QRect(280, 140, 87, 20))
        self.chk_custom_string_uppercase.setChecked(True)
        self.chk_custom_string_uppercase.setObjectName("chk_custom_string_uppercase")
        self.tabWidget.addTab(self.misc, "")
        self.person = QtWidgets.QWidget()
        self.person.setObjectName("person")
        self.cmb_person_first_name = QtWidgets.QRadioButton(self.person)
        self.cmb_person_first_name.setGeometry(QtCore.QRect(10, 70, 131, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cmb_person_first_name.setFont(font)
        self.cmb_person_first_name.setAutoExclusive(True)
        self.cmb_person_first_name.setObjectName("cmb_person_first_name")
        self.cmb_person_last_name = QtWidgets.QRadioButton(self.person)
        self.cmb_person_last_name.setGeometry(QtCore.QRect(10, 100, 100, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cmb_person_last_name.setFont(font)
        self.cmb_person_last_name.setObjectName("cmb_person_last_name")
        self.gender_selector = QtWidgets.QComboBox(self.person)
        self.gender_selector.setGeometry(QtCore.QRect(10, 10, 104, 26))
        self.gender_selector.setObjectName("gender_selector")
        self.gender_selector.addItem("")
        self.gender_selector.addItem("")
        self.cmb_person_suffix = QtWidgets.QRadioButton(self.person)
        self.cmb_person_suffix.setGeometry(QtCore.QRect(10, 160, 100, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cmb_person_suffix.setFont(font)
        self.cmb_person_suffix.setObjectName("cmb_person_suffix")
        self.cmb_person_full_name = QtWidgets.QRadioButton(self.person)
        self.cmb_person_full_name.setGeometry(QtCore.QRect(10, 130, 100, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cmb_person_full_name.setFont(font)
        self.cmb_person_full_name.setObjectName("cmb_person_full_name")
        self.lbl_eg_person_first_name = QtWidgets.QLabel(self.person)
        self.lbl_eg_person_first_name.setGeometry(QtCore.QRect(170, 70, 201, 16))
        font = QtGui.QFont()
        font.setItalic(True)
        self.lbl_eg_person_first_name.setFont(font)
        self.lbl_eg_person_first_name.setObjectName("lbl_eg_person_first_name")
        self.lbl_eg_person_last_name = QtWidgets.QLabel(self.person)
        self.lbl_eg_person_last_name.setGeometry(QtCore.QRect(170, 100, 201, 16))
        font = QtGui.QFont()
        font.setItalic(True)
        self.lbl_eg_person_last_name.setFont(font)
        self.lbl_eg_person_last_name.setObjectName("lbl_eg_person_last_name")
        self.lbl_eg_person_suffix = QtWidgets.QLabel(self.person)
        self.lbl_eg_person_suffix.setGeometry(QtCore.QRect(170, 160, 201, 16))
        font = QtGui.QFont()
        font.setItalic(True)
        self.lbl_eg_person_suffix.setFont(font)
        self.lbl_eg_person_suffix.setObjectName("lbl_eg_person_suffix")
        self.lbl_eg_person_full_name = QtWidgets.QLabel(self.person)
        self.lbl_eg_person_full_name.setGeometry(QtCore.QRect(170, 130, 201, 16))
        font = QtGui.QFont()
        font.setItalic(True)
        self.lbl_eg_person_full_name.setFont(font)
        self.lbl_eg_person_full_name.setObjectName("lbl_eg_person_full_name")
        self.lbl_eg_person_prefix = QtWidgets.QLabel(self.person)
        self.lbl_eg_person_prefix.setGeometry(QtCore.QRect(170, 40, 201, 16))
        font = QtGui.QFont()
        font.setItalic(True)
        self.lbl_eg_person_prefix.setFont(font)
        self.lbl_eg_person_prefix.setObjectName("lbl_eg_person_prefix")
        self.cmb_person_prefix = QtWidgets.QRadioButton(self.person)
        self.cmb_person_prefix.setGeometry(QtCore.QRect(10, 40, 100, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cmb_person_prefix.setFont(font)
        self.cmb_person_prefix.setChecked(True)
        self.cmb_person_prefix.setObjectName("cmb_person_prefix")
        self.tabWidget.addTab(self.person, "")
        self.address = QtWidgets.QWidget()
        self.address.setObjectName("address")
        self.lbl_eg_address_full = QtWidgets.QLabel(self.address)
        self.lbl_eg_address_full.setGeometry(QtCore.QRect(170, 40, 211, 16))
        font = QtGui.QFont()
        font.setItalic(True)
        self.lbl_eg_address_full.setFont(font)
        self.lbl_eg_address_full.setObjectName("lbl_eg_address_full")
        self.cmb_address_full = QtWidgets.QRadioButton(self.address)
        self.cmb_address_full.setGeometry(QtCore.QRect(10, 40, 131, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cmb_address_full.setFont(font)
        self.cmb_address_full.setAutoExclusive(True)
        self.cmb_address_full.setObjectName("cmb_address_full")
        self.cmb_address_secondary = QtWidgets.QRadioButton(self.address)
        self.cmb_address_secondary.setGeometry(QtCore.QRect(10, 70, 151, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cmb_address_secondary.setFont(font)
        self.cmb_address_secondary.setAutoExclusive(True)
        self.cmb_address_secondary.setObjectName("cmb_address_secondary")
        self.lbl_eg_address_secondary = QtWidgets.QLabel(self.address)
        self.lbl_eg_address_secondary.setGeometry(QtCore.QRect(170, 70, 201, 16))
        font = QtGui.QFont()
        font.setItalic(True)
        self.lbl_eg_address_secondary.setFont(font)
        self.lbl_eg_address_secondary.setObjectName("lbl_eg_address_secondary")
        self.cmb_address_street = QtWidgets.QRadioButton(self.address)
        self.cmb_address_street.setGeometry(QtCore.QRect(10, 100, 131, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cmb_address_street.setFont(font)
        self.cmb_address_street.setAutoExclusive(True)
        self.cmb_address_street.setObjectName("cmb_address_street")
        self.lbl_eg_address_street = QtWidgets.QLabel(self.address)
        self.lbl_eg_address_street.setGeometry(QtCore.QRect(170, 100, 201, 16))
        font = QtGui.QFont()
        font.setItalic(True)
        self.lbl_eg_address_street.setFont(font)
        self.lbl_eg_address_street.setObjectName("lbl_eg_address_street")
        self.lbl_eg_address_city = QtWidgets.QLabel(self.address)
        self.lbl_eg_address_city.setGeometry(QtCore.QRect(170, 130, 201, 16))
        font = QtGui.QFont()
        font.setItalic(True)
        self.lbl_eg_address_city.setFont(font)
        self.lbl_eg_address_city.setObjectName("lbl_eg_address_city")
        self.cmb_address_city = QtWidgets.QRadioButton(self.address)
        self.cmb_address_city.setGeometry(QtCore.QRect(10, 130, 131, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cmb_address_city.setFont(font)
        self.cmb_address_city.setAutoExclusive(True)
        self.cmb_address_city.setObjectName("cmb_address_city")
        self.cmb_address_zipcode = QtWidgets.QRadioButton(self.address)
        self.cmb_address_zipcode.setGeometry(QtCore.QRect(10, 160, 131, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cmb_address_zipcode.setFont(font)
        self.cmb_address_zipcode.setAutoExclusive(True)
        self.cmb_address_zipcode.setObjectName("cmb_address_zipcode")
        self.lbl_eg_address_zipcode = QtWidgets.QLabel(self.address)
        self.lbl_eg_address_zipcode.setGeometry(QtCore.QRect(170, 160, 201, 16))
        font = QtGui.QFont()
        font.setItalic(True)
        self.lbl_eg_address_zipcode.setFont(font)
        self.lbl_eg_address_zipcode.setObjectName("lbl_eg_address_zipcode")
        self.lbl_eg_address_state = QtWidgets.QLabel(self.address)
        self.lbl_eg_address_state.setGeometry(QtCore.QRect(170, 190, 201, 16))
        font = QtGui.QFont()
        font.setItalic(True)
        self.lbl_eg_address_state.setFont(font)
        self.lbl_eg_address_state.setObjectName("lbl_eg_address_state")
        self.cmb_address_state = QtWidgets.QRadioButton(self.address)
        self.cmb_address_state.setGeometry(QtCore.QRect(10, 190, 131, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cmb_address_state.setFont(font)
        self.cmb_address_state.setAutoExclusive(True)
        self.cmb_address_state.setObjectName("cmb_address_state")
        self.cmb_address_country = QtWidgets.QRadioButton(self.address)
        self.cmb_address_country.setGeometry(QtCore.QRect(10, 10, 131, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cmb_address_country.setFont(font)
        self.cmb_address_country.setChecked(True)
        self.cmb_address_country.setAutoExclusive(True)
        self.cmb_address_country.setObjectName("cmb_address_country")
        self.lbl_eg_address_country = QtWidgets.QLabel(self.address)
        self.lbl_eg_address_country.setGeometry(QtCore.QRect(170, 10, 201, 16))
        font = QtGui.QFont()
        font.setItalic(True)
        self.lbl_eg_address_country.setFont(font)
        self.lbl_eg_address_country.setObjectName("lbl_eg_address_country")
        self.tabWidget.addTab(self.address, "")

        self.retranslateUi(DataGeneratorDialog)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(DataGeneratorDialog.accept)
        self.buttonBox.rejected.connect(DataGeneratorDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(DataGeneratorDialog)

    def retranslateUi(self, DataGeneratorDialog):
        _translate = QtCore.QCoreApplication.translate
        DataGeneratorDialog.setWindowTitle(_translate("DataGeneratorDialog", "Dialog"))
        self.cmb_random_string.setText(_translate("DataGeneratorDialog", "Random string"))
        self.label.setText(_translate("DataGeneratorDialog", "Chars"))
        self.chk_random_string_letters.setText(_translate("DataGeneratorDialog", "Letters"))
        self.chk_random_string_digits.setText(_translate("DataGeneratorDialog", "Digits"))
        self.cmb_uuid.setText(_translate("DataGeneratorDialog", "UUID"))
        self.lbl_eg_random_string.setText(_translate("DataGeneratorDialog", "eg."))
        self.lbl_eg_uuid.setText(_translate("DataGeneratorDialog", "eg."))
        self.cmb_custom_string.setText(_translate("DataGeneratorDialog", "Custom"))
        self.txt_custom_string_template.setText(_translate("DataGeneratorDialog", "**#-#**"))
        self.lbl_eg_uuid_2.setText(_translate("DataGeneratorDialog", "(# for numeric, * for alphabet)"))
        self.lbl_eg_custom_string.setText(_translate("DataGeneratorDialog", "eg."))
        self.chk_custom_string_uppercase.setText(_translate("DataGeneratorDialog", "Uppercase"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.misc), _translate("DataGeneratorDialog", "Misc"))
        self.cmb_person_first_name.setText(_translate("DataGeneratorDialog", "First name"))
        self.cmb_person_last_name.setText(_translate("DataGeneratorDialog", "Last name"))
        self.gender_selector.setItemText(0, _translate("DataGeneratorDialog", "Male"))
        self.gender_selector.setItemText(1, _translate("DataGeneratorDialog", "Female"))
        self.cmb_person_suffix.setText(_translate("DataGeneratorDialog", "Suffix"))
        self.cmb_person_full_name.setText(_translate("DataGeneratorDialog", "Full name"))
        self.lbl_eg_person_first_name.setText(_translate("DataGeneratorDialog", "eg."))
        self.lbl_eg_person_last_name.setText(_translate("DataGeneratorDialog", "eg."))
        self.lbl_eg_person_suffix.setText(_translate("DataGeneratorDialog", "eg."))
        self.lbl_eg_person_full_name.setText(_translate("DataGeneratorDialog", "eg."))
        self.lbl_eg_person_prefix.setText(_translate("DataGeneratorDialog", "eg."))
        self.cmb_person_prefix.setText(_translate("DataGeneratorDialog", "Prefix"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.person), _translate("DataGeneratorDialog", "Person"))
        self.lbl_eg_address_full.setText(_translate("DataGeneratorDialog", "eg."))
        self.cmb_address_full.setText(_translate("DataGeneratorDialog", "Full Address"))
        self.cmb_address_secondary.setText(_translate("DataGeneratorDialog", "Secondary Address"))
        self.lbl_eg_address_secondary.setText(_translate("DataGeneratorDialog", "eg."))
        self.cmb_address_street.setText(_translate("DataGeneratorDialog", "Street Address"))
        self.lbl_eg_address_street.setText(_translate("DataGeneratorDialog", "eg."))
        self.lbl_eg_address_city.setText(_translate("DataGeneratorDialog", "eg."))
        self.cmb_address_city.setText(_translate("DataGeneratorDialog", "City"))
        self.cmb_address_zipcode.setText(_translate("DataGeneratorDialog", "Zip code"))
        self.lbl_eg_address_zipcode.setText(_translate("DataGeneratorDialog", "eg."))
        self.lbl_eg_address_state.setText(_translate("DataGeneratorDialog", "eg."))
        self.cmb_address_state.setText(_translate("DataGeneratorDialog", "State"))
        self.cmb_address_country.setText(_translate("DataGeneratorDialog", "Country"))
        self.lbl_eg_address_country.setText(_translate("DataGeneratorDialog", "eg."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.address), _translate("DataGeneratorDialog", "Address"))


