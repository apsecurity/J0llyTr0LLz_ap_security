# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jollydbg.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1424, 807)
        Form.setStyleSheet("font: 11pt \"ModeSeven\";\n"
"background-color: rgb(106, 9, 158);")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setStyleSheet("background-color: rgb(196, 112, 255);\n"
"border-color: rgb(65, 5, 98);\n"
"selection-color: rgb(65, 5, 98);")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_15 = QtWidgets.QWidget()
        self.tab_15.setObjectName("tab_15")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_15)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.listWidget = QtWidgets.QListWidget(self.tab_15)
        self.listWidget.setStyleSheet("background-color: rgb(196, 112, 255);\n"
"font: 75 11pt \"FreeMono\";\n"
"border-color: rgb(65, 5, 98);\n"
"selection-color: rgb(65, 5, 98);")
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_2.addWidget(self.listWidget, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_15, "")
        self.tab_17 = QtWidgets.QWidget()
        self.tab_17.setObjectName("tab_17")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_17)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.textEdit = QtWidgets.QTextEdit(self.tab_17)
        self.textEdit.setStyleSheet("background-color: rgb(196, 112, 255);\n"
"font: 75 11pt \"FreeMono\";\n"
"border-color: rgb(65, 5, 98);\n"
"selection-color: rgb(65, 5, 98);")
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_4.addWidget(self.textEdit, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_17, "")
        self.tab_16 = QtWidgets.QWidget()
        self.tab_16.setObjectName("tab_16")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_16)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.listWidget_2 = QtWidgets.QListWidget(self.tab_16)
        self.listWidget_2.setStyleSheet("background-color: rgb(196, 112, 255);\n"
"font: 75 11pt \"FreeMono\";\n"
"border-color: rgb(65, 5, 98);\n"
"selection-color: rgb(65, 5, 98);")
        self.listWidget_2.setObjectName("listWidget_2")
        self.gridLayout_3.addWidget(self.listWidget_2, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.tab_16)
        self.lineEdit.setStyleSheet("background-color: rgb(196, 112, 255);\n"
"border-color: rgb(65, 5, 98);\n"
"selection-color: rgb(65, 5, 98);")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_3.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_16, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.listWidget_3 = QtWidgets.QListWidget(self.tab)
        self.listWidget_3.setStyleSheet("background-color: rgb(196, 112, 255);\n"
"font: 75 11pt \"FreeMono\";\n"
"border-color: rgb(65, 5, 98);\n"
"selection-color: rgb(65, 5, 98);")
        self.listWidget_3.setObjectName("listWidget_3")
        self.gridLayout_5.addWidget(self.listWidget_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.actionAdress = QtWidgets.QAction(Form)
        self.actionAdress.setObjectName("actionAdress")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "J0llyDBG"))
        self.pushButton.setText(_translate("Form", "J0llyDBG"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_15), _translate("Form", "all"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_17), _translate("Form", "graph"))
        self.lineEdit.setPlaceholderText(_translate("Form", "address..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_16), _translate("Form", "function"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "strings"))
        self.actionAdress.setText(_translate("Form", "adress"))
        self.actionAdress.setShortcut(_translate("Form", "Return"))
