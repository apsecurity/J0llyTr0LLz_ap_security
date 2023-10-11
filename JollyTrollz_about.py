from PyQt5 import QtWidgets, QtCore

import about

class AboutApp(QtWidgets.QWidget, about.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(467, 841)