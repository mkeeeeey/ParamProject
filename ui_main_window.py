# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test_windowKFlkhe.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc
from connDB import modelBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1163, 654)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        icon = QIcon()
        icon.addFile(u"../../Downloads/icons8-file-80.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNew.setIcon(icon)
        self.actionopen = QAction(MainWindow)
        self.actionopen.setObjectName(u"actionopen")
        icon1 = QIcon()
        icon1.addFile(u"../../Documents/NEX/images/icons8-opened-folder-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionopen.setIcon(icon1)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        icon2 = QIcon()
        icon2.addFile(u":/images/images/icons8-save-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave.setIcon(icon2)
        self.actionSave_As = QAction(MainWindow)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.actionSave_as_CSV = QAction(MainWindow)
        self.actionSave_as_CSV.setObjectName(u"actionSave_as_CSV")
        icon3 = QIcon()
        icon3.addFile(u"../../Documents/NEX/images/icons8-csv-80.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave_as_CSV.setIcon(icon3)
        self.actionPrint = QAction(MainWindow)
        self.actionPrint.setObjectName(u"actionPrint")
        icon4 = QIcon()
        icon4.addFile(u"../../Documents/NEX/images/icons8-print-80.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionPrint.setIcon(icon4)
        self.actionFind = QAction(MainWindow)
        self.actionFind.setObjectName(u"actionFind")
        icon5 = QIcon()
        icon5.addFile(u"../../Documents/NEX/images/icons8-search-80.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionFind.setIcon(icon5)
        self.actionTool = QAction(MainWindow)
        self.actionTool.setObjectName(u"actionTool")
        self.actionTool.setCheckable(True)
        self.actionTool.setChecked(True)
        self.actionCategory = QAction(MainWindow)
        self.actionCategory.setObjectName(u"actionCategory")
        self.actionCategory.setCheckable(True)
        self.actionCategory.setChecked(True)
        self.actionKorean = QAction(MainWindow)
        self.actionKorean.setObjectName(u"actionKorean")
        self.actionKorean.setCheckable(True)
        icon6 = QIcon()
        icon6.addFile(u"../../Documents/NEX/images/south-korea.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionKorean.setIcon(icon6)
        self.actionEnglish = QAction(MainWindow)
        self.actionEnglish.setObjectName(u"actionEnglish")
        self.actionEnglish.setCheckable(True)
        icon7 = QIcon()
        icon7.addFile(u"../../Documents/NEX/images/united-kingdom (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionEnglish.setIcon(icon7)
        self.actionUpload_All = QAction(MainWindow)
        self.actionUpload_All.setObjectName(u"actionUpload_All")
        icon8 = QIcon()
        icon8.addFile(u"../../Documents/NEX/images/icons8-upload-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionUpload_All.setIcon(icon8)
        self.actionUpload_Pattern = QAction(MainWindow)
        self.actionUpload_Pattern.setObjectName(u"actionUpload_Pattern")
        self.actionDownload_All = QAction(MainWindow)
        self.actionDownload_All.setObjectName(u"actionDownload_All")
        icon9 = QIcon()
        icon9.addFile(u"../../Documents/NEX/images/icons8-download-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionDownload_All.setIcon(icon9)
        self.actionDownload_Pattern = QAction(MainWindow)
        self.actionDownload_Pattern.setObjectName(u"actionDownload_Pattern")
        self.actionCompare_File = QAction(MainWindow)
        self.actionCompare_File.setObjectName(u"actionCompare_File")
        self.actionInitialize_to_Factory_Default = QAction(MainWindow)
        self.actionInitialize_to_Factory_Default.setObjectName(u"actionInitialize_to_Factory_Default")
        self.actionInitialize_to_User_Default = QAction(MainWindow)
        self.actionInitialize_to_User_Default.setObjectName(u"actionInitialize_to_User_Default")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        icon10 = QIcon()
        icon10.addFile(u"../../Documents/NEX/images/icons8-help-80.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionHelp.setIcon(icon10)
        self.actionUser = QAction(MainWindow)
        self.actionUser.setObjectName(u"actionUser")
        self.actionAdmin = QAction(MainWindow)
        self.actionAdmin.setObjectName(u"actionAdmin")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_main)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_top.sizePolicy().hasHeightForWidth())
        self.frame_top.setSizePolicy(sizePolicy)
        self.frame_top.setMaximumSize(QSize(16777215, 70))
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_top)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_bar = QFrame(self.frame_top)
        self.frame_top_bar.setObjectName(u"frame_top_bar")
        self.frame_top_bar.setMaximumSize(QSize(16777215, 35))
        self.frame_top_bar.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(29, 53, 87);\n"
"}")
        self.frame_top_bar.setFrameShape(QFrame.NoFrame)
        self.frame_top_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_top_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_title_bar = QFrame(self.frame_top_bar)
        self.frame_title_bar.setObjectName(u"frame_title_bar")
        self.frame_title_bar.setMaximumSize(QSize(16777215, 35))
        self.frame_title_bar.setFrameShape(QFrame.NoFrame)
        self.frame_title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_title_bar)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_for_center = QFrame(self.frame_title_bar)
        self.frame_for_center.setObjectName(u"frame_for_center")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_for_center.sizePolicy().hasHeightForWidth())
        self.frame_for_center.setSizePolicy(sizePolicy1)
        self.frame_for_center.setMaximumSize(QSize(105, 35))
        self.frame_for_center.setFrameShape(QFrame.NoFrame)
        self.frame_for_center.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame_for_center)

        self.label_app_title = QLabel(self.frame_title_bar)
        self.label_app_title.setObjectName(u"label_app_title")
        font = QFont()
        font.setFamily(u"Calibri")
        font.setPointSize(16)
        self.label_app_title.setFont(font)
        self.label_app_title.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_app_title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_app_title)

        self.horizontalLayout.addWidget(self.frame_title_bar)

        self.frame_top_btn = QFrame(self.frame_top_bar)
        self.frame_top_btn.setObjectName(u"frame_top_btn")
        self.frame_top_btn.setMaximumSize(QSize(105, 35))
        self.frame_top_btn.setFrameShape(QFrame.NoFrame)
        self.frame_top_btn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_top_btn)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_top_btn)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy1.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy1)
        self.btn_minimize.setMaximumSize(QSize(35, 35))
        self.btn_minimize.setStyleSheet(u"QPushButton{\n"
"	image: url(:/icons/images/icons/icon_minimize.png);\n"
"}")
        self.btn_minimize.setFlat(True)

        self.horizontalLayout_2.addWidget(self.btn_minimize)

        self.btn_maximize = QPushButton(self.frame_top_btn)
        self.btn_maximize.setObjectName(u"btn_maximize")
        sizePolicy1.setHeightForWidth(self.btn_maximize.sizePolicy().hasHeightForWidth())
        self.btn_maximize.setSizePolicy(sizePolicy1)
        self.btn_maximize.setMaximumSize(QSize(35, 35))
        self.btn_maximize.setStyleSheet(u"QPushButton{\n"
"	image: url(:/icons/images/icons/icon_maximize.png);\n"
"}")
        self.btn_maximize.setFlat(True)

        self.horizontalLayout_2.addWidget(self.btn_maximize)

        self.btn_close = QPushButton(self.frame_top_btn)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy1.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy1)
        self.btn_close.setMaximumSize(QSize(35, 35))
        self.btn_close.setStyleSheet(u"QPushButton{\n"
"	image: url(:/icons/images/icons/icon_close.png);\n"
"}")
        self.btn_close.setFlat(True)

        self.horizontalLayout_2.addWidget(self.btn_close)

        self.horizontalLayout.addWidget(self.frame_top_btn)

        self.verticalLayout_3.addWidget(self.frame_top_bar)

        self.frame_menu_bar = QFrame(self.frame_top)
        self.frame_menu_bar.setObjectName(u"frame_menu_bar")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_menu_bar.sizePolicy().hasHeightForWidth())
        self.frame_menu_bar.setSizePolicy(sizePolicy2)
        self.frame_menu_bar.setMaximumSize(QSize(16777215, 35))
        self.frame_menu_bar.setStyleSheet(u"Qframe{\n"
"	background-color: rgb(69, 123, 157);\n"
"}")
        self.frame_menu_bar.setFrameShape(QFrame.NoFrame)
        self.frame_menu_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_menu_bar)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.menubar = QMenuBar(self.frame_menu_bar)
        self.menubar.setObjectName(u"menubar")
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(13)
        self.menubar.setFont(font1)
        self.menubar.setLayoutDirection(Qt.LeftToRight)
        self.menubar.setStyleSheet(u"QMenuBar{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(69, 123, 157);\n"
"}")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuLanguage = QMenu(self.menuView)
        self.menuLanguage.setObjectName(u"menuLanguage")
        self.menuCommunication = QMenu(self.menubar)
        self.menuCommunication.setObjectName(u"menuCommunication")
        self.menuOperation = QMenu(self.menubar)
        self.menuOperation.setObjectName(u"menuOperation")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuMode_2 = QMenu(self.menubar)
        self.menuMode_2.setObjectName(u"menuMode_2")

        self.horizontalLayout_3.addWidget(self.menubar)

        self.verticalLayout_3.addWidget(self.frame_menu_bar)

        self.verticalLayout_2.addWidget(self.frame_top)

        self.frame_content = QFrame(self.frame_main)
        self.frame_content.setObjectName(u"frame_content")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_content.sizePolicy().hasHeightForWidth())
        self.frame_content.setSizePolicy(sizePolicy3)
        self.frame_content.setMinimumSize(QSize(1163, 586))
        self.frame_content.setStyleSheet(u"background-color: rgb(237, 242, 244);")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_content)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_content = QWidget(self.frame_content)
        self.widget_content.setObjectName(u"widget_content")
        sizePolicy3.setHeightForWidth(self.widget_content.sizePolicy().hasHeightForWidth())
        self.widget_content.setSizePolicy(sizePolicy3)
        self.widget_content.setMinimumSize(QSize(1163, 586))
        self.gridLayout_5 = QGridLayout(self.widget_content)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.widget_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy3.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy3)
        self.stackedWidget.setMinimumSize(QSize(1163, 586))
        self.stackedWidget.setMaximumSize(QSize(16777215, 16777215))
        self.stackedWidget.setStyleSheet(u"")
        self.page_select = QWidget()
        self.page_select.setObjectName(u"page_select")
        sizePolicy3.setHeightForWidth(self.page_select.sizePolicy().hasHeightForWidth())
        self.page_select.setSizePolicy(sizePolicy3)
        self.gridLayout_6 = QGridLayout(self.page_select)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_select_model = QFrame(self.page_select)
        self.frame_select_model.setObjectName(u"frame_select_model")
        sizePolicy1.setHeightForWidth(self.frame_select_model.sizePolicy().hasHeightForWidth())
        self.frame_select_model.setSizePolicy(sizePolicy1)
        self.frame_select_model.setMinimumSize(QSize(1163, 586))
        self.frame_select_model.setMaximumSize(QSize(16777215, 16777215))
        self.frame_select_model.setFrameShape(QFrame.StyledPanel)
        self.frame_select_model.setFrameShadow(QFrame.Raised)
        self.frame_mode_btn = QFrame(self.frame_select_model)
        self.frame_mode_btn.setObjectName(u"frame_mode_btn")
        self.frame_mode_btn.setGeometry(QRect(480, 400, 241, 101))
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_mode_btn.sizePolicy().hasHeightForWidth())
        self.frame_mode_btn.setSizePolicy(sizePolicy4)
        self.frame_mode_btn.setFrameShape(QFrame.StyledPanel)
        self.frame_mode_btn.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_mode_btn)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_user = QPushButton(self.frame_mode_btn)
        self.btn_user.setObjectName(u"btn_user")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.btn_user.sizePolicy().hasHeightForWidth())
        self.btn_user.setSizePolicy(sizePolicy5)
        self.btn_user.setStyleSheet(u"background-color: rgb(168, 218, 220);\n"
"font: 75 16pt \"Consolas\";")

        self.gridLayout.addWidget(self.btn_user, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.btn_admin = QPushButton(self.frame_mode_btn)
        self.btn_admin.setObjectName(u"btn_admin")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.btn_admin.sizePolicy().hasHeightForWidth())
        self.btn_admin.setSizePolicy(sizePolicy6)
        self.btn_admin.setStyleSheet(u"background-color: rgb(168, 218, 220);\n"
"font: 75 16pt \"Consolas\";")

        self.gridLayout.addWidget(self.btn_admin, 0, 2, 1, 1)

        self.frame_model = QFrame(self.frame_select_model)
        self.frame_model.setObjectName(u"frame_model")
        self.frame_model.setGeometry(QRect(430, 190, 351, 202))
        self.frame_model.setStyleSheet(u"QComboBox:hover{border: 2px solid rgb(29, 53, 87);}\n"
"QComboBox{height: 30px;}\n"
"QComboBox::drop-down{\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 30px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-color: rgb(69, 123, 157);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {	\n"
"	color: rgb(29, 53, 87);\n"
"	background-color: rgb(168, 218, 220);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(69, 123, 157);\n"
"}\n"
"QLabel{\n"
"	\n"
"	font: 75 12pt \"Arial\";\n"
"\n"
"}")
        self.frame_model.setFrameShape(QFrame.NoFrame)
        self.frame_model.setFrameShadow(QFrame.Raised)
        self.formLayout_5 = QFormLayout(self.frame_model)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.formLayout_5.setLabelAlignment(Qt.AlignCenter)
        self.formLayout_5.setFormAlignment(Qt.AlignCenter)
        self.formLayout_5.setHorizontalSpacing(20)
        self.formLayout_5.setVerticalSpacing(10)
        self.formLayout_5.setContentsMargins(-1, -1, 11, -1)
        self.label_model = QLabel(self.frame_model)
        self.label_model.setObjectName(u"label_model")
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(9)
        self.label_model.setFont(font2)
        self.label_model.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_model)

        self.box_model = QComboBox(self.frame_model)
        self.box_model.setObjectName(u"box_model")
        self.box_model.addItems(modelBox())
        font3 = QFont()
        font3.setPointSize(11)
        self.box_model.setFont(font3)
        self.box_model.setStyleSheet(u"")

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.box_model)

        self.label_board = QLabel(self.frame_model)
        self.label_board.setObjectName(u"label_board")
        self.label_board.setFont(font2)

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.label_board)

        self.label_ether = QLabel(self.frame_model)
        self.label_ether.setObjectName(u"label_ether")
        self.label_ether.setFont(font2)

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.label_ether)

        self.label_zop = QLabel(self.frame_model)
        self.label_zop.setObjectName(u"label_zop")
        self.label_zop.setFont(font2)

        self.formLayout_5.setWidget(3, QFormLayout.LabelRole, self.label_zop)

        self.box_zop = QComboBox(self.frame_model)
        self.box_zop.addItem(u"")
        self.box_zop.addItem(u"Z1")
        self.box_zop.addItem(u"Z2")
        self.box_zop.addItem(u"Z3")
        self.box_zop.addItem(u"Z4")
        self.box_zop.addItem(u"Z5")
        self.box_zop.addItem(u"Z6")
        self.box_zop.addItem(u"Z7")
        self.box_zop.addItem(u"Z8")
        self.box_zop.addItem(u"Z9")
        self.box_zop.addItem(u"Z10")
        self.box_zop.setObjectName(u"box_zop")
        self.box_zop.setFont(font3)

        self.formLayout_5.setWidget(3, QFormLayout.FieldRole, self.box_zop)

        self.frame_board = QFrame(self.frame_model)
        self.frame_board.setObjectName(u"frame_board")
        self.frame_board.setFrameShape(QFrame.StyledPanel)
        self.frame_board.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_board)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.radio_10 = QRadioButton(self.frame_board)
        self.radio_10.setObjectName(u"radio_10")
        self.radio_10.setText(u"10")
        self.radio_10.setChecked(True)

        self.horizontalLayout_8.addWidget(self.radio_10, 0, Qt.AlignHCenter)

        self.radio_20 = QRadioButton(self.frame_board)
        self.radio_20.setObjectName(u"radio_20")
        self.radio_20.setText(u"20")

        self.horizontalLayout_8.addWidget(self.radio_20, 0, Qt.AlignHCenter)

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.frame_board)

        self.frame_ethernet = QFrame(self.frame_model)
        self.frame_ethernet.setObjectName(u"frame_ethernet")
        self.frame_ethernet.setFrameShape(QFrame.StyledPanel)
        self.frame_ethernet.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_ethernet)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(93, -1, -1, -1)
        self.checkBox = QCheckBox(self.frame_ethernet)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setText(u"ET")

        self.gridLayout_13.addWidget(self.checkBox, 0, 0, 1, 1)

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.frame_ethernet)

        self.frame_logo = QFrame(self.frame_select_model)
        self.frame_logo.setObjectName(u"frame_logo")
        self.frame_logo.setGeometry(QRect(350, 60, 491, 91))
        self.frame_logo.setStyleSheet(u"image: url(:/images/images/image001.png);")
        self.frame_logo.setFrameShape(QFrame.NoFrame)
        self.frame_logo.setFrameShadow(QFrame.Raised)

        self.gridLayout_6.addWidget(self.frame_select_model, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stackedWidget.addWidget(self.page_select)
        self.page_main = QWidget()
        self.page_main.setObjectName(u"page_main")
        sizePolicy3.setHeightForWidth(self.page_main.sizePolicy().hasHeightForWidth())
        self.page_main.setSizePolicy(sizePolicy3)
        self.page_main.setMinimumSize(QSize(1163, 586))
        self.page_main.setStyleSheet(u"")
        self.gridLayout_7 = QGridLayout(self.page_main)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_main_page = QFrame(self.page_main)
        self.frame_main_page.setObjectName(u"frame_main_page")
        sizePolicy3.setHeightForWidth(self.frame_main_page.sizePolicy().hasHeightForWidth())
        self.frame_main_page.setSizePolicy(sizePolicy3)
        self.frame_main_page.setFrameShape(QFrame.NoFrame)
        self.frame_main_page.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_main_page)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_toolbar = QFrame(self.frame_main_page)
        self.frame_toolbar.setObjectName(u"frame_toolbar")
        self.frame_toolbar.setMaximumSize(QSize(16777215, 30))
        self.frame_toolbar.setFrameShape(QFrame.StyledPanel)
        self.frame_toolbar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_toolbar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.toolBar = QToolBar(self.frame_toolbar)
        self.toolBar.setObjectName(u"toolBar")

        self.horizontalLayout_5.addWidget(self.toolBar)

        self.verticalLayout_5.addWidget(self.frame_toolbar)

        self.frame_container = QFrame(self.frame_main_page)
        self.frame_container.setObjectName(u"frame_container")
        sizePolicy3.setHeightForWidth(self.frame_container.sizePolicy().hasHeightForWidth())
        self.frame_container.setSizePolicy(sizePolicy3)
        self.frame_container.setFrameShape(QFrame.NoFrame)
        self.frame_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_container)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(10, 10, 10, 10)
        self.splitter = QSplitter(self.frame_container)
        self.splitter.setObjectName(u"splitter")
        sizePolicy3.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy3)
        self.splitter.setOrientation(Qt.Horizontal)
        self.frame_file_window = QFrame(self.splitter)
        self.frame_file_window.setObjectName(u"frame_file_window")
        self.frame_file_window.setMaximumSize(QSize(16777215, 16777215))
        self.frame_file_window.setFrameShape(QFrame.Box)
        self.frame_file_window.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_file_window)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.frame_file_window)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"QTabWidget::pane { /* The tab widget frame */\n"
