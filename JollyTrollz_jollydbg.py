from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QListWidget, QListWidgetItem

import os
import jollydbg
import r2pipe

class JollyDBGApp(QtWidgets.QWidget, jollydbg.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.filename = ''
        self.result = ''
        self.openFile()
        self.listWidget_2.doubleClicked.connect(self.getItem)

    def openFile(self):
        with open('save_filename.txt', 'r') as tmp:
            self.filename = tmp.read()

        with open("jdbg_obj_dump.txt") as tmp:
            self.result = tmp.read()
        os.system("rm jdbg_obj_dump.txt")

        with open('main_graph.txt') as tmp:
            graph = tmp.read()
        os.system('rm main_graph.txt')

        with open('functions.txt') as tmp:
            funcs = tmp.read()
        os.system('rm functions.txt')

        self.textEdit.setText(graph)
        for i in range(len(funcs.split("\n"))-1):
            self.listWidget_2.addItem(funcs.split("\n")[i])

        for i in range(len(self.result.split("\n"))):
            self.listWidget.addItem(self.result.split("\n")[i])

        

    def getItem(self):
        current_row = self.listWidget_2.currentRow()
        if(current_row>0):
            current_item = self.listWidget_2.item(current_row)
            tmp_target = current_item.text().split(" ")
            taget = tmp_target[len(tmp_target)-1]
            r = r2pipe.open(self.filename)
            r.cmd('aaa')
            r.cmd('s ' + taget + ';' + ' agf > graph.txt')      
            r.cmd('quit')
            self.setGraph()

    def setGraph(self):
        with open('graph.txt') as tmp:
            graph = tmp.read()
        os.system('rm graph.txt') 
        self.textEdit.clear()
        self.textEdit.setText(graph)
        self.tabWidget.setCurrentIndex(1)

        

# дописать графы и остальные сегменты памяти
# ласт - добавить тайм лайн отладчик
# все запихнуть в докер