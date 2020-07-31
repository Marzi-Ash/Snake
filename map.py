from PyQt4 import QtCore, QtGui
from Snake import play, SnakeGame

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, rows, columns, snake_length):
        MainWindow.keyPressEvent = self.newOnkeyPressEvent
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(505 , 515)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 290, 60, 16))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 861, 681))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.columns = columns
        self.rows = rows
        self.snake_length = snake_length
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.Map = QtGui.QTableWidget(self.centralwidget)
        self.Map.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Map.setObjectName(_fromUtf8("Map"))
        self.Map.setColumnCount(self.columns)
        self.Map.setRowCount(self.rows)
        self.Map.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.Map.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        header = self.Map.horizontalHeader()
        header.setResizeMode(QtGui.QHeaderView.Fixed)
        header.setDefaultSectionSize(27)

        header = self.Map.verticalHeader()
        header.setResizeMode(QtGui.QHeaderView.Fixed)
        header.setDefaultSectionSize(27)
        for row in range(self.rows):# It is for vertical header and white background
            for column in range(self.columns):
                item = QtGui.QTableWidgetItem()
                item.setBackground(QtCore.Qt.white)
                self.Map.setItem(row, column, item)
        self.gridLayout.addWidget(self.Map, 0, 0, 1, 3)
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.Score_value = QtGui.QLineEdit(self.widget)
        self.Score_value.setObjectName(_fromUtf8("Score_value"))
        self.gridLayout.addWidget(self.Score_value, 1, 1, 1, 1)
        self.Play_again = QtGui.QPushButton(self.widget)
        self.Play_again.setObjectName(_fromUtf8("Play_again"))
        self.gridLayout.addWidget(self.Play_again, 1, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 889, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.Score_value.setText("Please press Enter ro start")
        self.Score_value.setReadOnly(True)

        self.flag = False
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Play_again.clicked.connect(self.play_again_bp)

    def play_again_bp(self):
        self.game = play(self.snake_length, self.columns, self.rows)
        self.draw_map()

    def newOnkeyPressEvent(self,e):
        if self.flag == True and (e.key() == QtCore.Qt.Key_Left or e.key() == QtCore.Qt.Key_A):
            if self.game.dir != "r":
                self.game.dir ="l"
            print "l"
        elif self.flag == True and (e.key() == QtCore.Qt.Key_Right or e.key() == QtCore.Qt.Key_D):
            if self.game.dir != "l":
                self.game.dir = "r"
            print "r"
        elif self.flag == True and (e.key() == QtCore.Qt.Key_Up or e.key() == QtCore.Qt.Key_W):
            if self.game.dir != "d":
                self.game.dir = "u"
            print "u"
        elif self.flag == True and (e.key() == QtCore.Qt.Key_Down or e.key() == QtCore.Qt.Key_S):
            if self.game.dir != "u":
                self.game.dir = "d"
            print "d"
        elif (e.key() == QtCore.Qt.Key_Return or e.key() == QtCore.Qt.Key_Enter) and self.flag == False:
            print ('enter')
            self.flag = True
            self.game = play(self.snake_length, self.columns, self.rows)
            self.draw_map() # for keyboard interrupt

    def draw_map(self):
        self.game.move_snake()
        err = self.game.check_for_game_over()
        if (err != 0):
            err ='Your score is '+ str(self.game.score)+ '\n'+ err
            self.f =MyPopup(err)
            self.f.setGeometry(QRect(100, 100, 400, 200))
            self.f.show()
        self.game.draw_screen()

        self.Score_value.setText(str(self.game.score))
        for r in range(self.rows):
            for c in range(self.columns):
                if self.game.board[r][c] == 0:
                    item = QtGui.QTableWidgetItem()
                    item.setBackground(QtCore.Qt.white)
                    self.Map.setItem(r, c, item)

                elif self.game.board[r][c] == 1:
                    item = QtGui.QTableWidgetItem()
                    item.setBackground(QtCore.Qt.green)
                    self.Map.setItem(r, c, item)

                else:
                    item = QtGui.QTableWidgetItem()
                    item.setBackground(QtCore.Qt.black)
                    self.Map.setItem(r, c, item)
        QtCore.QTimer.singleShot(200- 3 * (self.game.score+self.snake_length), self.draw_map) # drew board map on the ui

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Snake Game", None))
        self.label.setText(_translate("MainWindow", "Score:", None))
        self.Play_again.setText(_translate("MainWindow", "Play Again", None))
class MyPopup(QtGui.QWidget):
    def __init__(self,message):
        QtGui.QWidget.__init__(self)
        QtGui.QMessageBox.about(self,"Error", message)
        self.close()
