import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# SPLASH SCREEN
import function_all
from connDB import getLang

import function_1100
from ui_main_window import Ui_MainWindow, Ui_Dialog
from ui_splash_login import Ui_splashLogin
from ui_splash_screen import Ui_SplashScreen

# GLOBALS
counter = 0
jumper = 10
GLOBAL_STATE = False
for_tree = False
for_tool = False


## ==> APPLICATION WINDOW
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.translator = QtCore.QTranslator(self)

        function_all.setStart(self)

        ## ==> REMOVE STANDARD TITLE BAR
        self.setWindowFlags(Qt.FramelessWindowHint)  # Remove title bar
        self.setAttribute(Qt.WA_TranslucentBackground)  # Set background to transparent
        # SET DROPSHADOW WINDOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        # APPLY DROPSHADOW TO FRAME
        self.ui.frame_main.setGraphicsEffect(self.shadow)
        # MAXIMIZE / RESTORE
        self.ui.btn_maximize.clicked.connect(lambda: self.maximize_restore())
        # MINIMIZE
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())
        # CLOSE
        self.ui.btn_close.clicked.connect(lambda: self.close())

        # MENUBAR
        self.ui.actionNew.triggered.connect(self.goSelect)
        self.ui.actionopen.triggered.connect(self.openFile)
        self.ui.actionCategory.triggered.connect(self.openTree)
        self.ui.actionTool.triggered.connect(self.openTool)
        self.ui.actionUser.triggered.connect(self.userMode)
        self.ui.actionAdmin.triggered.connect(self.adminMode)
        self.ui.actionKorean.triggered.connect(lambda index: function_1100.changeLang(self, 'kor', index))
        self.ui.actionEnglish.triggered.connect(lambda index: function_1100.changeLang(self, 'eng', index))

        # FIRST PAGE
        self.ui.btn_user.clicked.connect(self.userMode)
        self.ui.btn_admin.clicked.connect(self.adminMode)

        # CHANGE SENSOR EVENT
        # self.mod.currentIndexChanged.connect(lambda: function_1100.sensorType(self))

        ## PATTERN EDIT SSP
        self.ui.box_start_code.currentIndexChanged.connect(self.changeStartCode)

        ## BTN EVENT
        self.ui.user_tree.doubleClicked.connect(self.userClick)
        self.ui.admin_tree.doubleClicked.connect(self.adminClick)

        ## WINDOW MOVE
        def moveWindow(event):
            # IF LEFT CLICK MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.frame_title_bar.mouseMoveEvent = moveWindow

    ## APP EVENTS
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    ## ==> MAXIMIZE RESTORE FUNCTION
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE

        # IF NOT MAXIMIZED
        if status == False:
            self.showMaximized()
            # SET GLOBAL TO 1
            GLOBAL_STATE = True
            self.ui.btn_maximize.setToolTip("Restore")
            width = self.ui.widget_content.width()
            height = self.ui.widget_content.height()
            print(str(width)+" X "+ str(height))

            # self.ui.page_main.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.ui.page_main.resize(QSize(width, height))
            self.ui.page_select.resize(QSize(width, height))
            print(self.ui.page_main.size())
            self.ui.stackedWidget.setFixedSize(QSize(width, height))
            print(self.ui.stackedWidget.size())
            # self.ui.stackedWidget_2.resize()
        else:
            GLOBAL_STATE = False
            self.showNormal()
            self.resize(self.width() + 1, self.height() + 1)
            self.ui.btn_maximize.setToolTip("Maximize")

            self.ui.stackedWidget.setFixedSize(QSize(1163, 586))
            print(self.ui.stackedWidget.size())

    def setStatus(self, status):
        global GLOBAL_STATE
        GLOBAL_STATE = status

    ## INITIALIZE START
    # def setStart(self):

    ## SET FIRST PAGE
    def goSelect(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_main)

    ## FILE OPEN
    def openFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open', '', 'All Files(*);;Database (*.db)')

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)
        else:
            pass

    ## TOOLBAR ACTION
    def openTool(self):
        global for_tool
        tool = for_tool

        if tool == False:
            self.ui.frame_toolbar.hide()
            for_tool = True
        else:
            for_tool = False
            self.ui.frame_toolbar.show()

    ## CATEGORY ACTION
    def openTree(self):
        global for_tree
        tree = for_tree

        if tree == False:
            self.ui.frame_file_window.hide()
            for_tree = True
        else:
            for_tree = False
            self.ui.frame_file_window.show()

    ## ==> SELECT USER/ADMIN MODE
    ############################################################################
    ## USER MODE CLICK EVENT
    def userMode(self):
        global nex
        nex = self.ui.box_model.currentText()
        global lang
        lang = getLang()
        if nex == 'NEX1100':
            function_1100.userModel(self, lang)
        self.ui.label_app_title.setText("NEX Parameter - " + nex)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_main)
        self.ui.tabWidget.setTabVisible(1, False)

    ## ADMIN MODE CLICK EVENT
    def adminMode(self):
        global nex
        nex = self.ui.box_model.currentText()
        global lang
        lang = getLang()
        self.form = PassWindow()
        self.form.show()
        r = self.form.exec_()
        if r:
            self.ui.tabWidget.setTabVisible(1, True)
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_main)
            self.ui.label_app_title.setText("NEX Parameter - " + nex)
            if nex == 'NEX1100':
                function_1100.userModel(self, lang)
                function_1100.adminModel(self, lang)

    ## ==> TREE ITEM CLICK EVENT
    ############################################################################
    ## USER TREE CLICK EVENT
    def userClick(self, QModelIndex):
        global index
        global nex
        item = self.user.itemData(QModelIndex)
        index = item[256]
        lang = getLang()
        self.nex = nex
        if self.nex == 'NEX1100':
            function_1100.userItem(self, lang, index)
        else:
            pass

    ## ADMIN TREE CLICK EVENT
    def adminClick(self, QModelIndex):
        global index
        global nex
        item = self.admin.itemData(QModelIndex)
        index = item[256]
        lang = getLang()
        self.nex = nex
        if self.nex == 'NEX1100':
            function_1100.adminItem(self, lang, index)
        else:
            pass

    def changeStartCode(self):
        if self.ui.box_start_code.currentText() == 'TPV':
            self.ui.label_ssp.hide()
            self.ui.lineEdit_ssp.hide()
        else:
            self.ui.label_ssp.show()
            self.ui.lineEdit_ssp.show()

    def changeEvent(self, event):
        if event.type() == QtCore.QEvent.LanguageChange:
            self.ui.retranslateUi(self)
        super(MainWindow, self).changeEvent(event)


