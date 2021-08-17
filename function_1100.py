import datetime
from collections import deque

from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import Qt, QTime
from PySide2.QtGui import QStandardItemModel, QStandardItem
from PySide2.QtWidgets import QTableWidgetItem, QComboBox, QGridLayout, QTableWidget, QDateTimeEdit, QLineEdit

from conn1100 import userTree, adminTree, setVar, getTitle, getTable, eu1, eus1
from connDB import itemBox, typeBox, listIdx, getLang, setLang

# VARIABLE OF SP
nex1100 = dict()
datas = setVar()
for data in datas:
    key1 = data[1]
    key2 = data[2]
    value = data[9]
    if key1 not in nex1100:
        nex1100[key1] = {}
    if key2 not in nex1100[key1]:
        nex1100[key1][key2] = value

# VARIABLE OF MIN/MAX
limit1100= dict()
eu1 = eu1(0)
for eu in eu1:
    key = eu[0]
    min = eu[1]
    max = eu[2]
    if key not in limit1100:
        limit1100[key] = {}
        limit1100[key]['min'] = min
        limit1100[key]['max'] = max


# USER MODE TREE
def userModel(self, lang):
    self.user = QStandardItemModel()
    self.ui.user_tree.setModel(self.user)
    self.user.setRowCount(0)
    values = deque(userTree())
    root = None
    seen = {}
    if root is None:
        root = self.user.invisibleRootItem()
    while values:
        value = values.popleft()
        if value[4] == 0:
            parent = root
        else:
            pid = value[1]
            if pid not in seen:
                values.append(value)
                continue
            parent = seen[pid]
        dbid = value[0]
        if lang == 'kor':
            usertxt = QStandardItem(value[2])
        else:
            usertxt = QStandardItem(value[3])
        usertxt.setData(dbid, Qt.UserRole)
        usertxt.setEditable(False)
        parent.appendRow(usertxt)
        seen[dbid] = parent.child(parent.rowCount() - 1)


# ADMIN MODE TREE
def adminModel(self, lang):
    self.admin = QStandardItemModel()
    self.ui.admin_tree.setModel(self.admin)
    self.admin.setRowCount(0)
    values = deque(adminTree())
    root = None
    seen = {}
    if root is None:
        root = self.admin.invisibleRootItem()
    while values:
        value = values.popleft()
        if value[4] == 0:
            parent = root
        else:
            pid = value[1]
            if pid not in seen:
                values.append(value)
                continue
            parent = seen[pid]
        dbid = value[0]
        if lang == 'kor':
            admintxt = QStandardItem(value[2])
        else:
            admintxt = QStandardItem(value[3])
        admintxt.setData(dbid, Qt.UserRole)
        admintxt.setEditable(False)
        parent.appendRow(admintxt)
        seen[dbid] = parent.child(parent.rowCount() - 1)


