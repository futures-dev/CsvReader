# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SettingsWindow.ui'
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

class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        SettingsWindow.setObjectName(_fromUtf8("SettingsWindow"))
        SettingsWindow.resize(400, 158)
        self.separatorBox = QtGui.QComboBox(SettingsWindow)
        self.separatorBox.setEnabled(True)
        self.separatorBox.setGeometry(QtCore.QRect(203, 30, 181, 20))
        self.separatorBox.setObjectName(_fromUtf8("separatorBox"))
        self.separatorBox.addItem(_fromUtf8(""))
        self.separatorBox.addItem(_fromUtf8(""))
        self.separatorLabel = QtGui.QLabel(SettingsWindow)
        self.separatorLabel.setGeometry(QtCore.QRect(9, 30, 181, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(10)
        self.separatorLabel.setFont(font)
        self.separatorLabel.setObjectName(_fromUtf8("separatorLabel"))
        self.saveButton = QtGui.QPushButton(SettingsWindow)
        self.saveButton.setGeometry(QtCore.QRect(180, 120, 75, 23))
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.exitButton = QtGui.QPushButton(SettingsWindow)
        self.exitButton.setGeometry(QtCore.QRect(290, 120, 75, 23))
        self.exitButton.setObjectName(_fromUtf8("exitButton"))

        self.retranslateUi(SettingsWindow)
        QtCore.QMetaObject.connectSlotsByName(SettingsWindow)

    def retranslateUi(self, SettingsWindow):
        SettingsWindow.setWindowTitle(_translate("SettingsWindow", "Настройки", None))
        self.separatorBox.setItemText(0, _translate("SettingsWindow", ",", None))
        self.separatorBox.setItemText(1, _translate("SettingsWindow", ";", None))
        self.separatorLabel.setText(_translate("SettingsWindow", "Разделитель", None))
        self.saveButton.setText(_translate("SettingsWindow", "Сохранить", None))
        self.exitButton.setText(_translate("SettingsWindow", "Отмена", None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    SettingsWindow = QtGui.QWidget()
    ui = Ui_SettingsWindow()
    ui.setupUi(SettingsWindow)
    SettingsWindow.show()
    sys.exit(app.exec_())
