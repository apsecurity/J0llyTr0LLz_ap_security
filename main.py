# from email.policy import default
# from fileinput import filename
import sys
from PyQt5 import QtWidgets

from JollyTrollz import *

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = JollyTrollz()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()