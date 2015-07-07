# coding=utf-8
__author__ = 'Kolomiets'

from PyQt4 import QtGui,QtCore
from GUI.AboutWindow_Ui import Ui_AboutWindow,_fromUtf8

def static_aw():
    def decorate(func):
        setattr(func,'aw',1)
        return func
    return decorate

@static_aw()
def about_window_show():
    if (about_window_show.aw==1):
        about_window_show.aw = AboutWindow(Ui_AboutWindow())
    about_window_show.aw.show()
    about_window_show.aw.activateWindow()
    return about_window_show.aw

class AboutWindow(QtGui.QWidget):
    def __init__(self,ui):
        super(AboutWindow,self).__init__()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowMaximizeButtonHint)
        ui.setupUi(self)

        self.ui = ui