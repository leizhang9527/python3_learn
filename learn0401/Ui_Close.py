# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\work-space\eric6\learn\Close.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_guanbichuangkou(object):
    def setupUi(self, guanbichuangkou):
        guanbichuangkou.setObjectName("guanbichuangkou")
        guanbichuangkou.resize(1066, 864)
        self.centralwidget = QtWidgets.QWidget(guanbichuangkou)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 200, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        guanbichuangkou.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(guanbichuangkou)
        self.statusbar.setObjectName("statusbar")
        guanbichuangkou.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(guanbichuangkou)
        self.toolBar.setObjectName("toolBar")
        guanbichuangkou.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtWidgets.QToolBar(guanbichuangkou)
        self.toolBar_2.setObjectName("toolBar_2")
        guanbichuangkou.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        self.caidnalan = QtWidgets.QMenuBar(guanbichuangkou)
        self.caidnalan.setGeometry(QtCore.QRect(0, 0, 1066, 26))
        self.caidnalan.setObjectName("caidnalan")
        self.wenjian = QtWidgets.QMenu(self.caidnalan)
        self.wenjian.setEnabled(True)
        self.wenjian.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.wenjian.setAutoFillBackground(True)
        self.wenjian.setTearOffEnabled(True)
        self.wenjian.setSeparatorsCollapsible(True)
        self.wenjian.setToolTipsVisible(True)
        self.wenjian.setObjectName("wenjian")
        self.bianji = QtWidgets.QMenu(self.caidnalan)
        self.bianji.setObjectName("bianji")
        guanbichuangkou.setMenuBar(self.caidnalan)
        self.toolBar_3 = QtWidgets.QToolBar(guanbichuangkou)
        self.toolBar_3.setObjectName("toolBar_3")
        guanbichuangkou.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_3)
        self.actionfileOpenAction = QtWidgets.QAction(guanbichuangkou)
        self.actionfileOpenAction.setCheckable(True)
        self.actionfileOpenAction.setPriority(QtWidgets.QAction.LowPriority)
        self.actionfileOpenAction.setObjectName("actionfileOpenAction")
        self.actionfileNewAction = QtWidgets.QAction(guanbichuangkou)
        self.actionfileNewAction.setCheckable(True)
        self.actionfileNewAction.setObjectName("actionfileNewAction")
        self.actionCloseAction = QtWidgets.QAction(guanbichuangkou)
        self.actionCloseAction.setCheckable(True)
        self.actionCloseAction.setObjectName("actionCloseAction")
        self.wenjian.addSeparator()
        self.wenjian.addSeparator()
        self.wenjian.addSeparator()
        self.bianji.addSeparator()
        self.bianji.addSeparator()
        self.caidnalan.addAction(self.wenjian.menuAction())
        self.caidnalan.addAction(self.bianji.menuAction())

        self.retranslateUi(guanbichuangkou)
        self.pushButton.clicked.connect(guanbichuangkou.close)
        QtCore.QMetaObject.connectSlotsByName(guanbichuangkou)

    def retranslateUi(self, guanbichuangkou):
        _translate = QtCore.QCoreApplication.translate
        guanbichuangkou.setWindowTitle(_translate("guanbichuangkou", "MainWindow"))
        self.pushButton.setText(_translate("guanbichuangkou", "关闭窗口"))
        self.toolBar.setWindowTitle(_translate("guanbichuangkou", "toolBar"))
        self.toolBar_2.setWindowTitle(_translate("guanbichuangkou", "toolBar_2"))
        self.wenjian.setTitle(_translate("guanbichuangkou", "文件(&F)"))
        self.bianji.setTitle(_translate("guanbichuangkou", "编辑(&E)"))
        self.toolBar_3.setWindowTitle(_translate("guanbichuangkou", "toolBar_3"))
        self.actionfileOpenAction.setText(_translate("guanbichuangkou", "fileOpenAction"))
        self.actionfileOpenAction.setShortcut(_translate("guanbichuangkou", "Ctrl+O"))
        self.actionfileNewAction.setText(_translate("guanbichuangkou", "fileNewAction"))
        self.actionfileNewAction.setShortcut(_translate("guanbichuangkou", "Ctrl+N"))
        self.actionCloseAction.setText(_translate("guanbichuangkou", "CloseAction"))
        self.actionCloseAction.setShortcut(_translate("guanbichuangkou", "Ctrl+C"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    guanbichuangkou = QtWidgets.QMainWindow()
    ui = Ui_guanbichuangkou()
    ui.setupUi(guanbichuangkou)
    guanbichuangkou.show()
    sys.exit(app.exec_())

