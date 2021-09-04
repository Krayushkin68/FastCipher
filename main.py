import gui
import passw
import MyCipher
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import os


class FastShifr(gui.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(FastShifr, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.exitButton.clicked.connect(self.appexit)

    def appexit(self):
        app.exit()

    def mouseMoveEvent(self, event:QtGui.QMouseEvent):
        self.move(self.pos() + event.globalPos() - self.dragPos)
        self.dragPos = event.globalPos()

    def mousePressEvent(self, event:QtGui.QMouseEvent):
        self.dragPos = event.globalPos()

    def cip_files(self, val):
        global files
        files = val.split('-*--*-')
        global epas
        epas = PassWindow()
        epas.show()


class PassWindow(passw.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(PassWindow, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.pushButton.clicked.connect(self.p_ok)
        self.pushButton_2.clicked.connect(self.p_back)
        self.lineEdit.setFocus()

    def p_ok(self):
        passw = self.lineEdit.text()
        if passw:
            start_cip(passw)
            self.close()
        else:
            print('no passw')
            self.close()

    def p_back(self):
        self.close()

    def mouseMoveEvent(self, event: QtGui.QMouseEvent):
        self.move(self.pos() + event.globalPos() - self.dragPos)
        self.dragPos = event.globalPos()

    def mousePressEvent(self, event:QtGui.QMouseEvent):
        self.dragPos = event.globalPos()


def start_cip(passw):
    cipher = MyCipher.MyCipher(passw)
    for f in files:
        if f.endswith('.crypt'):
            cipher.decrypt_file_aes(f, f[:-6])
        else:
            cipher.encrypt_file_aes(f, f+'.crypt')



if __name__ == '__main__':
    files = []
    app = QtWidgets.QApplication()
    sh = FastShifr()
    sh.show()
    app.exec_()