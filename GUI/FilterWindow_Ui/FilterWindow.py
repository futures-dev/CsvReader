# coding=utf-8
__author__ = 'Kolomiets'

from PyQt4 import QtGui,QtCore
from GUI.FilterWindow_Ui import Ui_FilterWindow,_fromUtf8,_translate

def static_fw():
    def decorate(func):
        setattr(func,'fw',1)
        return func
    return decorate

@static_fw()
def filter_window_show(main):
    if (filter_window_show.fw==1):
        filter_window_show.fw = FilterWindow(Ui_FilterWindow(),main)
    filter_window_show.fw.show()
    return filter_window_show.fw

class FilterWindow(QtGui.QWidget):

    form_i = 0
    form_saved = 0

    def add_form(self):
        if (not self.form_i in self.ui.comboBox) or self.ui.comboBox[self.form_i].parentWidget()==None:

            self.ui.comboBox[self.form_i] = QtGui.QComboBox(self.ui.scrollAreaWidgetContents);
            self.ui.groupBox[self.form_i] = QtGui.QGroupBox();
            self.ui.horizontalLayout[self.form_i] = QtGui.QHBoxLayout(self.ui.groupBox[self.form_i]);
            self.ui.horizontalLayout[self.form_i].setObjectName(_fromUtf8("horizontalLayout"+`self.form_i`));
            self.ui.comboBox[self.form_i].setMinimumSize(250,0);
            self.ui.comboBox[self.form_i].setObjectName(_fromUtf8("comboBox"+`self.form_i`));
            i=0
            for column in self.main.original.header:
                self.ui.comboBox[self.form_i].addItem(_fromUtf8(""))
                self.ui.comboBox[self.form_i].setItemText(i,_translate("FilterWindow", column, None))
                i+=1
            self.ui.lineEdit[self.form_i] = QtGui.QLineEdit(self.ui.scrollAreaWidgetContents);
            self.ui.lineEdit[self.form_i].setObjectName(_fromUtf8("lineEdit"+`self.form_i`));
            self.ui.checkBox[self.form_i] = QtGui.QCheckBox(self.ui.scrollAreaWidgetContents);
            self.ui.checkBox[self.form_i].setText(_fromUtf8(""));
            self.ui.checkBox[self.form_i].setObjectName(_fromUtf8("checkBox"+`self.form_i`));
            self.ui.horizontalLayout[self.form_i].addWidget(self.ui.comboBox[self.form_i]);
            self.ui.horizontalLayout[self.form_i].addWidget(self.ui.lineEdit[self.form_i]);
            self.ui.horizontalLayout[self.form_i].addWidget(self.ui.checkBox[self.form_i]);
            self.ui.groupBox[self.form_i].setLayout(self.ui.horizontalLayout[self.form_i]);
            self.ui.verticalLayout.addWidget(self.ui.groupBox[self.form_i])

        else:
            self.ui.groupBox[self.form_i].setLayout(self.ui.horizontalLayout[self.form_i])
            self.ui.verticalLayout.addWidget(self.ui.groupBox[self.form_i])

        self.form_i += 1

    def commit_filter(self):
        self.form_saved = self.form_i
        columns = []
        predicates = []
        for i in xrange(self.form_i):
            line=self.ui.lineEdit[i]
            combo=self.ui.comboBox[i]
            check=self.ui.checkBox[i]
            if (unicode(line.text())):
                columns.append(combo.currentIndex())
                predicates.append((lambda x,line=line:x==unicode(line.text())) if check.isChecked() else
                                  lambda x,line=line:x.upper().find(unicode(line.text()).upper())>-1)
        self.main.filter_model(columns,predicates)
        self.close()

    def closeEvent(self, QCloseEvent):
        for i in range(self.form_saved,self.form_i):
            self.ui.verticalLayout.removeWidget(self.ui.groupBox[i])
            self.ui.groupBox[i].setParent(None)
        self.form_saved=self.form_i
        QCloseEvent.accept()

    def __init__(self,ui,main):
        super(FilterWindow,self).__init__()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        ui.setupUi(self)
        ui.comboBox = {}
        ui.groupBox = {}
        ui.horizontalLayout = {}
        ui.lineEdit = {}
        ui.checkBox = {}
        self.main = main
        QtCore.QObject.connect(ui.commandLinkButton, QtCore.SIGNAL('clicked()'),self.add_form)
        QtCore.QObject.connect(ui.saveButton, QtCore.SIGNAL('clicked()'),self.commit_filter)
        QtCore.QObject.connect(ui.exitButton, QtCore.SIGNAL('clicked()'),self.close)
            

        self.ui = ui