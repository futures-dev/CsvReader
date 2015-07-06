# coding=utf-8
__author__ = 'Kolomiets'

from GUI.FilterWindow_Ui import *

def filter_window_show(main):
    fw = FilterWindow(Ui_FilterWindow(),main)
    fw.show()
    return fw

class FilterWindow(QtGui.QWidget):

    form_i = 0

    def add_form(self):

        self.ui.comboBox[self.form_i] = QtGui.QComboBox(self.ui.scrollAreaWidgetContents);
        self.ui.groupBox[self.form_i] = QtGui.QGroupBox();
        self.ui.horizontalLayout[self.form_i] = QtGui.QHBoxLayout(self.ui.groupBox[self.form_i]);
        self.ui.horizontalLayout[self.form_i].setObjectName("horizontalLayout"+`self.form_i`);
        self.ui.comboBox[self.form_i].setMinimumSize(250,0);
        self.ui.comboBox[self.form_i].setObjectName("comboBox"+`self.form_i`);
        i=0
        for column in self.main.original.header:
            self.ui.comboBox[self.form_i].addItem("")
            self.ui.comboBox[self.form_i].setItemText(i,QtGui.QApplication.translate("FilterWindow", column, None))
            i+=1
        self.ui.lineEdit[self.form_i] = QtGui.QLineEdit(self.ui.scrollAreaWidgetContents);
        self.ui.lineEdit[self.form_i].setObjectName("lineEdit"+`self.form_i`);
        self.ui.checkBox[self.form_i] = QtGui.QCheckBox(self.ui.scrollAreaWidgetContents);
        self.ui.checkBox[self.form_i].setText("");
        self.ui.checkBox[self.form_i].setObjectName("checkBox"+`self.form_i`);
        self.ui.horizontalLayout[self.form_i].addWidget(self.ui.comboBox[self.form_i]);
        self.ui.horizontalLayout[self.form_i].addWidget(self.ui.lineEdit[self.form_i]);
        self.ui.horizontalLayout[self.form_i].addWidget(self.ui.checkBox[self.form_i]);
        self.ui.groupBox[self.form_i].setLayout(self.ui.horizontalLayout[self.form_i]);
        self.ui.verticalLayout.addWidget(self.ui.groupBox[self.form_i])

        self.form_i += 1

    def commit_filter(self):
        columns = []
        predicates = []
        for i in xrange(self.form_i):
            line=self.ui.lineEdit[i]
            combo=self.ui.comboBox[i]
            check=self.ui.checkBox[i]
            if (unicode(line.text())):
                columns.append(combo.currentIndex())
                predicates.append((lambda x:x==unicode(line.text())) if check.isChecked() else lambda x:x.upper().find(unicode(line.text()).upper())>-1)
        self.main.filter_model(columns,predicates)
        self.close()

    def __init__(self,ui,main):
        super(FilterWindow,self).__init__()
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