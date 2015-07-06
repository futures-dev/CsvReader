# coding=utf-8
__author__ = 'Kolomiets'

from PyQt4 import QtCore,QtGui
from GUI.SettingsWindow_Ui import Ui_SettingsWindow,_fromUtf8,_translate
from Data import Settings

def settings_window_show():
    sw = SettingsWindow(Ui_SettingsWindow())
    sw.show()
    return sw

class SettingsWindow(QtGui.QWidget):
    def save(self):
        Settings.separator = self.ui.separatorBox.currentIndex()
        Settings.encoding = self.ui.encodingBox.currentIndex()
        Settings.headers = self.ui.headersBox.isChecked()
        self.close()


    def __init__(self,ui):
        super(SettingsWindow,self).__init__()
        ui.setupUi(self)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        QtCore.QObject.connect(ui.saveButton, QtCore.SIGNAL(_fromUtf8('clicked()')),self.save)
        QtCore.QObject.connect(ui.exitButton, QtCore.SIGNAL(_fromUtf8('clicked()')),self.close)
        ui.separatorBox.setCurrentIndex(Settings.separator)
        ui.encodingBox.setCurrentIndex(Settings.encoding)
        ui.headersBox.setChecked(Settings.headers)

        self.ui = ui
