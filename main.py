import os, sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from gui_menu import *


app = QtGui.QApplication(sys.argv) # make UI
MainWindow = QtGui.QMainWindow()
ui = Main_menu()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
