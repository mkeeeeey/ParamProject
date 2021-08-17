# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_loginsQXqAQ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import splash_logo_rc

class Ui_splashLogin(object):
    def setupUi(self, splashLogin):
        if not splashLogin.objectName():
            splashLogin.setObjectName(u"splashLogin")
        splashLogin.resize(441, 551)
        self.centralwidget = QWidget(splashLogin)
        self.centralwidget.setObjectName(u"centralwidget")
        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setGeometry(QRect(0, 0, 441, 551))
        self.main_frame.setStyleSheet(u"border: 4px solid rgb(29, 53, 87);\n"
"border-radius: 12px;\n"
"background-color: qlineargradient(spread:pad, x1:0.078, y1:0.522864, x2:1, y2:0.528, stop:0 rgba(241, 250, 238, 255), stop:1 rgba(168, 218, 220, 255));")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.logo_frame = QFrame(self.centralwidget)
        self.logo_frame.setObjectName(u"logo_frame")
        self.logo_frame.setGeometry(QRect(40, 70, 361, 80))
        self.logo_frame.setStyleSheet(u"image: url(:/images/images/image001.png);")
        self.logo_frame.setFrameShape(QFrame.StyledPanel)
        self.logo_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(80, 250, 281, 271))
        self.gridLayout = QGridLayout(self.verticalLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.newBtn = QPushButton(self.verticalLayoutWidget)
        self.newBtn.setObjectName(u"newBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newBtn.sizePolicy().hasHeightForWidth())
        self.newBtn.setSizePolicy(sizePolicy)
        self.newBtn.setStyleSheet(u"background-color: rgb(69, 123, 157);\n"
"color: rgb(255, 255, 255);\n"
"font: 15pt \"Copperplate Gothic Bold\";\n"
"border-radius: 15px;")

        self.gridLayout.addWidget(self.newBtn, 0, 0, 1, 1)

        self.openBtn = QPushButton(self.verticalLayoutWidget)
        self.openBtn.setObjectName(u"openBtn")
        sizePolicy.setHeightForWidth(self.openBtn.sizePolicy().hasHeightForWidth())
        self.openBtn.setSizePolicy(sizePolicy)
        self.openBtn.setStyleSheet(u"background-color: rgb(69, 123, 157);\n"
"color: rgb(255, 255, 255);\n"
"font: 15pt \"Copperplate Gothic Bold\";\n"
"border-radius: 15px;")

        self.gridLayout.addWidget(self.openBtn, 1, 0, 1, 1)

        self.editBtn = QPushButton(self.verticalLayoutWidget)
        self.editBtn.setObjectName(u"editBtn")
        sizePolicy.setHeightForWidth(self.editBtn.sizePolicy().hasHeightForWidth())
        self.editBtn.setSizePolicy(sizePolicy)
        self.editBtn.setStyleSheet(u"background-color: rgb(69, 123, 157);\n"
"color: rgb(255, 255, 255);\n"
"font: 15pt \"Copperplate Gothic Bold\";\n"
"border-radius: 15px;")

        self.gridLayout.addWidget(self.editBtn, 2, 0, 1, 1)

        self.exitBtn = QPushButton(self.centralwidget)
        self.exitBtn.setObjectName(u"exitBtn")
        self.exitBtn.setGeometry(QRect(400, 10, 31, 31))
        self.exitBtn.setStyleSheet(u"background-color: rgb(69, 123, 157);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Arial\";\n"
"border-radius: 10px;")
        splashLogin.setCentralWidget(self.centralwidget)

        self.retranslateUi(splashLogin)

        QMetaObject.connectSlotsByName(splashLogin)
    # setupUi

    def retranslateUi(self, splashLogin):
        splashLogin.setWindowTitle(QCoreApplication.translate("splashLogin", u"MainWindow", None))
        self.newBtn.setText(QCoreApplication.translate("splashLogin", u"New", None))
        self.openBtn.setText(QCoreApplication.translate("splashLogin", u"Open", None))
        self.editBtn.setText(QCoreApplication.translate("splashLogin", u"Edit Data", None))
        self.exitBtn.setText(QCoreApplication.translate("splashLogin", u"X", None))
    # retranslateUi

