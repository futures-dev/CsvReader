# coding=utf-8
__author__ = 'Kolomiets'

from GUI.MainWindow_Ui.MainWindow import *
from GUI.AboutWindow_Ui.AboutWindow import *

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)

    mainWindow = main_window_show()

    sys.exit(app.exec_())