# USER MODE TABLE
def userItem(self, lang, index):
    # 하위트리 존재 상위 인덱스 목록
    idx = [102, 108, 110, 111, 113]
    if index in idx:
        pass
    # 패턴편집
    elif index == 114 or index == 115:
        if index == 114:
            if lang == 'kor':
                self.ui.label_ptn_title.setText("패턴편집 - CH1")
            else:
                self.ui.label_ptn_title.setText("Pattern Edit - CH1")
        else:
            if lang == 'kor':
                self.ui.label_ptn_title.setText("패턴편집 - CH2")
            else:
                self.ui.label_ptn_title.setText("Pattern Edit - CH2")
        if self.ui.box_start_code.currentText() == 'TPV':
            self.ui.label_ssp.hide()
            self.ui.lineEdit_ssp.hide()
        else:
            self.ui.label_ssp.show()
            self.ui.lineEdit_ssp.show()
        self.tableWidget = self.ui.table_pt_set
        if lang == 'kor':
            if (self.tableWidget.columnCount() < 100):
                self.tableWidget.setColumnCount(100)
            for i in range(100):
                globals()['tableitem{}'.format(i)] = QTableWidgetItem("세그먼트" + str(i + 1))
                self.tableWidget.setHorizontalHeaderItem(i, globals()['tableitem{}'.format(i)])
            if (self.tableWidget.rowCount() < 19):
                self.tableWidget.setRowCount(19)
            tablever = QTableWidgetItem("목표 SP")
            self.tableWidget.setVerticalHeaderItem(0, tablever)
            tablever1 = QTableWidgetItem("시간 (H.M.S)")
            self.tableWidget.setVerticalHeaderItem(1, tablever1)
            for i in range(2, 14):
                globals()['tablever{}'.format(i)] = QTableWidgetItem("타임시그널" + str(i - 1))
                self.tableWidget.setVerticalHeaderItem(i, globals()['tablever{}'.format(i)])
            for i in range(14, 18):
                globals()['tablever{}'.format(i)] = QTableWidgetItem("세그경보" + str(i - 13))
                self.tableWidget.setVerticalHeaderItem(i, globals()['tablever{}'.format(i)])
            tablever18 = QTableWidgetItem("대기동작")
            self.tableWidget.setVerticalHeaderItem(18, tablever18)
        else:
            if (self.tableWidget.columnCount() < 100):
                self.tableWidget.setColumnCount(100)
            for i in range(100):
                globals()['tableitem{}'.format(i)] = QTableWidgetItem("Segment" + str(i + 1))
                self.tableWidget.setHorizontalHeaderItem(i, globals()['tableitem{}'.format(i)])
            if (self.tableWidget.rowCount() < 19):
                self.tableWidget.setRowCount(19)
            tablever = QTableWidgetItem("Target SP")
            self.tableWidget.setVerticalHeaderItem(0, tablever)
            tablever1 = QTableWidgetItem("TIME (H.M.S)")
            self.tableWidget.setVerticalHeaderItem(1, tablever1)
            for i in range(2, 14):
                globals()['tablever{}'.format(i)] = QTableWidgetItem("Time Signal" + str(i - 1))
                self.tableWidget.setVerticalHeaderItem(i, globals()['tablever{}'.format(i)])
            for i in range(14, 18):
                globals()['tablever{}'.format(i)] = QTableWidgetItem("Seg Alarm" + str(i - 13))
                self.tableWidget.setVerticalHeaderItem(i, globals()['tablever{}'.format(i)])
            tablever18 = QTableWidgetItem("Wait")
            self.tableWidget.setVerticalHeaderItem(18, tablever18)

        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_ptn)
    # 파일편집
    else:
        titles = getTitle(index)
        if lang == 'kor':
            self.ui.label_table_title.setText(titles[0])
        else:
            self.ui.label_table_title.setText(titles[1])
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_table)
        values = getTable(index)
        row = 0
        self.ui.tableWidget.setRowCount(len(values))
        for value in values:
            self.ui.tableWidget.setVerticalHeaderItem(row, QTableWidgetItem(value[5]))
            self.ui.tableWidget.setCellWidget(row, 3, None)
            if lang == 'kor':
                self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(value[3]))
                self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(value[10]))
            else:
                self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(value[4]))
                self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(value[11]))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(value[6]))
            self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(value[7]))
            # 파일편집
            if index == 109:
                if row == 1:
                    # 복사원본패턴 채널
                    self.src = QComboBox()
                    self.src.addItems(itemBox(lang, 'SRC'))
                    self.src.setCurrentIndex(nex1100[value[1]][value[2]])
                    self.ui.tableWidget.setCellWidget(row, 3, self.src)
                elif row == 3 or row == 6:
                    # 복사대상패턴 및 삭제패턴 채널
                    self.dest = QComboBox()
                    self.dest.addItems(itemBox(lang, 'DEST'))
                    self.dest.setCurrentIndex(nex1100[value[1]][value[2]])
                    self.ui.tableWidget.setCellWidget(row, 3, self.dest)
                else:
                    self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(nex1100[value[1]][value[2]]))
            # 반복설정
            elif index == 116 or index == 117:
                if row == 3:
                    self.endact = QComboBox()
                    self.endact.addItems(itemBox(lang, 'endact'))
                    self.endact.setCurrentIndex(nex1100[value[1]][value[2]])
                    self.ui.tableWidget.setCellWidget(row, 3, self.endact)
                else:
                    self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(nex1100[value[1]][value[2]]))
            # 대기동작설정
            elif index == 118 or index == 119:
                if row == 0:
                    self.onbtn = QComboBox()
                    self.onbtn.addItems(itemBox(lang, 'ONBTN'))
                    self.onbtn.setCurrentIndex(nex1100[value[1]][value[2]])
                    self.ui.tableWidget.setCellWidget(row, 3, self.onbtn)
                elif row == 3:
                    self.wact = QComboBox()
                    self.wact.addItems(itemBox(lang, 'WACT'))
                    self.wact.setCurrentIndex(nex1100[value[1]][value[2]])
                    self.ui.tableWidget.setCellWidget(row, 3, self.wact)
                else:
                    self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(nex1100[value[1]][value[2]]))
            else:
                self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(nex1100[value[1]][value[2]]))
            row = row + 1


