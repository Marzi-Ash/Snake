from PyQt4 import QtCore, QtGui
from map import *
import os, sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Main_menu(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(410, 509)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.Start_button = QtGui.QPushButton(self.centralwidget)
        self.Start_button.setObjectName(_fromUtf8("Start_button"))
        self.gridLayout.addWidget(self.Start_button, 5, 0, 1, 2)
        self.Board_height_value = QtGui.QLineEdit(self.centralwidget)
        self.Board_height_value.setText(_fromUtf8(""))
        self.Board_height_value.setObjectName(_fromUtf8("Board_height_value"))
        self.gridLayout.addWidget(self.Board_height_value, 2, 1, 1, 1)
        self.Board_width_value = QtGui.QLineEdit(self.centralwidget)
        self.Board_width_value.setText(_fromUtf8(""))
        self.Board_width_value.setObjectName(_fromUtf8("Board_width_value"))
        self.gridLayout.addWidget(self.Board_width_value, 3, 1, 1, 1)
        self.Board_width_label = QtGui.QLabel(self.centralwidget)
        self.Board_width_label.setObjectName(_fromUtf8("Board_width_label"))
        self.gridLayout.addWidget(self.Board_width_label, 3, 0, 1, 1)
        self.snake_length_value = QtGui.QLineEdit(self.centralwidget)
        self.snake_length_value.setText(_fromUtf8(""))
        self.snake_length_value.setObjectName(_fromUtf8("snake_length_value"))
        self.gridLayout.addWidget(self.snake_length_value, 4, 1, 1, 1)
        self.Snake_lenght_label = QtGui.QLabel(self.centralwidget)
        self.Snake_lenght_label.setObjectName(_fromUtf8("Snake_lenght_label"))
        self.gridLayout.addWidget(self.Snake_lenght_label, 4, 0, 1, 1)
        self.Board_height_label = QtGui.QLabel(self.centralwidget)
        self.Board_height_label.setObjectName(_fromUtf8("Board_height_label"))
        self.gridLayout.addWidget(self.Board_height_label, 2, 0, 1, 1)

        self.Picture = QtGui.QLabel(self.centralwidget)
        self.Picture.setText(_fromUtf8(""))
        self.Picture.setObjectName(_fromUtf8("Picture"))
        self.Picture.setPixmap(QtGui.QPixmap(os.getcwd() + "/snake"))
        self.gridLayout.addWidget(self.Picture, 1, 0, 1, 2)
        self.welcom_label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.welcom_label.sizePolicy().hasHeightForWidth())
        self.welcom_label.setSizePolicy(sizePolicy)
        self.welcom_label.setAlignment(QtCore.Qt.AlignCenter)
        self.welcom_label.setObjectName(_fromUtf8("welcom_label"))
        self.gridLayout.addWidget(self.welcom_label, 0, 0, 1, 2)
        self.Board_height_value.raise_()
        self.Start_button.raise_()
        self.snake_length_value.raise_()
        self.Snake_lenght_label.raise_()
        self.Board_height_label.raise_()
        self.Board_width_label.raise_()
        self.Board_width_value.raise_()
        self.Picture.raise_()
        self.welcom_label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 509, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Start_button.clicked.connect(self.start_pb)
    def start_pb(self):
        snake_length = int(self.snake_length_value.text())
        Board_width = int(self.Board_width_value.text())
        Board_height = int(self.Board_height_value.text())
        if (snake_length > Board_width and snake_length > Board_height):
            print ('it is not ok')
            message = "Please, increase the size of board or decrease the length of snake!"
            self.f =MyPopup(message)
            self.f.setGeometry(QRect(100, 100, 400, 200))
            self.f.show()
        elif (Board_width>15 or Board_height >15):
            message = "Please resize the board to under 15!"
            self.f =MyPopup(message)
            self.f.setGeometry(QRect(100, 100, 400, 200))
            self.f.show()
        else:
            print ('it is ok')
            self.window = QtGui.QMainWindow()
            self.ui= Ui_MainWindow()
            self.ui.setupUi(self.window,Board_height, Board_width, snake_length)
            self.window.show()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Snake Game", None))
        self.Start_button.setText(_translate("MainWindow", "Start Game", None))
        self.Board_width_label.setText(_translate("MainWindow", "Board Width", None))
        self.Snake_lenght_label.setText(_translate("MainWindow", "Snake Length", None))
        self.Board_height_label.setText(_translate("MainWindow", "Board Height ", None))
        self.welcom_label.setText(_translate("MainWindow", " Snake Game", None))

class MyPopup(QtGui.QWidget):
    def __init__(self,message):
        QtGui.QWidget.__init__(self)
        QtGui.QMessageBox.about(self,"Error", message)
        self.close()
