# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screenwevrqS.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(340, 340)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.circularProgressBarBase = QFrame(self.centralwidget)
        self.circularProgressBarBase.setObjectName(u"circularProgressBarBase")
        self.circularProgressBarBase.setGeometry(QRect(10, 10, 320, 320))
        self.circularProgressBarBase.setFrameShape(QFrame.NoFrame)
        self.circularProgressBarBase.setFrameShadow(QFrame.Raised)
        self.circularProgress = QFrame(self.circularProgressBarBase)
        self.circularProgress.setObjectName(u"circularProgress")
        self.circularProgress.setGeometry(QRect(10, 10, 300, 300))
        self.circularProgress.setStyleSheet(u"QFrame{\n"
"	border-radius: 150px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255, 0, 127, 0), stop:0.75 rgba(168, 218, 220, 255))\n"
"}")
        self.circularProgress.setFrameShape(QFrame.NoFrame)
        self.circularProgress.setFrameShadow(QFrame.Raised)
        self.circularBg = QFrame(self.circularProgressBarBase)
        self.circularBg.setObjectName(u"circularBg")
        self.circularBg.setGeometry(QRect(10, 10, 300, 300))
        self.circularBg.setStyleSheet(u"QFrame{\n"
"	border-radius: 150px;\n"
"	background-color: rgba(77, 77, 127, 120);\n"
"}")
        self.circularBg.setFrameShape(QFrame.NoFrame)
        self.circularBg.setFrameShadow(QFrame.Raised)
        self.container = QFrame(self.circularProgressBarBase)
        self.container.setObjectName(u"container")
        self.container.setGeometry(QRect(25, 25, 270, 270))
        self.container.setStyleSheet(u"QFrame{\n"
"	border-radius: 135px;\n"
"	background-color: rgb(69, 123, 157);\n"
"}")
        self.container.setFrameShape(QFrame.NoFrame)
        self.container.setFrameShadow(QFrame.Raised)
        self.widget = QWidget(self.container)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 40, 191, 201))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.labelTitle = QLabel(self.widget)
        self.labelTitle.setObjectName(u"labelTitle")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        self.labelTitle.setFont(font)
        self.labelTitle.setStyleSheet(u"background-color: none;\n"
"color: #FFFFFF;")
        self.labelTitle.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelTitle, 0, 0, 1, 1)

        self.labelPercentage = QLabel(self.widget)
        self.labelPercentage.setObjectName(u"labelPercentage")
        font1 = QFont()
        font1.setFamily(u"Yu Gothic Light")
        font1.setPointSize(48)
        self.labelPercentage.setFont(font1)
        self.labelPercentage.setStyleSheet(u"background-color: none;\n"
"color: #FFFFFF;")
        self.labelPercentage.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelPercentage, 1, 0, 1, 1)

        self.labelLoading = QLabel(self.widget)
        self.labelLoading.setObjectName(u"labelLoading")
        self.labelLoading.setMinimumSize(QSize(0, 20))
        self.labelLoading.setMaximumSize(QSize(16777215, 20))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(9)
        self.labelLoading.setFont(font2)
        self.labelLoading.setStyleSheet(u"QLabel{\n"
"	border-radius: 10px;	\n"
"	background-color: rgb(95, 133, 157);\n"
"	color: #FFFFFF;\n"
"	margin-left: 40px;\n"
"	margin-right: 40px;\n"
"}")
        self.labelLoading.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelLoading, 2, 0, 1, 1)

        self.labelTitle_3 = QLabel(self.widget)
        self.labelTitle_3.setObjectName(u"labelTitle_3")
        self.labelTitle_3.setFont(font2)
        self.labelTitle_3.setStyleSheet(u"background-color: none;\n"
"color: rgb(112, 200, 255)")
        self.labelTitle_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelTitle_3, 3, 0, 1, 1)

        self.circularBg.raise_()
        self.circularProgress.raise_()
        self.container.raise_()
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.labelTitle.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p><span style=\" font-weight:600; color:#70c8ff;\">NEX</span>Parameter</p></body></html>", None))
        self.labelPercentage.setText(QCoreApplication.translate("SplashScreen", u"<p><span style=\" font-size:58pt;\">0</span><span style=\" font-size:48pt; vertical-align:super;\">%</span></p>", None))
        self.labelLoading.setText(QCoreApplication.translate("SplashScreen", u"loading...", None))
        self.labelTitle_3.setText(QCoreApplication.translate("SplashScreen", u"NEXCONTROL", None))
    # retranslateUi