## ==> PASSWORD WINDOW FOR ADMIN MODE
class PassWindow(QDialog):
    ok = Signal()

    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        ## ==> REMOVE STANDARD TITLE BAR
        self.setWindowFlags(Qt.FramelessWindowHint)  # Remove title bar
        self.setAttribute(Qt.WA_TranslucentBackground)  # Set background to transparent
        # SET DROPSHADOW WINDOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        # APPLY DROPSHADOW TO FRAME
        self.ui.frame_input_pw.setGraphicsEffect(self.shadow)

        ## CLOSE FORM
        self.ui.btn_close.clicked.connect(self.close)

        self.ui.btn_enter.clicked.connect(self.onOk)
        self.ui.lineEdit.returnPressed.connect(self.onOk)

    ## FOR CHANGE LANGUAGE
    def changeEvent(self, event):
        if event.type() == QtCore.QEvent.LanguageChange:
            self.ui.retranslateUi(self)
        super(PassWindow, self).changeEvent(event)

    ## OK BTN CLICK EVENT
    def onOk(self):
        if self.ui.lineEdit.text() == '0000' or self.ui.lineEdit.text() == '0205':
            self.ok.emit()
            self.accept()
        else:
            QMessageBox.critical(self, "Password Error", "Incorrect Password")
            self.ui.lineEdit.setFocus()


## ==> SELECT WINDOW
class SplashLogin(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_splashLogin()
        self.ui.setupUi(self)

        ## ==> REMOVE STANDARD TITLE BAR
        self.setWindowFlags(Qt.FramelessWindowHint)  # Remove title bar
        self.setAttribute(Qt.WA_TranslucentBackground)  # Set background to transparent
        # CLOSE
        self.ui.exitBtn.clicked.connect(lambda: self.close())

        ## ==> MAIN WINDOW
        self.ui.newBtn.clicked.connect(self.goMain)

    def goMain(self):
        ## GO MAINWINDOW
        self.main = MainWindow()
        self.main.show()
        ## CLOSE SELECT WINDOW
        self.close()


## ==> SPLASHSCREEN WINDOW
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## ==> SET INITIAL PROGRESS BAR TO (0) ZERO
        self.progressBarValue(0)

        ## ==> REMOVE STANDARD TITLE BAR
        self.setWindowFlags(Qt.FramelessWindowHint) # Remove title bar
        self.setAttribute(Qt.WA_TranslucentBackground) # Set background to transparent

        ## ==> APPLY DROP SHADOW SHEET
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 120))
        self.ui.circularBg.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(15)

        ## SHOW ==> MAINWINDOW
        ################################################################################
        self.show()
        ## ==> END ##

    ## DEF TO LOADING
    ################################################################################
    def progress(self):
        global counter
        global jumper
        value = counter

        # HTML TEXT PERCENTAGE
        htmlText = """<p><span style=" font-size:58pt;">{VALUE}</span><span style=" font-size:48pt; vertical-align:super;">%</span></p>"""

        # REPLACE VALUE
        newHtml = htmlText.replace("{VALUE}", str(jumper))

        if (value > jumper):
            # APPLY NEW PERCENTAGE TEXT
            self.ui.labelPercentage.setText(newHtml)
            jumper += 10

        # SET VALUE TO PROGRESS BAR
        # fix max value error if > than 100
        if value >= 100: value = 1.000
        self.progressBarValue(value)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.login = SplashLogin()
            self.login.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1

    ## DEF PROGRESSBAR VALUE
    ################################################################################
    def progressBarValue(self, value):

        # PROGRESSBAR STYLESHEET BASE
        styleSheet = """
        QFrame{
            border-radius: 150px;
            background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} rgba(168, 218, 220, 255));
        }
        """

        # GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
        # stop works of 1.000 to 0.000
        progress = (100 - value) / 100.0

        # GET NEW VALUES
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        # FIX MAX VALUE
        if value == 100:
            stop_1 = "1.000"
            stop_2 = "1.000"

        # SET VALUES TO NEW STYLESHEET
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

        # APPLY STYLESHEET WITH NEW VALUES
        self.ui.circularProgress.setStyleSheet(newStylesheet)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())