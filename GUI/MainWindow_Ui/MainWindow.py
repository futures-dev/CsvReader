# coding=utf-8
__author__ = 'Kolomiets'

from GUI.MainWindow_Ui import *
from GUI.AboutWindow_Ui.AboutWindow import *
from GUI.SettingsWindow_Ui.SettingsWindow import *
from GUI.FilterWindow_Ui.FilterWindow import *
from CsvHandler import CsvReader

def main_window_show():
    m = MainWindow(Ui_MainWindow())
    m.show()
    return m

class TableModel(QtCore.QAbstractTableModel,CsvReader.CsvReader):

    def __init__(self,header=list(),rows=list()):
        QtCore.QAbstractTableModel.__init__(self)
        CsvReader.CsvReader.__init__(self,header,rows)

    def rowCount(self, QModelIndex_parent=None, *args, **kwargs):
        #if (QModelIndex_parent!=None):
        #    return 0
        #else:
            return len(self.rows)

    def columnCount(self, QModelIndex_parent=None, *args, **kwargs):
        #if (QModelIndex_parent!=None):
        #    return 0
        #else:
            return len(self.header)

    def data(self, QModelIndex, int_role=None):
        #God only knows what this is
        if not QModelIndex.isValid():
            return QtCore.QVariant()
        elif int_role!=QtCore.Qt.DisplayRole and int_role!=QtCore.Qt.EditRole:
            return QtCore.QVariant()
        #Return table[index.row,index.column]
        if int_role==QtCore.Qt.DisplayRole:
            return QtCore.QVariant(self.rows[QModelIndex.row()][QModelIndex.column()])
        else:
            return QtCore.QVariant('')

    def setData(self, QModelIndex, QVariant, int_role=None):
        pass

    def headerData(self, p_int, Qt_Orientation, int_role=None):
        if Qt_Orientation==QtCore.Qt.Horizontal and int_role==QtCore.Qt.DisplayRole:
            return QtCore.QVariant(self.header[p_int])
        else:
            return QtCore.QVariant()

class MainWindow(QtGui.QMainWindow):
    def about_window_show(self):
        self.windows.append(about_window_show())

    def settings_window_show(self):
        self.windows.append(settings_window_show())

    def filter_window_show(self):
        self.windows.append(filter_window_show())

    def open_file_dialog(self):
        fileName = unicode(QtGui.QFileDialog.getOpenFileName(self,u'Открыть файл')).encode('utf-8')
        if fileName[-4:]=='.csv':
            self.model = TableModel()
            self.model.gui = self.ui
            self.model.open(fileName,',' if Settings.Separator==0 else ';')
            self.ui.tableView.setModel(self.model)
            #phonebook = {"Олег": "Красноярск",
            #     "Вася": "Воронеж",
            #     "Петя": "Москва"}
            #model =QtGui.QStandardItemModel(3,2)
            #row = 0
            #for name, address in phonebook.items():
            # model.setData(model.index(row, 0), name)
            #model.setData(model.index(row, 1), address)
            #row += 1
            #model.setHeaderData(0, QtCore.Qt.Horizontal, "Имя")
            #model.setHeaderData(1, QtCore.Qt.Horizontal, "Адрес")

            self.ui.tableView.setModel(self.model)
            self.ui.tableView.show()

        else:
            QtGui.QMessageBox.warning(self,u'Ошибка',u'Файл '+fileName+u' имеет неверное расширение',QtGui.QMessageBox.Ok)

    def __init__(self,ui):
        super(MainWindow,self).__init__()
        ui.setupUi(self)
        self.windows = list()
        QtCore.QObject.connect(ui.aboutButton, QtCore.SIGNAL('triggered()'),self.about_window_show)
        QtCore.QObject.connect(ui.settingsButton, QtCore.SIGNAL('triggered()'),self.settings_window_show)
        QtCore.QObject.connect(ui.filterButton, QtCore.SIGNAL('triggered()'),self.filter_window_show)
        QtCore.QObject.connect(ui.openButton, QtCore.SIGNAL('triggered()'),self.open_file_dialog)

        self.ui = ui


