# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pass.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(320, 142)
        MainWindow.setStyleSheet(u"")
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
        self.label.setGeometry(QRect(0, 10, 301, 31))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 50, 251, 31))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(11)
        self.lineEdit.setFont(font1)
        self.lineEdit.setEchoMode(QLineEdit.Password)
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"	border: 1px solid rgb(170, 144, 255);\n"
"	border-radius: 10px;\n"
"	background-color: rgb(70,80, 120);\n"
"	color: rgb(197, 197, 197);\n"
"}\n"
"QLineEdit:hover{\n"
"	background-color: rgb(65,70, 110);\n"
"}")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(72, 90, 75, 23))
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 170, 0);\n"
"	border-radius: 10px;\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 170, 0, 150);\n"
"}")
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(163, 90, 75, 23))
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(170, 0, 0);\n"
"	border-radius: 10px;\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 170, 0, 150);\n"
"}")

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c:", None))
        self.lineEdit.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043a", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

