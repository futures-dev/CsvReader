# coding=utf-8
__author__ = 'Kolomiets'

from PyQt4 import QtGui
from GUI.MainWindow_Ui.MainWindow import main_window_show

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    mainWindow = main_window_show()

    sys.exit(app.exec_())