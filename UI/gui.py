# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class MySignals(QObject):
    sig_files = Signal(str)

class DropFrame(QFrame):
    def __init__(self, parent):
        super(DropFrame, self).__init__(parent)
        self.setAcceptDrops(True)
        self.sig = MySignals()
        self.sig.sig_files.connect(parent.parent().parent().cip_files)

    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls():
            e.acceptProposedAction()
            self.setStyleSheet(u"QFrame{\n"
                               "	border: 4px solid rgb(170, 144, 255);\n"
                               "	border-radius: 15px;\n"
                               "	background-color: rgb(65,70, 110);\n"
                               "	color: rgb(197, 197, 197);\n"
                               "}\n""QFrame:hover{\n"
                                "	background-color: rgb(65,70, 110);\n"
                                "}")

    def dragLeaveEvent(self, event):
        self.setStyleSheet(u"QFrame{\n"
                           "	border: 4px solid rgb(170, 144, 255);\n"
                           "	border-radius: 15px;\n"
                           "	background-color: rgb(58,60, 100);\n"
                           "	color: rgb(197, 197, 197);\n"
                           "}\n""QFrame:hover{\n"
                            "	background-color: rgb(65,70, 110);\n"
                            "}")

    def dropEvent(self, e):
        file_name =[]
        for url in e.mimeData().urls():
            file_name.append(url.toLocalFile())
        self.sig.sig_files.emit('-*--*-'.join(file_name))

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(536, 378)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(56, 58, 89);\n"
"	color: rgb(197, 197, 197);\n"
"	border-radius: 10px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(5, 10, 511, 62))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(35)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignCenter)
        self.frame_2 = DropFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(40, 100, 431, 231))
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	border: 4px solid rgb(170, 144, 255);\n"
"	border-radius: 15px;\n"
"	background-color: rgb(58,60, 100);\n"
"	color: rgb(197, 197, 197);\n"
"}\n"
"QFrame:hover{\n"
"	background-color: rgb(65,70, 110);\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 40, 291, 141))
        font1 = QFont()
        font1.setFamily(u"Segoe UI Light")
        font1.setPointSize(21)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"QLabel{\n"
"border: none;\n"
"background-color: none;\n"
"}")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.exitButton = QPushButton(self.frame)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setGeometry(QRect(490, 10, 20, 20))
        self.exitButton.setMinimumSize(QSize(20, 20))
        self.exitButton.setMaximumSize(QSize(20, 20))
        self.exitButton.setBaseSize(QSize(20, 20))
        self.exitButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 37, 102);\n"
"    border-radius:9px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 37, 102,150);\n"
"}")

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    @Slot(str)
    def cip_files(self, val):
        pass

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0411\u044b\u0441\u0442\u0440\u044b\u0439 \u0448\u0438\u0444\u0440\u0430\u0442\u043e\u0440", None))
        # self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u043d\u0435\u0441\u0438 \u0441\u044e\u0434\u0430 \u0444\u0430\u0439\u043b\u044b \u0447\u0442\u043e\u0431\u044b \u0437\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Перенеси сюда, чтобы зашифровать/расшифровать файлы", None))
        self.exitButton.setText("")
    # retranslateUi

