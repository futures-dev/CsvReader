# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FilterWindow.ui'
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

class Ui_FilterWindow(object):
    def setupUi(self, FilterWindow):
        FilterWindow.setObjectName(_fromUtf8("FilterWindow"))
        FilterWindow.resize(632, 301)
        self.label = QtGui.QLabel(FilterWindow)
        self.label.setGeometry(QtCore.QRect(20, 10, 141, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(FilterWindow)
        self.label_2.setGeometry(QtCore.QRect(280, 10, 91, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.scrollArea = QtGui.QScrollArea(FilterWindow)
        self.scrollArea.setGeometry(QtCore.QRect(10, 40, 611, 221))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 609, 219))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.comboBox = QtGui.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 241, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.verticalScrollBar = QtGui.QScrollBar(self.scrollAreaWidgetContents)
        self.verticalScrollBar.setGeometry(QtCore.QRect(590, 0, 16, 251))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName(_fromUtf8("verticalScrollBar"))
        self.lineEdit = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit.setGeometry(QtCore.QRect(270, 10, 291, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.checkBox = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox.setGeometry(QtCore.QRect(570, 10, 20, 20))
        self.checkBox.setText(_fromUtf8(""))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_3 = QtGui.QLabel(FilterWindow)
        self.label_3.setGeometry(QtCore.QRect(460, 10, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.saveButton = QtGui.QPushButton(FilterWindow)
        self.saveButton.setGeometry(QtCore.QRect(350, 270, 75, 23))
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.exitButton = QtGui.QPushButton(FilterWindow)
        self.exitButton.setGeometry(QtCore.QRect(490, 270, 75, 23))
        self.exitButton.setObjectName(_fromUtf8("exitButton"))

        self.retranslateUi(FilterWindow)
        QtCore.QMetaObject.connectSlotsByName(FilterWindow)

    def retranslateUi(self, FilterWindow):
        FilterWindow.setWindowTitle(_translate("FilterWindow", "Фильтр", None))
        self.label.setText(_translate("FilterWindow", "Колонка", None))
        self.label_2.setText(_translate("FilterWindow", "Значение", None))
        self.label_3.setText(_translate("FilterWindow", "Точное соответствие", None))
        self.saveButton.setText(_translate("FilterWindow", "Применить", None))
        self.exitButton.setText(_translate("FilterWindow", "Отмена", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    FilterWindow = QtGui.QWidget()
    ui = Ui_FilterWindow()
    ui.setupUi(FilterWindow)
    FilterWindow.show()
    sys.exit(app.exec_())

