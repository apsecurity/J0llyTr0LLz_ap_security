from PyQt5 import QtWidgets, QtCore

import syscall_table

class SyscallHelpApp(QtWidgets.QWidget, syscall_table.Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.columns = ['NR','syscall name','references','rax','arg0 (rdi)','arg1 (rsi)','arg2 (rdx)','arg3 (r10)','arg4 (r8)', 'arg5 (r9)']
        self.x86_table()
        self.x86_64_table()
        self.arm_32_bit_EABI_table()
        self.arm_64_table()

    def x86_table(self):
        self.tableWidget86.clear()
        self.tableWidget86.setColumnCount(len(self.columns))
        self.tableWidget86.setHorizontalHeaderLabels(self.columns) 
        with open("./syscall_table/x86.txt",'r') as tmp:
            read_tmp = tmp.read()
        tmp_1 = read_tmp.split("\n")
        self.tableWidget86.verticalHeader().setVisible(False)
        self.tableWidget86.setRowCount(len(tmp_1))
        for i in range(len(tmp_1)):
            for j in range(len(tmp_1[i].split("\t"))):
                self.tableWidget86.setItem(i, j, QtWidgets.QTableWidgetItem(tmp_1[i].split("\t")[j]))

    def x86_64_table(self):
        self.tableWidget86_64.clear()
        self.tableWidget86_64.setColumnCount(len(self.columns))
        self.tableWidget86_64.setHorizontalHeaderLabels(self.columns) 
        with open("./syscall_table/x86_64.txt",'r') as tmp:
            read_tmp = tmp.read()
        tmp_1 = read_tmp.split("\n")
        self.tableWidget86_64.verticalHeader().setVisible(False)
        self.tableWidget86_64.setRowCount(len(tmp_1))
        for i in range(len(tmp_1)):
            for j in range(len(tmp_1[i].split("\t"))):
                self.tableWidget86_64.setItem(i, j, QtWidgets.QTableWidgetItem(tmp_1[i].split("\t")[j]))

    def arm_32_bit_EABI_table(self):
        self.tableWidgetarm32.clear()
        self.tableWidgetarm32.setColumnCount(len(self.columns))
        self.tableWidgetarm32.setHorizontalHeaderLabels(self.columns) 
        with open("./syscall_table/arm_32_bit_EABI.txt",'r') as tmp:
            read_tmp = tmp.read()
        tmp_1 = read_tmp.split("\n")
        self.tableWidgetarm32.verticalHeader().setVisible(False)
        self.tableWidgetarm32.setRowCount(len(tmp_1))
        for i in range(len(tmp_1)):
            for j in range(len(tmp_1[i].split("\t"))):
                self.tableWidgetarm32.setItem(i, j, QtWidgets.QTableWidgetItem(tmp_1[i].split("\t")[j]))

    def arm_64_table(self):
        self.tableWidgetarm64.clear()
        self.tableWidgetarm64.setColumnCount(len(self.columns))
        self.tableWidgetarm64.setHorizontalHeaderLabels(self.columns) 
        with open("./syscall_table/arm64.txt",'r') as tmp:
            read_tmp = tmp.read()
        tmp_1 = read_tmp.split("\n")
        self.tableWidgetarm64.verticalHeader().setVisible(False)
        self.tableWidgetarm64.setRowCount(len(tmp_1))
        for i in range(len(tmp_1)):
            for j in range(len(tmp_1[i].split("\t"))):
                self.tableWidgetarm64.setItem(i, j, QtWidgets.QTableWidgetItem(tmp_1[i].split("\t")[j]))