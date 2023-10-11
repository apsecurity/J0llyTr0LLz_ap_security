from PyQt5 import QtWidgets, QtCore

from capstone import *
import binascii
from PyQt5.QtWidgets import QMessageBox

import jtdisasm

class JTDisasmApp(QtWidgets.QMainWindow, jtdisasm.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bytecode = bytearray()
        self.actionOpen.triggered.connect(self.openFile)
        self.actionDisassembly.triggered.connect(self.disasm)

    def openFile(self):
        file = QtWidgets.QFileDialog.getOpenFileName()
        if(len(file[0]) != 0):
            with open(file[0], 'rb') as tmp:
                barray = bytearray(tmp.read())
            self.bytecode = barray
            self.disasm()
        else:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Can't open file")
            msgBox.setWindowTitle("ATTENTION")
            msgBox.setStandardButtons(QMessageBox.Ok)
            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Ok:
                return 0

    def disasm(self):
        TEXT_CS_ARCH = 0
        TEXT_CS_MODE = 0
        instr = ""
        self.listWidget.clear()

        if(self.comboBox.currentText() == 'ARCH_X86'):
            TEXT_CS_ARCH = CS_ARCH_X86
        elif(self.comboBox.currentText() == 'ARCH_ARM'):
            TEXT_CS_ARCH = CS_ARCH_ARM
        elif(self.comboBox.currentText() == 'ARCH_MIPS'):
            TEXT_CS_ARCH = CS_ARCH_MIPS
        elif(self.comboBox.currentText() == 'ARCH_PPC'):
            TEXT_CS_ARCH = CS_ARCH_PPC

        if(self.comboBox_2.currentText() == 'MODE_32'):
            TEXT_CS_MODE = CS_MODE_32
        elif(self.comboBox_2.currentText() == 'MODE_ARM'):
            TEXT_CS_MODE = CS_MODE_ARM
        elif(self.comboBox_2.currentText() == 'MODE_THUMB'):
            TEXT_CS_MODE = CS_MODE_THUMB
        elif(self.comboBox_2.currentText() == 'MODE_64'):
            TEXT_CS_MODE = CS_MODE_64
        elif(self.comboBox_2.currentText() == 'MODE_MIPS_32'):
            TEXT_CS_MODE = CS_MODE_MIPS32
        elif(self.comboBox_2.currentText() == 'MODE_MIPS_64'):
            TEXT_CS_MODE = CS_MODE_MIPS64
        elif(self.comboBox_2.currentText() == 'MODE_MIPS_32R6'):
            TEXT_CS_MODE = CS_MODE_MIPS32R6

        if(self.lineEdit.text().isdigit()):
            entryPoint = int(self.lineEdit.text())
        else:
            entryPoint = 0x400000

        try:
            md = Cs(TEXT_CS_ARCH, TEXT_CS_MODE)
            md.syntax = CS_OPT_SYNTAX_INTEL
            md.detail = True
            count = 0
            for i in md.disasm(self.bytecode, entryPoint):
                tmp_byte = str(binascii.hexlify(bytearray(i.bytes)))[2:]
                self.listWidget.addItem("0x{}:\t{}\t{}\t{}".format(i.address, tmp_byte[:len(tmp_byte)-1], i.mnemonic, i.op_str))
        except:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Can't disassembly")
            msgBox.setWindowTitle("ATTENTION")
            msgBox.setStandardButtons(QMessageBox.Ok)
            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Ok:
                return 0
        self.toHex()
            
    def toHex(self):
        tmp = ""
        self.hexTextEdit.clear()
        for i in range(len(self.bytecode)):
            if(i%8 == 0 and i != 0):
                tmp += "\n"
            if(self.bytecode[i] < 16):
                tmp += "0" + hex(self.bytecode[i])[2:] + " "
            else:
                tmp += hex(self.bytecode[i])[2:] + " "
        self.hexTextEdit.setText(tmp)
        self.fromHex()
    
    def fromHex(self):
        tmp = ""
        self.fromHexTextEdit.clear()
        for i in range(len(self.bytecode)):
            if(i%16 == 0 and i != 0):
                tmp += "\n"
            tmp += chr(self.bytecode[i])
        self.fromHexTextEdit.setText(tmp) 