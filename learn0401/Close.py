# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class CloseWin(object):
    def setupUi(self, closeWinBtn):
        closeWinBtn.setObjectName("closeWinBtn")
        closeWinBtn.resize(1066, 864)
        self.centralwidget = QtWidgets.QWidget(closeWinBtn)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 200, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        closeWinBtn.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(closeWinBtn)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1066, 26))
        self.menubar.setObjectName("menubar")
        closeWinBtn.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(closeWinBtn)
        self.statusbar.setObjectName("statusbar")
        closeWinBtn.setStatusBar(self.statusbar)

        self.retranslateUi(closeWinBtn)
        self.pushButton.clicked.connect(closeWinBtn.close)
        QtCore.QMetaObject.connectSlotsByName(closeWinBtn)

    def retranslateUi(self, closeWinBtn):
        _translate = QtCore.QCoreApplication.translate
        closeWinBtn.setWindowTitle(_translate("closeWinBtn", "MainWindow"))
        self.pushButton.setText(_translate("closeWinBtn", "关闭窗口"))

