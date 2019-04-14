import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from Close import CloseWin
from Ui_test2 import Ui_MainWindow

class MyMainWindow(QMainWindow,CloseWin):
    def __init__(self,parent = None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

class Ui_MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent = None):
        super(Ui_MainWindow, self).__init__(parent)
        self.setupUi(self)

    # @pyqtSignature("")
    # def on_pushButton_6_clicked(self):


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin1 = Ui_MainWindow()
    # myWin.show()
    myWin1.show()
    sys.exit(app.exec_())