"    border-top: 2px solid #C2C7CB;\n"
"    position: absolute;\n"
"    top: -0.5em;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    alignment: center;\n"
"}\n"
"\n"
"/* Style the tab using the tab sub-control. Note that\n"
"    it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"    color: rgb(255, 255, 255);\n"
"	background-color: rgb(69, 123, 157);\n"
"    border: 2px solid #C4C4C3;\n"
"    border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    min-width: 8ex;\n"
"    padding: 2px;\n"
"	width: 80px;\n"
"	height: 25px;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"	font: 75 10pt \"Arial\";\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(241, 250, 238);\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-color: #9B9B9B;\n"
"    border-bottom-color: #C2C7CB; /* same as pane color */\n"
"}")
        self.tabWidget.setTabsClosable(False)
        self.tab_user = QWidget()
        self.tab_user.setObjectName(u"tab_user")
        self.gridLayout_10 = QGridLayout(self.tab_user)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setHorizontalSpacing(0)
        self.gridLayout_10.setContentsMargins(1, 0, 0, 0)
        self.user_tree = QTreeView(self.tab_user)
        self.user_tree.setObjectName(u"user_tree")
        self.user_tree.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.user_tree.header().setVisible(False)

        self.gridLayout_10.addWidget(self.user_tree, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_user, "")
        self.tab_admin = QWidget()
        self.tab_admin.setObjectName(u"tab_admin")
        self.gridLayout_11 = QGridLayout(self.tab_admin)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setHorizontalSpacing(0)
        self.gridLayout_11.setContentsMargins(1, 0, 0, 0)
        self.admin_tree = QTreeView(self.tab_admin)
        self.admin_tree.setObjectName(u"admin_tree")
        self.admin_tree.header().setVisible(False)

        self.gridLayout_11.addWidget(self.admin_tree, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_admin, "")

        self.horizontalLayout_9.addWidget(self.tabWidget)

        self.splitter.addWidget(self.frame_file_window)
        self.widget_setvalue = QWidget(self.splitter)
        self.widget_setvalue.setObjectName(u"widget_setvalue")
        self.gridLayout_4 = QGridLayout(self.widget_setvalue)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_2 = QStackedWidget(self.widget_setvalue)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setMinimumSize(QSize(827, 0))
        self.stackedWidget_2.setFrameShape(QFrame.StyledPanel)
        self.default = QWidget()
        self.default.setObjectName(u"default")
        self.gridLayout_8 = QGridLayout(self.default)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_2.addWidget(self.default)
        self.page_ptn = QWidget()
        self.page_ptn.setObjectName(u"page_ptn")
        sizePolicy3.setHeightForWidth(self.page_ptn.sizePolicy().hasHeightForWidth())
        self.page_ptn.setSizePolicy(sizePolicy3)
        self.page_ptn.setMinimumSize(QSize(827, 0))
        self.gridLayout_9 = QGridLayout(self.page_ptn)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.page_ptn)
        self.frame.setObjectName(u"frame")
        sizePolicy4.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy4)
        self.frame.setMinimumSize(QSize(827, 0))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.table_pt_set = QTableWidget(self.frame)
        self.table_pt_set.setObjectName(u"table_pt_set")
        sizePolicy7 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.table_pt_set.sizePolicy().hasHeightForWidth())
        self.table_pt_set.setSizePolicy(sizePolicy7)
        self.table_pt_set.setFrameShape(QFrame.NoFrame)
        self.table_pt_set.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)

        self.gridLayout_2.addWidget(self.table_pt_set, 2, 0, 1, 1)

        self.frame_set_ptn = QFrame(self.frame)
        self.frame_set_ptn.setObjectName(u"frame_set_ptn")
        sizePolicy8 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.frame_set_ptn.sizePolicy().hasHeightForWidth())
        self.frame_set_ptn.setSizePolicy(sizePolicy8)
        self.frame_set_ptn.setMaximumSize(QSize(16777215, 60))
        self.frame_set_ptn.setFrameShape(QFrame.NoFrame)
        self.frame_set_ptn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_set_ptn)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 10, 0, 10)
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_pt_no = QLabel(self.frame_set_ptn)
        self.label_pt_no.setObjectName(u"label_pt_no")
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_pt_no.setFont(font4)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_pt_no)

        self.lineEdit_pt_no = QLineEdit(self.frame_set_ptn)
        self.lineEdit_pt_no.setObjectName(u"lineEdit_pt_no")
        self.lineEdit_pt_no.setMaximumSize(QSize(100, 16777215))

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lineEdit_pt_no)

        self.horizontalLayout_7.addLayout(self.formLayout_2)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_start_code = QLabel(self.frame_set_ptn)
        self.label_start_code.setObjectName(u"label_start_code")
        self.label_start_code.setFont(font4)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_start_code)

        self.box_start_code = QComboBox(self.frame_set_ptn)
        self.box_start_code.addItem("")
        self.box_start_code.addItem("")
        self.box_start_code.addItem("")
        self.box_start_code.setObjectName(u"box_start_code")
        sizePolicy2.setHeightForWidth(self.box_start_code.sizePolicy().hasHeightForWidth())
        self.box_start_code.setSizePolicy(sizePolicy2)
        self.box_start_code.setMaximumSize(QSize(100, 30))
        self.box_start_code.setStyleSheet(u"QComboBox{\n"
"	width: 30px;\n"
"	heigth: 20px;\n"
"}")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.box_start_code)

        self.horizontalLayout_7.addLayout(self.formLayout_3)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_ssp = QLabel(self.frame_set_ptn)
        self.label_ssp.setObjectName(u"label_ssp")
        self.label_ssp.setFont(font4)

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_ssp)

        self.lineEdit_ssp = QLineEdit(self.frame_set_ptn)
        self.lineEdit_ssp.setObjectName(u"lineEdit_ssp")
        self.lineEdit_ssp.setMaximumSize(QSize(100, 16777215))
        self.lineEdit_ssp.setMaxLength(6)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.lineEdit_ssp)

        self.horizontalLayout_7.addLayout(self.formLayout_4)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)

        self.btn_pt_move = QPushButton(self.frame_set_ptn)
        self.btn_pt_move.setObjectName(u"btn_pt_move")
        self.btn_pt_move.setMaximumSize(QSize(16777215, 40))
        self.btn_pt_move.setFont(font4)
        self.btn_pt_move.setStyleSheet(u"background-color: rgb(69, 123, 157);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_7.addWidget(self.btn_pt_move)

        self.gridLayout_2.addWidget(self.frame_set_ptn, 1, 0, 1, 1)

        self.label_ptn_title = QLabel(self.frame)
        self.label_ptn_title.setObjectName(u"label_ptn_title")
        self.label_ptn_title.setMaximumSize(QSize(16777215, 30))
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_ptn_title.setFont(font5)

        self.gridLayout_2.addWidget(self.label_ptn_title, 0, 0, 1, 1)

        self.gridLayout_9.addWidget(self.frame, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.page_ptn)
        self.page_table = QWidget()
        self.page_table.setObjectName(u"page_table")
        self.gridLayout_12 = QGridLayout(self.page_table)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(10, 0, 10, 10)
        self.label_table_title = QLabel(self.page_table)
        self.label_table_title.setObjectName(u"label_table_title")
        self.label_table_title.setFont(font5)
        self.label_table_title.setMargin(10)

        self.gridLayout_12.addWidget(self.label_table_title, 0, 0, 1, 1)

        self.tableWidget = QTableWidget(self.page_table)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setFrameShape(QFrame.NoFrame)

        self.gridLayout_12.addWidget(self.tableWidget, 1, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.page_table)
        self.page_tab = QWidget()
        self.page_tab.setObjectName(u"page_tab")
        self.verticalLayout = QVBoxLayout(self.page_tab)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_tab_title = QLabel(self.page_tab)
        self.label_tab_title.setObjectName(u"label_tab_title")
        self.label_tab_title.setFont(font5)
        self.label_tab_title.setMargin(10)

        self.verticalLayout.addWidget(self.label_tab_title)

        self.tab_param = QTabWidget(self.page_tab)
        self.tab_param.setObjectName(u"tab_param")

        self.verticalLayout.addWidget(self.tab_param)

        self.stackedWidget_2.addWidget(self.page_tab)

        self.gridLayout_4.addWidget(self.stackedWidget_2, 0, 0, 1, 1)

        self.splitter.addWidget(self.widget_setvalue)

        self.horizontalLayout_6.addWidget(self.splitter)

        self.verticalLayout_5.addWidget(self.frame_container)

        self.gridLayout_7.addWidget(self.frame_main_page, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_main)

        self.gridLayout_5.addWidget(self.stackedWidget, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.widget_content)

        self.verticalLayout_2.addWidget(self.frame_content)

        self.gridLayout_3.addWidget(self.frame_main, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuMode_2.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuCommunication.menuAction())
        self.menubar.addAction(self.menuOperation.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionopen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionSave_as_CSV)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPrint)
        self.menuEdit.addAction(self.actionFind)
        self.menuView.addAction(self.actionTool)
        self.menuView.addAction(self.actionCategory)
        self.menuView.addSeparator()
        self.menuView.addAction(self.menuLanguage.menuAction())
        self.menuLanguage.addAction(self.actionKorean)
        self.menuLanguage.addAction(self.actionEnglish)
        self.menuCommunication.addAction(self.actionUpload_All)
        self.menuCommunication.addAction(self.actionUpload_Pattern)
        self.menuCommunication.addSeparator()
        self.menuCommunication.addAction(self.actionDownload_All)
        self.menuCommunication.addAction(self.actionDownload_Pattern)
        self.menuCommunication.addSeparator()
        self.menuCommunication.addAction(self.actionCompare_File)
        self.menuOperation.addAction(self.actionInitialize_to_Factory_Default)
        self.menuOperation.addAction(self.actionInitialize_to_User_Default)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionHelp)
        self.menuMode_2.addAction(self.actionUser)
        self.menuMode_2.addAction(self.actionAdmin)
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionopen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionSave_as_CSV)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionUpload_All)
        self.toolBar.addAction(self.actionDownload_All)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionFind)
        self.toolBar.addAction(self.actionKorean)
        self.toolBar.addAction(self.actionPrint)
        self.toolBar.addAction(self.actionHelp)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionopen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionSave_As.setText(QCoreApplication.translate("MainWindow", u"Save As", None))
        self.actionSave_as_CSV.setText(QCoreApplication.translate("MainWindow", u"Save as CSV", None))
        self.actionPrint.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.actionFind.setText(QCoreApplication.translate("MainWindow", u"Find", None))
        self.actionTool.setText(QCoreApplication.translate("MainWindow", u"Tool", None))
        self.actionCategory.setText(QCoreApplication.translate("MainWindow", u"Category", None))
        self.actionKorean.setText(QCoreApplication.translate("MainWindow", u"Korean", None))
        self.actionEnglish.setText(QCoreApplication.translate("MainWindow", u"English", None))
        self.actionUpload_All.setText(QCoreApplication.translate("MainWindow", u"Upload All", None))
        self.actionUpload_Pattern.setText(QCoreApplication.translate("MainWindow", u"Upload Pattern", None))
        self.actionDownload_All.setText(QCoreApplication.translate("MainWindow", u"Download All", None))
        self.actionDownload_Pattern.setText(QCoreApplication.translate("MainWindow", u"Download Pattern", None))
        self.actionCompare_File.setText(QCoreApplication.translate("MainWindow", u"Compare File", None))
        self.actionInitialize_to_Factory_Default.setText(QCoreApplication.translate("MainWindow", u"Initialize to Factory Default", None))
        self.actionInitialize_to_User_Default.setText(QCoreApplication.translate("MainWindow", u"Initialize to User Default", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.actionUser.setText(QCoreApplication.translate("MainWindow", u"User", None))
        self.actionAdmin.setText(QCoreApplication.translate("MainWindow", u"Admin", None))
        self.label_app_title.setText(QCoreApplication.translate("MainWindow", u"NEX Parameter", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuLanguage.setTitle(QCoreApplication.translate("MainWindow", u"Language", None))
        self.menuCommunication.setTitle(QCoreApplication.translate("MainWindow", u"Communication", None))
        self.menuOperation.setTitle(QCoreApplication.translate("MainWindow", u"Operation", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuMode_2.setTitle(QCoreApplication.translate("MainWindow", u"Mode", None))
        self.btn_user.setText(QCoreApplication.translate("MainWindow", u"USER", None))
        self.btn_admin.setText(QCoreApplication.translate("MainWindow", u"ADMIN", None))
        self.label_model.setText(QCoreApplication.translate("MainWindow", u"Model", None))
        self.label_board.setText(QCoreApplication.translate("MainWindow", u"Board", None))
        self.label_ether.setText(QCoreApplication.translate("MainWindow", u"Ethernet", None))
        self.label_zop.setText(QCoreApplication.translate("MainWindow", u"Z-Option", None))

        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_user), QCoreApplication.translate("MainWindow", u"Pattern", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_admin), QCoreApplication.translate("MainWindow", u"Parameter", None))
        self.label_pt_no.setText(QCoreApplication.translate("MainWindow", u"Pattern No.", None))
        self.label_start_code.setText(QCoreApplication.translate("MainWindow", u"Start Code", None))
        self.box_start_code.setItemText(0, QCoreApplication.translate("MainWindow", u"TPV", None))
        self.box_start_code.setItemText(1, QCoreApplication.translate("MainWindow", u"SPV", None))
        self.box_start_code.setItemText(2, QCoreApplication.translate("MainWindow", u"SSP", None))

        self.label_ssp.setText(QCoreApplication.translate("MainWindow", u"SSP", None))
        self.btn_pt_move.setText(QCoreApplication.translate("MainWindow", u"APPLY", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Min.", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Max.", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Set Value", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Unit", None));\
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'passwordofXlXj.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(540, 270)
        Dialog.setModal(True)
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_input_pw = QFrame(Dialog)
        self.frame_input_pw.setObjectName(u"frame_input_pw")
        self.frame_input_pw.setFrameShape(QFrame.NoFrame)
        self.frame_input_pw.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_input_pw)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_input_pw)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMaximumSize(QSize(16777215, 35))
        self.frame_top.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(29, 53, 87);\n"
"}")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_topbar = QFrame(self.frame_top)
        self.frame_topbar.setObjectName(u"frame_topbar")
        self.frame_topbar.setFrameShape(QFrame.NoFrame)
        self.frame_topbar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_topbar)

        self.frame_top_btn = QFrame(self.frame_top)
        self.frame_top_btn.setObjectName(u"frame_top_btn")
        self.frame_top_btn.setMaximumSize(QSize(35, 35))
        self.frame_top_btn.setFrameShape(QFrame.NoFrame)
        self.frame_top_btn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top_btn)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_close = QPushButton(self.frame_top_btn)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy)
        self.btn_close.setMaximumSize(QSize(35, 35))
        self.btn_close.setStyleSheet(u"QPushButton{\n"
"	image: url(:/icons/images/icons/icon_close.png);\n"
"	background-color: rgb(29, 53, 87);\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_close)

        self.horizontalLayout_2.addWidget(self.frame_top_btn)

        self.verticalLayout.addWidget(self.frame_top)

        self.frame_content = QFrame(self.frame_input_pw)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(237, 242, 244);\n"
"}")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.lineEdit = QLineEdit(self.frame_content)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(160, 85, 200, 40))
        self.lineEdit.setMaxLength(12)
        self.lineEdit.setEchoMode(QLineEdit.Password)
        self.label = QLabel(self.frame_content)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 40, 300, 25))
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.btn_enter = QPushButton(self.frame_content)
        self.btn_enter.setObjectName(u"btn_enter")
        self.btn_enter.setGeometry(QRect(225, 147, 70, 35))

        self.verticalLayout.addWidget(self.frame_content)

        self.horizontalLayout.addWidget(self.frame_input_pw)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        self.label.setText(QCoreApplication.translate("Dialog", u"Enter admin mode password", None))
        self.btn_enter.setText(QCoreApplication.translate("Dialog", u"ENTER", None))
    # retranslateUi