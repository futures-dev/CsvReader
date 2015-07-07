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
        FilterWindow.resize(632, 312)
        self.label = QtGui.QLabel(FilterWindow)
        self.label.setGeometry(QtCore.QRect(30, 20, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(FilterWindow)
        self.label_2.setGeometry(QtCore.QRect(290, 20, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.scrollArea = QtGui.QScrollArea(FilterWindow)
        self.scrollArea.setGeometry(QtCore.QRect(10, 60, 611, 201))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 609, 199))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_3 = QtGui.QLabel(FilterWindow)
        self.label_3.setGeometry(QtCore.QRect(420, 20, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.saveButton = QtGui.QPushButton(FilterWindow)
        self.saveButton.setGeometry(QtCore.QRect(324, 270, 121, 31))
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.exitButton = QtGui.QPushButton(FilterWindow)
        self.exitButton.setGeometry(QtCore.QRect(490, 270, 91, 31))
        self.exitButton.setObjectName(_fromUtf8("exitButton"))
        self.commandLinkButton = QtGui.QCommandLinkButton(FilterWindow)
        self.commandLinkButton.setGeometry(QtCore.QRect(130, 5, 151, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(10)
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))

        self.retranslateUi(FilterWindow)
        QtCore.QMetaObject.connectSlotsByName(FilterWindow)

    def retranslateUi(self, FilterWindow):
        FilterWindow.setWindowTitle(_translate("FilterWindow", "Фильтр", None))
        self.label.setText(_translate("FilterWindow", "Колонка", None))
        self.label_2.setText(_translate("FilterWindow", "Значение", None))
        self.label_3.setText(_translate("FilterWindow", "Точное соответствие", None))
        self.saveButton.setText(_translate("FilterWindow", "Применить", None))
        self.exitButton.setText(_translate("FilterWindow", "Отмена", None))
        self.commandLinkButton.setText(_translate("FilterWindow", "Добавить", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    FilterWindow = QtGui.QWidget()
    ui = Ui_FilterWindow()
    ui.setupUi(FilterWindow)
    FilterWindow.show()
    sys.exit(app.exec_())

