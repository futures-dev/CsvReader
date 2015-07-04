# coding=utf-8
__author__ = 'Kolomiets'

class CsvReader(object):

    def __init__(self,header=list(),rows=list()):
        self.header = header
        self.rows = rows
        self.__indent = 0

    @property
    def indent(self):
        if self.__indent==0:
            max = 0
            for row in self.rows:
                for cell in row:
                    if len(cell)>max:
                        max = len(cell)
            for cell in self.header:
                if len(cell)>max:
                    max = len(cell)
            self.__indent = max + 2
        return self.__indent

    def open(self,fileName,separator=','):
        fileName.replace('/','\\',0)
        with open(fileName,'r') as f:
            self.header = f.readline().split(separator)
            for line in f:
                self.rows.append(line.split(separator))

    def print_table(self):
        s = ''
        for cell in self.header:
            s += '{0:{1}}'.format(cell,self.indent)
        s = s.split('\n')[0]
        print s
        for row in self.rows:
            s = ''
            for cell in row:
                s += '{0:{1}}'.format(cell,self.indent)
            s = s.split('\n')[0]
            print s

    def filter_rows(self,columns,predicates):
        newRows = list()
        for row in self.rows:
            ok = True
            for i in xrange(min(len(columns),len(predicates))):
                if not predicates[i](row[columns[i]]):
                    ok = False
                    break
            if ok:
                newRows.append(row)
        return CsvReader(self.header,newRows)

    def filter_columns(self,columns):
        newHeader = list()
        newRows = list()
        for c in columns:
            newHeader.append(self.header[c])
        for row in self.rows:
            newRow = list()
            for c in columns:
                newRow.append(row[c])
            newRows.append(newRow)
        return CsvReader(newHeader,newRows)


