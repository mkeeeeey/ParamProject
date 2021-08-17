from PySide2 import QtCore, QtWidgets

import function_1100
from conn1100 import getTitle
from connDB import getLang, listIdx, setLang


## INITIALIZE START
def setStart(self):
    lang = getLang()
    if lang == 'kor':
        if self.translator.load("main.ko-KR"):
            QtCore.QCoreApplication.instance().installTranslator(self.translator)
            print('load')
    else:
        QtCore.QCoreApplication.instance().removeTranslator(self.translator)


## ==> TREE ITEM CLICK EVENT
############################################################################
## USER TREE CLICK EVENT
def userClick(self, nex, QModelIndex):
    global index
    item = self.user.itemData(QModelIndex)
    index = item[256]
    lang = getLang()
    self.nex = nex
    if self.nex == 'NEX1100':
        function_1100.userItem(self, lang, index)
    else:
        pass


## ADMIN TREE CLICK EVENT
def adminClick(self, nex, QModelIndex):
    global index
    item = self.admin.itemData(QModelIndex)
    index = item[256]
    lang = getLang()
    self.nex = nex
    if self.nex == 'NEX1100':
        function_1100.adminItem(self, lang, index)
    else:
        pass


