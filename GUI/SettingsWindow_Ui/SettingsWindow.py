# coding=utf-8
__author__ = 'Kolomiets'

from PyQt4 import QtCore,QtGui
from GUI.SettingsWindow_Ui import Ui_SettingsWindow,_fromUtf8,_translate
from Data import Settings

def static_sw():
    def decorate(func):
        setattr(func,'sw',1)
        return func
    return decorate

@static_sw()
def settings_window_show():
    if (settings_window_show.sw==1):
        settings_window_show.sw = SettingsWindow(Ui_SettingsWindow())
    settings_window_show.sw.show()
    settings_window_show.sw.activateWindow()
    return settings_window_show.sw

class SettingsWindow(QtGui.QWidget):
    def save(self):
        Settings.separator = self.ui.separatorBox.currentIndex()
        Settings.encoding = self.ui.encodingBox.currentIndex()
        Settings.headers = self.ui.headersBox.isChecked()
        Settings.rows = self.ui.rowsBox.isChecked()
        self.close()

    def closeEvent(self, QCloseEvent):
        self.ui.separatorBox.setCurrentIndex(Settings.separator)
        self.ui.encodingBox.setCurrentIndex(Settings.encoding)
        self.ui.headersBox.setChecked(Settings.headers)
        self.ui.rowsBox.setChecked(Settings.rows)
        QCloseEvent.accept()


    def __init__(self,ui):
        super(SettingsWindow,self).__init__()
        ui.setupUi(self)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowMaximizeButtonHint)

        QtCore.QObject.connect(ui.saveButton, QtCore.SIGNAL(_fromUtf8('clicked()')),self.save)
        QtCore.QObject.connect(ui.exitButton, QtCore.SIGNAL(_fromUtf8('clicked()')),self.close)
        ui.separatorBox.setCurrentIndex(Settings.separator)
        ui.encodingBox.setCurrentIndex(Settings.encoding)
        ui.headersBox.setChecked(Settings.headers)
        ui.rowsBox.setChecked(Settings.rows)

        self.ui = ui
