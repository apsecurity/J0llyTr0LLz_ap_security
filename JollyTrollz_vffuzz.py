from PyQt5 import QtWidgets, QtCore

import os
import vffuzz

class VffuzzApp(QtWidgets.QWidget, vffuzz.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.strings = []
        self.gadgets = []
        self.objdump = []
        self.result_func = []
        self.result_gadgets = []

        self.output = ['printf', 'puts', 'putc']
        self.specificator = ['%c', '%d', '%i','%e', '%f', '%g', '%o', '%s', '%x', '%p', '%n', '%u']
        self.input = ['getchar', 'putchar', 'fgets', 'puts', 'fputs', 'scanf', 'sscanf', 'printf', 'getc', 'putc']
        self.heap = ['malloc', 'calloc', 'free', 'realloc', 'mmap', 'munmap', 'ftruncate', 'getpagesize', 'memfd_create', 'mincore', 'mlock', 'mmap2', 'mprotect', 'mremap', 'msync', 'remap_file_pages', 'setrlimit', 'shmat', 'userfaultfd', 'shm_open', 'shm_overview']
        self.str_move = ['strcpy','strcat', 'memcpy', 'memmove', 'strncpy', 'strncat', 'strcmp', 'strncmp', 'strcoll', 'strxfrm','memchr','strchr', 'strcspn','memset', 'setlocate'] 

        self.tasty_gadgets = ['call rax', 'call eax', 'call rbx', 'call ebx', 'call rcx', 'call ecx', 'call rdx', 'call edx', 'call rsi', 'call esi', 'call rdi', 'call edi','call r8', 'call r9', 'call r10', 'call r11', 'call r12', 'call r13', 'call r14', 'call r15', 'jmp rsp', 'jmp esp', 'jmp rbp', 'jmp ebp', 'jmp rax', 'jmp eax', 'jmp rbx', 'jmp ebx', 'jmp rcx', 'jmp ecx', 'jmp rdx', 'jmp edx', 'jmp rsi', 'jmp esi', 'jmp rdi', 'jmp edi', 'jmp r8', 'jmp r9', 'jmp r10', 'jmp r11', 'jmp r12', 'jmp r13', 'jmp r14', 'jmp r15', 'syscall']

        self.openFile()
        self.gadgets_func()

    def openFile(self):
        with open("vffuzz_strings.txt", 'r') as tmp:
            str_tmp = tmp.read()
        os.system("rm vffuzz_strings.txt")
        for i in str_tmp.split("\n"):
            self.strings.append(i)

        with open("vffuzz_objdump.txt", 'r') as tmp:
            str_tmp = tmp.read()
        os.system("rm vffuzz_objdump.txt")
        for i in str_tmp.split("\n"):
            self.objdump.append(i)

        with open("vffuzz_gadgets.txt",'r') as tmp:
            str_tmp = tmp.read()
        os.system("rm vffuzz_gadgets.txt")
        for i in str_tmp.split("\n"):
            self.gadgets.append(i)

        self.grepStr(self.output)
        self.grepStr(self.specificator)
        self.grepStr(self.input)
        self.grepStr(self.heap)
        self.grepStr(self.str_move)
        for i in range(len(self.result_func)):
            self.listWidget.addItem(self.result_func[i])
        self.lineEdit.setText("total: " + str(len(self.result_func)))

    def grepStr(self, string):
            self.listWidget.clear()
            count = 0
            for j in string:
                textReg = j
                reg = QtCore.QRegExp(textReg)
                tmp_strings = []
                for i in range(len(self.strings)):
                    pos = reg.indexIn(self.strings[i],0)
                    while pos != -1:
                        tmp_strings.append(self.strings[i])
                        pos += reg.matchedLength()
                        pos = reg.indexIn(self.strings[i], pos)
                        count += 1
                if(count != 0):
                    for i in range(len(tmp_strings)):
                        self.result_func.append(self.find_objdump(tmp_strings[i]) + ' ' + tmp_strings[i])

    def gadgets_func(self):
        self.listWidget_2.clear()
        for j in self.tasty_gadgets:
            textReg = j
            reg = QtCore.QRegExp(textReg)
            tmp_strings = []
            for i in range(len(self.gadgets)):
                pos = reg.indexIn(self.gadgets[i],0)
                while pos != -1:
                    self.result_gadgets.append(self.gadgets[i])
                    pos += reg.matchedLength()
                    pos = reg.indexIn(self.gadgets[i], pos)
        for i in range(len(self.result_gadgets)):
            self.listWidget_2.addItem(self.result_gadgets[i])
        self.lineEdit_2.setText("total: " + str(len(self.result_gadgets)))        
            
    def find_objdump(self, strong):
        textReg = strong
        count = 0
        reg = QtCore.QRegExp(textReg)
        tmp_strings = []
        for i in range(len(self.objdump)):
            pos = reg.indexIn(self.objdump[i],0)
            while pos != -1:
                tmp_strings.append(self.objdump[i])
                pos += reg.matchedLength()
                pos = reg.indexIn(self.objdump[i], pos)
                count += 1
        if(count != 0):
            return tmp_strings[0].split(" ")[0]
        else:
            return ""
