# coding=utf-8
__author__ = 'Kolomiets'

from GUI.FilterWindow_Ui import *

def filter_window_show():
    fw = FilterWindow(Ui_FilterWindow())
    fw.show()
    return fw

class FilterWindow(QtGui.QWidget):
    def __init__(self,ui):
        super(FilterWindow,self).__init__()
        ui.setupUi(self)

        self.ui = ui