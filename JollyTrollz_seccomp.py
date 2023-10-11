from PyQt5 import QtWidgets, QtCore

import seccomp
import os

class SeccompApp(QtWidgets.QWidget, seccomp.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.seccomp_function()
    
    def seccomp_function(self):
        all = []
        with open("seccomp_tmp.txt", 'r') as tmp:
            tmp_read = tmp.read()
        os.system("rm seccomp_tmp.txt")
        # self.listWidget.addItem("line ")
        for i in range(len(tmp_read.split("\n"))):
            if(tmp_read.split("\n")[i] == "================================="):
                self.listWidget.addItem(" line  CODE  JT   JF      K")
                for j in range(i+1, len(tmp_read.split("\n"))):
                    self.listWidget.addItem(tmp_read.split("\n")[j])
                break