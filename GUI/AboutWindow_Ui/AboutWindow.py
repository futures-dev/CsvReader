# coding=utf-8
__author__ = 'Kolomiets'

from PyQt4 import QtGui
from GUI.AboutWindow_Ui import Ui_AboutWindow

def about_window_show():
    aw = AboutWindow(Ui_AboutWindow())
    aw.show()
    return aw

class AboutWindow(QtGui.QWidget):
    def __init__(self,ui):
        super(AboutWindow,self).__init__()
        ui.setupUi(self)

        self.ui = ui