# AMDIN MODE TABLE
def adminItem(self, lang, index):
    indexes = (101,122,103,125,126,127,128,129,143,130,147,148,149,166,150,151,153,154,131,132,176,177,178,179,182,104,105,142,141)
    j = 0
    if index in indexes:
        pass
    # 경보시그널
    # elif index == 135 or index == 136:
    #     titles = getTitle(index)
    #     if lang == 'kor':
    #         self.ui.label_tab_title.setText(titles[0])
    #     else:
    #         self.ui.label_tab_title.setText(titles[1])
    #     self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_tab)
    #     self.ui.tab_param.clear()
    #     for i in range(1, 9):
    #         self.tableWidget = QTableWidget()
    #         if (self.tableWidget.columnCount() < 5):
    #             self.tableWidget.setColumnCount(5)
    #         __qtablewidgetitem = QTableWidgetItem("Name")
    #         self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
    #         __qtablewidgetitem1 = QTableWidgetItem("Min")
    #         self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
    #         __qtablewidgetitem2 = QTableWidgetItem("Max")
    #         self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
    #         __qtablewidgetitem3 = QTableWidgetItem("Set Value")
    #         self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
    #         __qtablewidgetitem4 = QTableWidgetItem("Unit")
    #         self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
    #         width = self.ui.tab_param.width() - 25
    #         header = self.tableWidget.horizontalHeader()
    #         self.tableWidget.setColumnWidth(0, width * 4 / 10)
    #         self.tableWidget.setColumnWidth(2, width * 1 / 10)
    #         self.tableWidget.setColumnWidth(3, width * 1 / 10)
    #         self.tableWidget.setColumnWidth(4, width * 3 / 10)
    #         self.tableWidget.setColumnWidth(5, width * 1 / 10)
    #         # self.tableWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
    #         al = 11
    #         sal = 10
    #         if i == 8:
    #             values = getTable(index)[(i-1)*al:(i-1)*al+10]
    #         elif
    #         else:
    #             values = getTable(index)[(i-1)*al:(i-1)*al+11]
    #         row = 0
    #         self.tableWidget.setRowCount(len(values))
    #         for value in values:
    #             self.tableWidget.setVerticalHeaderItem(row, QTableWidgetItem(value[5]))
    #             if lang == 'kor':
    #                 self.tableWidget.setItem(row, 0, QTableWidgetItem(value[3]))
    #                 self.tableWidget.setItem(row, 4, QTableWidgetItem(value[10]))
    #             else:
    #                 self.tableWidget.setItem(row, 0, QTableWidgetItem(value[4]))
    #                 self.tableWidget.setItem(row, 4, QTableWidgetItem(value[11]))
    #             self.tableWidget.setItem(row, 1, QTableWidgetItem(value[6]))
    #             self.tableWidget.setItem(row, 2, QTableWidgetItem(value[7]))
    #             self.tableWidget.setItem(row, 3, QTableWidgetItem(nex1100[value[1]][value[2]]))
    #             row = row + 1
    #         self.gridLayout = QGridLayout()
    #         self.gridLayout.setContentsMargins(2, 2, 2, 2)
    #         self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
    #         self.ui.tab_param.addTab(self.tableWidget, "ON/OFF Signal " + str(i))
    # 이너시그널
    elif index == 137 or index == 138:
        titles = getTitle(index)
        if lang == 'kor':
            self.ui.label_tab_title.setText(titles[0])
        else:
            self.ui.label_tab_title.setText(titles[1])
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_tab)
        self.ui.tab_param.clear()
        for i in range(1, 17):
            self.tableWidget = QTableWidget()
            if (self.tableWidget.columnCount() < 5):
                self.tableWidget.setColumnCount(5)
            __qtablewidgetitem = QTableWidgetItem("Name")
            self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
            __qtablewidgetitem1 = QTableWidgetItem("Min")
            self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
            __qtablewidgetitem2 = QTableWidgetItem("Max")
            self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
            __qtablewidgetitem3 = QTableWidgetItem("Set Value")
            self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
            __qtablewidgetitem4 = QTableWidgetItem("Unit")
            self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
            width = self.ui.tab_param.width()-25
            header = self.tableWidget.horizontalHeader()
            self.tableWidget.setColumnWidth(0, width * 4 / 10)
            self.tableWidget.setColumnWidth(2, width * 1 / 10)
            self.tableWidget.setColumnWidth(3, width * 1 / 10)
            self.tableWidget.setColumnWidth(4, width * 3 / 10)
            self.tableWidget.setColumnWidth(5, width * 1 / 10)
            # self.tableWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
            j = 5
            values = getTable(index)[(i-1)*j:(i-1)*j+5]
            row = 0
            self.tableWidget.setRowCount(len(values))
            for value in values:
                self.tableWidget.setVerticalHeaderItem(row, QTableWidgetItem(value[5]))
                if lang == 'kor':
                    self.tableWidget.setItem(row, 0, QTableWidgetItem(value[3]))
                    self.tableWidget.setItem(row, 4, QTableWidgetItem(value[10]))
                else:
                    self.tableWidget.setItem(row, 0, QTableWidgetItem(value[4]))
                    self.tableWidget.setItem(row, 4, QTableWidgetItem(value[11]))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(value[6]))
                self.tableWidget.setItem(row, 2, QTableWidgetItem(value[7]))
                if row ==  0:
                    self.isat = QComboBox()
                    self.isat.addItems(itemBox(lang, 'ISAT'))
                    self.isat.setCurrentIndex(nex1100[value[1]][value[2]])
                    self.ui.tableWidget.setCellWidget(row, 3, self.isat)
                elif row == 1:
                    self.isam = QComboBox()
                    self.isam.addItems(itemBox(lang, 'ISAM'))
                    self.isam.setCurrentIndex(nex1100[value[1]][value[2]])
                    self.ui.tableWidget.setCellWidget(row, 3, self.isam)
                else:
                    self.tableWidget.setItem(row, 3, QTableWidgetItem(nex1100[value[1]][value[2]]))
                row = row + 1
            self.gridLayout = QGridLayout()
            self.gridLayout.setContentsMargins(2, 2, 2, 2)
            self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
            self.ui.tab_param.addTab(self.tableWidget, "IS " + str(i))
    # ON/OFF 시그널
    elif index == 139 or index == 140:
        titles = getTitle(index)
        if lang == 'kor':
            self.ui.label_tab_title.setText(titles[0])
        else:
            self.ui.label_tab_title.setText(titles[1])
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_tab)
        self.ui.tab_param.clear()
        for i in range(1, 9):
            self.tableWidget = QTableWidget()
            if (self.tableWidget.columnCount() < 5):
                self.tableWidget.setColumnCount(5)
            __qtablewidgetitem = QTableWidgetItem("Name")
            self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
            __qtablewidgetitem1 = QTableWidgetItem("Min")
            self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
            __qtablewidgetitem2 = QTableWidgetItem("Max")
            self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
            __qtablewidgetitem3 = QTableWidgetItem("Set Value")
            self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
            __qtablewidgetitem4 = QTableWidgetItem("Unit")
            self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
            width = self.ui.tab_param.width() - 25
            header = self.tableWidget.horizontalHeader()
            self.tableWidget.setColumnWidth(0, width * 4 / 10)
            self.tableWidget.setColumnWidth(2, width * 1 / 10)
            self.tableWidget.setColumnWidth(3, width * 1 / 10)
            self.tableWidget.setColumnWidth(4, width * 3 / 10)
            self.tableWidget.setColumnWidth(5, width * 1 / 10)
            # self.tableWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
            j = 6
            if i == 8:
                values = getTable(index)[(i-1)*j:]
            else:
                values = getTable(index)[(i-1)*j:(i-1)*j + 6]
            row = 0
            self.tableWidget.setRowCount(len(values))
            for value in values:
                self.tableWidget.setVerticalHeaderItem(row, QTableWidgetItem(value[5]))
                if lang == 'kor':
                    self.tableWidget.setItem(row, 0, QTableWidgetItem(value[3]))
                    self.tableWidget.setItem(row, 4, QTableWidgetItem(value[10]))
                else:
                    self.tableWidget.setItem(row, 0, QTableWidgetItem(value[4]))
                    self.tableWidget.setItem(row, 4, QTableWidgetItem(value[11]))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(value[6]))
                self.tableWidget.setItem(row, 2, QTableWidgetItem(value[7]))
                self.tableWidget.setItem(row, 3, QTableWidgetItem(nex1100[value[1]][value[2]]))
                row = row + 1

            self.gridLayout = QGridLayout()
            self.gridLayout.setContentsMargins(2, 2, 2, 2)
            self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
            self.ui.tab_param.addTab(self.tableWidget, "ON/OFF Signal " + str(i))
    # PID
    elif index == 196 or index == 197:
        titles = getTitle(index)
        if lang == 'kor':
            self.ui.label_tab_title.setText(titles[0])
        else:
            self.ui.label_tab_title.setText(titles[1])
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_tab)
        self.ui.tab_param.clear()
        for i in range(1, 7):
            self.tableWidget = QTableWidget()
            if (self.tableWidget.columnCount() < 5):
                self.tableWidget.setColumnCount(5)
            __qtablewidgetitem = QTableWidgetItem("Name")
            self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
            __qtablewidgetitem1 = QTableWidgetItem("Min")
            self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
            __qtablewidgetitem2 = QTableWidgetItem("Max")
            self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
            __qtablewidgetitem3 = QTableWidgetItem("Set Value")
            self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
            __qtablewidgetitem4 = QTableWidgetItem("Unit")
            self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
            width = self.ui.tab_param.width()-25
            header = self.tableWidget.horizontalHeader()
            self.tableWidget.setColumnWidth(0, width * 4 / 10)
            self.tableWidget.setColumnWidth(2, width * 1 / 10)
            self.tableWidget.setColumnWidth(3, width * 1 / 10)
            self.tableWidget.setColumnWidth(4, width * 3 / 10)
            self.tableWidget.setColumnWidth(5, width * 1 / 10)
            # self.tableWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
            j = 5
            values = getTable(index)[(i-1)*j:(i-1)*j + 5]
            row = 0
            self.tableWidget.setRowCount(len(values))
            for value in values:
                self.tableWidget.setVerticalHeaderItem(row, QTableWidgetItem(value[5]))
                if lang == 'kor':
                    self.tableWidget.setItem(row, 0, QTableWidgetItem(value[3]))
                    self.tableWidget.setItem(row, 4, QTableWidgetItem(value[10]))
                else:
                    self.tableWidget.setItem(row, 0, QTableWidgetItem(value[4]))
                    self.tableWidget.setItem(row, 4, QTableWidgetItem(value[11]))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(value[6]))
                self.tableWidget.setItem(row, 2, QTableWidgetItem(value[7]))
                self.tableWidget.setItem(row, 3, QTableWidgetItem(nex1100[value[1]][value[2]]))
                row = row + 1

            self.gridLayout = QGridLayout()
            self.gridLayout.setContentsMargins(2, 2, 2, 2)
            self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
            self.ui.tab_param.addTab(self.tableWidget, "PID Gain " + str(i))
    else:
        titles = getTitle(index)
        if lang == 'kor':
            self.ui.label_table_title.setText(titles[0])
        else:
            self.ui.label_table_title.setText(titles[1])
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_table)
        values = getTable(index)
        row = 0
        self.ui.tableWidget.setRowCount(len(values))
        for value in values:
            self.ui.tableWidget.setVerticalHeaderItem(row, QTableWidgetItem(value[5]))
            self.ui.tableWidget.setCellWidget(row, 3, None)
            if lang == 'kor':
                self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(value[3]))
                self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(value[10]))
            else:
                self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(value[4]))
                self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(value[11]))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(value[6]))
            self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(value[7]))
            # 운전동작설정
            if index == 106 or index == 107:
                if row == 0:
                    self.mod = QComboBox()
                    self.mod.addItems(itemBox(lang, 'MOD'))
                    self.mod.setCurrentIndex(nex1100[value[1]][value[2]])
                    self.ui.tableWidget.setCellWidget(row, 3, self.mod)
                elif row == 1 or row == 6 or row == 7:
                    self.onbtn = QComboBox()
                    self.onbtn.addItems(itemBox(lang, 'ONBTN'))
                    self.onbtn.setCurrentIndex(nex1100[value[1]][value[2]])
                    self.ui.tableWidget.setCellWidget(row, 3, self.onbtn)
                elif row == 9:
                    self.lock = QComboBox()
                    self.lock.addItems(itemBox(lang, 'lock'))
                    self.lock.setCurrentIndex(nex1100[value[1]][value[2]])
                    self.ui.tableWidget.setCellWidget(row, 3, self.lock)
                elif row == 10:
                    self.rmd = QComboBox()
                    self.rmd.addItems(itemBox(lang, 'RMD'))
                    self.rmd.setCurrentIndex(nex1100[value[1]][value[2]])
                    self.ui.tableWidget.setCellWidget(row, 3, self.rmd)
                elif row == 3:
                    self.frth = QLineEdit()
                    t1 = datetime.timedelta(seconds=int(nex1100[value[1]][value[2]]))
                    self.frth.setText(str(t1))
                    self.ui.tableWidget.setCellWidget(row, 3, self.frth)
                else:
                    self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(nex1100[value[1]][value[2]]))
            # SD저장설정
            elif index == 124:
                if row == 1:
                    self.actbox = QComboBox()
                    self.actbox.addItems(itemBox(lang, 'actbox'))
                    self.actbox.setCurrentIndex(nex1100[value[1]][value[2]])
                    self.ui.tableWidget.setCellWidget(row, 3, self.actbox)
                elif row == 0:
                    self.frth = QLineEdit()
                    t1 = datetime.timedelta(seconds=int(nex1100[value[1]][value[2]]))
                    # t2 = t1.
                    self.frth.setText(str(t1))
                    self.ui.tableWidget.setCellWidget(row, 3, self.frth)
                else:
                    self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(nex1100[value[1]][value[2]]))
            # 화면설정
            elif index == 123:
                if row == 0:
                    self.lang = QComboBox()
                    self.lang.addItems(itemBox(lang, 'actbox'))
                    self.lang.setCurrentIndex(nex1100[value[1]][value[2]])
                    self.ui.tableWidget.setCellWidget(row, 3, self.lang)
                elif row == 1:
                    self.font = QComboBox()
                    self.font.addItems(itemBox(lang, 'font'))
                    self.font.setCurrentIndex(nex1100[value[1]][value[2]])
                    self.ui.tableWidget.setCellWidget(row, 3, self.font)
                elif row == 5 or row == 6:
                    self.onbtn = QComboBox()
                    self.onbtn.addItems(itemBox(lang, 'ONBTN'))
                    self.onbtn.setCurrentIndex(nex1100[value[1]][value[2]])
                    self.ui.tableWidget.setCellWidget(row, 3, self.onbtn)
                elif row == 9:
                    self.msd = QComboBox()
                    self.msd.addItems(itemBox(lang, 'msd'))
                    self.msd.setCurrentIndex(nex1100[value[1]][value[2]])
                    self.ui.tableWidget.setCellWidget(row, 3, self.msd)
                else:
                    self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(nex1100[value[1]][value[2]]))
            # 기본설정
            elif index == 133 or index == 144:
                if row == 0:
                    self.type = QComboBox()
                    self.type.addItems(itemBox(lang, 'TYPE'))
                    self.type.setCurrentIndex(nex1100[value[1]][value[2]])
                    self.ui.tableWidget.setCellWidget(row, 3, self.type)
                elif row == 1:
                    self.sensor = QComboBox()
                    self.sensor.addItems(itemBox(lang, 'TC'))
                    self.sensor.setCurrentIndex(nex1100[value[1]][value[2]])
                    self.ui.tableWidget.setCellWidget(row, 3, self.sensor)
                else:
                    self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(nex1100[value[1]][value[2]]))
            # PID
            elif index == 194 or index == 195:
                if row == 0:
                    self.zon = QComboBox()
                    self.zon.addItems(itemBox(lang, 'ZON'))
                    self.zon.setCurrentIndex(nex1100[value[1]][value[2]])
                    self.ui.tableWidget.setCellWidget(row, 3, self.zon)
                elif row == 1:
                    self.isat = QComboBox()
                    self.isat.addItems(itemBox(lang, 'ISAT'))
                    self.isat.setCurrentIndex(nex1100[value[1]][value[2]])
                    self.ui.tableWidget.setCellWidget(row, 3, self.isat)
                elif row == 2:
                    self.usebox = QComboBox()
                    self.usebox.addItems(itemBox(lang, 'usebox'))
                    self.usebox.setCurrentIndex(nex1100[value[1]][value[2]])
                    self.ui.tableWidget.setCellWidget(row, 3, self.usebox)
                elif row == 3:
                    self.onbtn = QComboBox()
                    self.onbtn.addItems(itemBox(lang, 'ONBTN'))
                    self.onbtn.setCurrentIndex(nex1100[value[1]][value[2]])
                    self.ui.tableWidget.setCellWidget(row, 3, self.onbtn)
                else:
                    self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(nex1100[value[1]][value[2]]))
            # DI동작방식
            elif index == 158 or index == 159:
                if row == 0:
                    self.at1 = QComboBox()
                    self.at1.addItems(itemBox(lang, 'at1'))
                    self.at1.setCurrentIndex(nex1100[value[1]][value[2]])
                    self.ui.tableWidget.setCellWidget(row, 3, self.at1)
                elif row == 1:
                    self.diact1 = QComboBox()
                    self.diact1.addItems(itemBox(lang, 'diact1'))
                    self.diact1.setCurrentIndex(nex1100[value[1]][value[2]])
                    self.ui.tableWidget.setCellWidget(row, 3, self.diact1)
                elif row == 2:
                    self.diact2 = QComboBox()
                    self.diact2.addItems(itemBox(lang, 'diact2'))
                    self.diact2.setCurrentIndex(nex1100[value[1]][value[2]])
                    self.ui.tableWidget.setCellWidget(row, 3, self.diact2)
                elif row == 3:
                    self.diact3 = QComboBox()
                    self.diact3.addItems(itemBox(lang, 'diact3'))
                    self.diact3.setCurrentIndex(nex1100[value[1]][value[2]])
                    self.ui.tableWidget.setCellWidget(row, 3, self.diact3)
                elif row == 4:
                    self.diact4 = QComboBox()
                    self.diact4.addItems(itemBox(lang, 'diact4'))
                    self.diact4.setCurrentIndex(nex1100[value[1]][value[2]])
                    self.ui.tableWidget.setCellWidget(row, 3, self.diact4)
                else:
                    self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(nex1100[value[1]][value[2]]))
            ##
            # 고급설정

            else:
                self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(nex1100[value[1]][value[2]]))
            row = row + 1

