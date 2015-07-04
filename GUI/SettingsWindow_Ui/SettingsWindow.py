# coding=utf-8
__author__ = 'Kolomiets'

from GUI.SettingsWindow_Ui import *
from Data import Settings

def settings_window_show():
    sw = SettingsWindow(Ui_SettingsWindow())
    sw.show()
    return sw

class SettingsWindow(QtGui.QWidget):
    def save(self):
        Settings.Separator = self.ui.separatorBox.currentIndex()
        self.close()


    def __init__(self,ui):
        super(SettingsWindow,self).__init__()
        ui.setupUi(self)

        QtCore.QObject.connect(ui.saveButton, QtCore.SIGNAL('clicked()'),self.save)
        QtCore.QObject.connect(ui.exitButton, QtCore.SIGNAL('clicked()'),self.close)
        ui.separatorBox.setCurrentIndex(Settings.Separator)

        self.ui = ui
