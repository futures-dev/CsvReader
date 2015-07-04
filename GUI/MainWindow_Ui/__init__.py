# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tableView = QtGui.QTableView(self.centralwidget)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.gridLayout.addWidget(self.tableView, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.fileMenu = QtGui.QMenu(self.menubar)
        self.fileMenu.setObjectName(_fromUtf8("fileMenu"))
        self.helpMenu = QtGui.QMenu(self.menubar)
        self.helpMenu.setObjectName(_fromUtf8("helpMenu"))
        self.actionMenu = QtGui.QMenu(self.menubar)
        self.actionMenu.setObjectName(_fromUtf8("actionMenu"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.openButton = QtGui.QAction(MainWindow)
        self.openButton.setObjectName(_fromUtf8("openButton"))
        self.settingsButton = QtGui.QAction(MainWindow)
        self.settingsButton.setObjectName(_fromUtf8("settingsButton"))
        self.exitButton = QtGui.QAction(MainWindow)
        self.exitButton.setObjectName(_fromUtf8("exitButton"))
        self.aboutButton = QtGui.QAction(MainWindow)
        self.aboutButton.setObjectName(_fromUtf8("aboutButton"))
        self.filterButton = QtGui.QAction(MainWindow)
        self.filterButton.setObjectName(_fromUtf8("filterButton"))
        self.fileMenu.addAction(self.openButton)
        self.fileMenu.addAction(self.settingsButton)
        self.fileMenu.addAction(self.exitButton)
        self.helpMenu.addAction(self.aboutButton)
        self.actionMenu.addAction(self.filterButton)
        self.menubar.addAction(self.fileMenu.menuAction())
        self.menubar.addAction(self.actionMenu.menuAction())
        self.menubar.addAction(self.helpMenu.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.exitButton, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "CsvViewer", None))
        self.fileMenu.setTitle(_translate("MainWindow", "Файл", None))
        self.helpMenu.setTitle(_translate("MainWindow", "Справка", None))
        self.actionMenu.setTitle(_translate("MainWindow", "Действия", None))
        self.openButton.setText(_translate("MainWindow", "Открыть", None))
        self.settingsButton.setText(_translate("MainWindow", "Настройки", None))
        self.exitButton.setText(_translate("MainWindow", "Выход", None))
        self.aboutButton.setText(_translate("MainWindow", "О программе", None))
        self.filterButton.setText(_translate("MainWindow", "Фильтр", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