"""경보시그널(126)
        DO릴레이(131)
        통신환경(132)
    고급설정(105)
        센서설정(176)
        전송제어출력(177)
        구간별입력보정(178)
        PID설정및복사(179)
        DI접점방식(180)
        DI기능동작(181)
        상태램프설정(182)
        화면설정및PW(183)
"""

# SENSOR TYPE ON SENSOR GROUP
def sensorType(self, ch):
    if ch == 1:
        nex1100[15][1] = self.type.currentIndex()
        type = self.type.currentText()
        self.sensor = QComboBox()
        self.sensor.addItems(typeBox(type))
    elif ch == 2:
        nex1100[16][1] = self.type.currentIndex()
        type = self.type.currentText()
        self.sensor = QComboBox()
        self.sensor.addItems(typeBox(type))


# MIN/MAX VALUE ON SENSOR GROUP
# def changeVal(self, ch):
#     if ch == 1:
#         nex1100[15][1] = self.type.currentIndex()
#         if nex1100[15][1] == 0:
#             sensor = self.sensor.currentIndex()
#
#             for i in eu1(1):
#                 limit1100[i]['min'] =


# def sensorType(self, ch):
#     eu1 = eu1(ch)
#     eus1 = eus1(ch)
#     # CH1 SENSOR TYPE VARIABLE
#     if ch == 1:
#         nex1100[15][1] = self.type.currentIndex()
#         if nex1100[15][1] == 0:
#             value = typeBox('TC')
#             for eu in eu1:
#                 limit1100[eu[0]]['min'] = value[1]
#                 limit1100[eu[0]]['max'] = value[2]
#             self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(value[6]))
#             self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(value[7]))
#     # CH2 SENSOR TYPE VARIABLE
#     elif ch == 2:
#         nex1100[16][1] = self.type.currentIndex()


