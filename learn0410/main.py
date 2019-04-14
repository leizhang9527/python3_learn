# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from Ui_main import Ui_MainWindow
from glob import  glob
import re, os
import shutil
from os.path import join
from xlrd import  open_workbook


class MainWindow(QMainWindow, Ui_MainWindow):
    my_dir = ''

    def __init__(self,parent = None):
        QMainWindow.__init__(self,parent)
        self.setupUi(self)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.my_dir= QtWidgets.QFileDialog.getExistingDirectory(self, '选择文件夹', '/')
        my_dir = self.my_dir.replace('/', '\\')
        print('选择的文件所在目录是:',my_dir)

    
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        print('开始查找!!')
#        print(self.my_dir)
        
        #使用glob
        print('要找的是 :',self.lineEdit.text())
        my_list = re.split(r' ',self.lineEdit.text())
#         for eachone in my_list:
#             print(eachone)
#        print(glob(join(self.my_dir,'*.xlsx')))
        
#        self.dir = (QtWidgets.QFileDialog.getExistingDirectory(self, '选择文件夹', 'D:/work-space/eric6/')).replace("/", "\\")
        a = 0
        for fn in  glob(join(self.my_dir,'*.xlsx')):
            print( fn)
            wb = open_workbook(fn.replace('/', '\\'))
            for s in wb.sheets():
                for row in range(s.nrows):
                    for col in range(s.ncols):
                        if s.cell(row, col).value:
#                            print(s.cell(row, col).value)
                            for words in my_list:
#                                word = str(words)
                                if str(words) == s.cell(row,col).value:
                                    print( '找到了')
                                    a +=1
#                                   b = str(a)
#                                   x = '找到了出现了'+ b + '次,所在文件是:'
#                                   self.textEdit.setPlainText(x)
                                    self.textEdit.append( fn)
                                    if not os.path.exists(self.my_dir + '\\符合条件'):
                                        os.mkdir(self.my_dir + '\\符合条件')
                                        self.textEdit.append( '创建文件夹成功：%s'%self.my_dir + '\\符合条件')
                                    else:
                                        self.textEdit.append( '文件夹已存在，不需要重复创建')
                                    self.textEdit.append( '复制文件中...')
                                    shutil.copy(fn, self.my_dir + '\\符合条件')
                                    self.textEdit.append( '1个文件复制完成')
        self.textEdit.append( '一共处理了%s个文件'%str(a))
         
        #使用os
#         print(os.path.isdir(self.my_dir))     
#         if os.path.isdir(self.my_dir):
#             for myfile in os.listdir(self.my_dir):
# #                 print(myfile)
#                 if myfile[-5:] == '.xlsx':
#                     print("找到文件",myfile)

        
    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        self.textEdit.setPlainText('')

    @pyqtSlot()
    def on_actiondakai_triggered(self):
        """
        Slot documentation goes here.
        """
        

    
    @pyqtSlot()
    def on_actionguanbi_triggered(self):
        """
        Slot documentation goes here.
        """
        

    
    @pyqtSlot()
    def on_actiontuichu_triggered(self):
        """
        Slot documentation goes here.
        """
        sys.exit()

    
    @pyqtSlot()
    def on_actionshiyongshuoming_triggered(self):
        """
        Slot documentation goes here.
        """

    
    @pyqtSlot()
    def on_actionguanyu_triggered(self):
        """
        Slot documentation goes here.
        """


        
        
if  __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
    
    
