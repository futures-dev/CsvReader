# coding=utf-8
__author__ = 'Kolomiets'

from PyQt4 import QtGui,QtCore
from GUI.MainWindow_Ui import Ui_MainWindow,_fromUtf8,_translate
from GUI.AboutWindow_Ui.AboutWindow import about_window_show
from GUI.SettingsWindow_Ui.SettingsWindow import settings_window_show
from GUI.FilterWindow_Ui.FilterWindow import filter_window_show
from Data import Settings
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
        return len(self.rows)

    def columnCount(self, QModelIndex_parent=None, *args, **kwargs):
        return len(self.header)

    def data(self, QModelIndex, int_role=None):
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
        if int_role==QtCore.Qt.EditRole:
            self.rows[QModelIndex.row()][QModelIndex.column()] = unicode(QVariant.toString())
            return True
        else:
            return False

    def headerData(self, p_int, Qt_Orientation, int_role=None):
        if int_role==QtCore.Qt.DisplayRole:
            if Qt_Orientation==QtCore.Qt.Horizontal:
                return QtCore.QVariant(self.header[p_int])
            elif Qt_Orientation==QtCore.Qt.Vertical and Settings.Rows():
                return QtCore.QVariant(p_int+1)
            else:
                return QtCore.QVariant()
        else:
            return QtCore.QVariant()

    def setHeaderData(self, p_int, Qt_Orientation, QVariant, int_role=None):
        if int_role==QtCore.Qt.EditRole and Qt_Orientation==QtCore.Qt.Horizontal:
            self.header[p_int] = unicode(QVariant.toString())
            return True
        else:
            return False

    def sort(self,colN,order):
        self.emit(QtCore.SIGNAL(_fromUtf8("layoutAboutToBeChanged()")))
        ints = True
        for line in self.rows:
            try:
                int(line[colN])
            except:
                ints=False
                break
        self.rows.sort(key=lambda x:int(x[colN]) if ints else x[colN])
        if order==QtCore.Qt.DescendingOrder:
            self.rows.reverse()
        self.emit(QtCore.SIGNAL(_fromUtf8("layoutChanged()")))

    def flags(self,index):
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

class MainWindow(QtGui.QMainWindow):
    def about_window_show(self):
        self.windows.append(about_window_show())

    def settings_window_show(self):
        self.windows.append(settings_window_show())

    def filter_window_show(self):
        self.windows.append(filter_window_show(self))

    def filter_model(self,columns,predicates):
        v = self.original.filter_rows(columns,predicates)
        self.filtered = TableModel(v[0],v[1])
        self.model = self.filtered
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.resizeColumnsToContents()
        self.ui.tableView.show()

    def open_file_dialog(self):
        fileName = unicode(QtGui.QFileDialog.getOpenFileName(self,u'Открыть файл'))
        if fileName[-4:]=='.csv':
            self.model = TableModel()
            self.model.gui = self.ui
            try:
                self.model.open(fileName,Settings.Separator(), Settings.Encoding(),Settings.Headers())
                QtCore.QTextCodec.setCodecForTr(QtCore.QTextCodec.codecForName(Settings.QEncoding()))
            except UnicodeDecodeError:
                QtGui.QMessageBox.warning(self,u'Ошибка',u'Файл '+fileName+u' записан не в кодировке '+Settings.Encoding(),QtGui.QMessageBox.Ok)
            self.ui.tableView.setModel(self.model)
            self.original = self.model
            self.ui.tableView.resizeColumnsToContents()
            self.ui.tableView.show()
        elif len(fileName)>0:
            QtGui.QMessageBox.warning(self,u'Ошибка',u'Файл '+fileName+u' имеет неверное расширение',QtGui.QMessageBox.Ok)

    def save_file_dialog(self):
        fileName = unicode(QtGui.QFileDialog.getSaveFileName(self,u'Сохранить как'))
        if fileName[-4:]=='.csv':
            self.model.save_as(fileName,Settings.Encoding(),Settings.NewLine(),Settings.Headers())
        elif len(fileName)>0:
            QtGui.QMessageBox.warning(self,u'Ошибка',u'Файл '+fileName+u' имеет неверное расширение',QtGui.QMessageBox.Ok)

    def __init__(self,ui):
        super(MainWindow,self).__init__()
        ui.setupUi(self)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.windows = list()
        QtCore.QObject.connect(ui.aboutButton, QtCore.SIGNAL(_fromUtf8('triggered()')),self.about_window_show)
        QtCore.QObject.connect(ui.settingsButton, QtCore.SIGNAL(_fromUtf8('triggered()')),self.settings_window_show)
        QtCore.QObject.connect(ui.filterButton, QtCore.SIGNAL(_fromUtf8('triggered()')),self.filter_window_show)
        QtCore.QObject.connect(ui.openButton, QtCore.SIGNAL(_fromUtf8('triggered()')),self.open_file_dialog)
        QtCore.QObject.connect(ui.saveAsButton, QtCore.SIGNAL(_fromUtf8('triggered()')),self.save_file_dialog)

        self.ui = ui


