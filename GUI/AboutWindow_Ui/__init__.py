# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AboutWindow.ui'
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

class Ui_AboutWindow(object):
    def setupUi(self, AboutWindow):
        AboutWindow.setObjectName(_fromUtf8("AboutWindow"))
        AboutWindow.resize(400, 160)
        self.verticalLayout = QtGui.QVBoxLayout(AboutWindow)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_1 = QtGui.QLabel(AboutWindow)
        self.label_1.setScaledContents(False)
        self.label_1.setObjectName(_fromUtf8("label_1"))
        self.verticalLayout.addWidget(self.label_1)
        self.label_2 = QtGui.QLabel(AboutWindow)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.label_4 = QtGui.QLabel(AboutWindow)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.label_3 = QtGui.QLabel(AboutWindow)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.label_5 = QtGui.QLabel(AboutWindow)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)

        self.retranslateUi(AboutWindow)
        QtCore.QMetaObject.connectSlotsByName(AboutWindow)

    def retranslateUi(self, AboutWindow):
        AboutWindow.setWindowTitle(_translate("AboutWindow", "Form", None))
        self.label_1.setText(_translate("AboutWindow", "Программа для работы с csv таблицами", None))
        self.label_2.setText(_translate("AboutWindow", "Учебная практика. Python.", None))
        self.label_4.setText(_translate("AboutWindow", "Коломиец Андрей БПИ143", None))
        self.label_3.setText(_translate("AboutWindow", "aikolomiets@edu.hse.ru", None))
        self.label_5.setText(_translate("AboutWindow", "Программная инженерия 2015", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    AboutWindow = QtGui.QWidget()
    ui = Ui_AboutWindow()
    ui.setupUi(AboutWindow)
    AboutWindow.show()
    sys.exit(app.exec_())

