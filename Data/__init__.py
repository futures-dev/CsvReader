# coding=utf-8
__author__ = 'Kolomiets'

class Settings(object):
    separator=1
    encoding=1
    headers=1
    rows=1

    @staticmethod
    def Encoding():
        if Settings.encoding==0:
            return 'windows-1251'
        elif Settings.encoding==1:
            return 'utf-8'
        elif Settings.encoding==2:
            return 'mac_cyrillic'
        else:
            return 'windows-1251'

    @staticmethod
    def QEncoding():
        if Settings.encoding==0:
            return 'windows-1251'
        elif Settings.encoding==1:
            return 'utf-8'
        elif Settings.encoding==2:
            return 'ISO-8859-5'
        else:
            return 'windows-1251'

    @staticmethod
    def Separator():
        if Settings.separator==0:
            return ','
        elif Settings.separator==1:
            return ';'
        else:
            return ','

    @staticmethod
    def NewLine():
        if Settings.encoding==0:
            return '\n'
        elif Settings.encoding==1:
            return '\n'
        else:
            return '\r'

    @staticmethod
    def Headers():
        if Settings.headers==0:
            return False
        elif Settings.headers==1:
            return True
        else:
            return False

    @staticmethod
    def Rows():
        if Settings.rows==0:
            return True
        elif Settings.rows==1:
            return False
        else:
            return True