# CHANGE LANGUAGE
@QtCore.Slot(QtWidgets.QAction)
def changeLang(self, lang, index):
    setLang(lang)
    newlang = getLang()
    ## USER TREE
    userModel(self, newlang)
    ## ADMIN TREE
    adminModel(self, newlang)
    titles = getTitle(index)
    useridx = listIdx(1)
    adminidx = listIdx(2)
    if lang == 'kor':
        if self.translator.load('main.ko-KR'):
            QtCore.QCoreApplication.instance().installTranslator(self.translator)
        if index == 137 or index == 138 or index == 139 or index == 140 or index == 196 or index == 197:
            self.ui.label_tab_title.setText(titles[0])
        elif index == 114 or index == 115:
            if index == 114:
                self.ui.label_ptn_title.setText("패턴편집 - CH1")
            else:
                self.ui.label_ptn_title.setText("패턴편집 - CH2")
        else:
            self.ui.label_table_title.setText(titles[0])
        if index in useridx:
            userItem(self, lang, index)
        else:
            adminItem(self, lang, index)
    else:
        QtCore.QCoreApplication.instance().removeTranslator(self.translator)
        if index == 137 or index == 138 or index == 139 or index == 140 or index == 196 or index == 197:
            adminItem(self, lang, index)
            self.ui.label_tab_title.setText(titles[1])
        elif index == 114 or index == 115:
            userItem(self, lang, index)
            if index == 114:
                self.ui.label_ptn_title.setText("Pattern Edit - CH1")
            else:
                self.ui.label_ptn_title.setText("Pattern Edit - CH2")
        else:
            self.ui.label_table_title.setText(titles[1])
        if index in useridx:
            userItem(self, lang, index)
        else:
            adminItem(self, lang, index)