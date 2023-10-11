from PyQt5 import QtWidgets, QtCore

import os
import strings

class StringsApp(QtWidgets.QWidget, strings.Ui_Form):
    result = ""
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.strings()
        self.actionGrepStrings.triggered.connect(self.grepStr)

    def strings(self):
        with open("tmp_strings.txt", 'r') as tmp:
            str_tmp = tmp.read()
        os.system("rm tmp_strings.txt")
        self.result = ""
        self.result = str_tmp.split("\n")
        self.showStrings()
    
    def showStrings(self):
        for i in range(len(self.result)):
            self.listWidget.addItem(self.result[i])
    
    def grepStr(self):
        if(len(self.lineEdit.text()) == 0):
            self.listWidget.clear()
            self.showStrings()
        else:
            textReg = self.lineEdit.text()
            reg = QtCore.QRegExp(textReg)
            tmp_strings = []
            for i in range(self.listWidget.count()):
                pos = reg.indexIn(self.listWidget.item(i).text(),0)
                while pos != -1:
                    # find_string = self.listWidget.item(i).text()[pos : pos + reg.matchedLength()]
                    tmp_strings.append(self.listWidget.item(i).text())
                    pos += reg.matchedLength()
                    pos = reg.indexIn(self.listWidget.item(i).text(), pos)
            self.listWidget.clear()
            for i in range(len(tmp_strings)):
                self.listWidget.addItem(tmp_strings[i])