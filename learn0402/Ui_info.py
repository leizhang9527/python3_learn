# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\work-space\eric6\learn0402\info.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(714, 519)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dialog.sizePolicy().hasHeightForWidth())
        dialog.setSizePolicy(sizePolicy)
        dialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        dialog.setSizeIncrement(QtCore.QSize(5, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        dialog.setFont(font)
        dialog.setSizeGripEnabled(True)
        self.label = QtWidgets.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(180, 70, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(dialog)
        self.label_2.setGeometry(QtCore.QRect(180, 200, 72, 15))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(dialog)
        self.label_3.setGeometry(QtCore.QRect(180, 240, 72, 15))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(dialog)
        self.label_4.setGeometry(QtCore.QRect(180, 280, 72, 15))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(dialog)
        self.label_5.setGeometry(QtCore.QRect(180, 110, 72, 15))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(dialog)
        self.label_6.setGeometry(QtCore.QRect(180, 160, 72, 15))
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(dialog)
        self.lineEdit.setGeometry(QtCore.QRect(230, 70, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 110, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(230, 160, 113, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(230, 200, 113, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(230, 240, 113, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(230, 280, 113, 21))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.toolButton = QtWidgets.QToolButton(dialog)
        self.toolButton.setGeometry(QtCore.QRect(360, 110, 47, 21))
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(dialog)
        self.toolButton_2.setGeometry(QtCore.QRect(360, 160, 47, 21))
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_3 = QtWidgets.QToolButton(dialog)
        self.toolButton_3.setGeometry(QtCore.QRect(360, 200, 47, 21))
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_4 = QtWidgets.QToolButton(dialog)
        self.toolButton_4.setGeometry(QtCore.QRect(360, 240, 47, 21))
        self.toolButton_4.setObjectName("toolButton_4")
        self.pushButton = QtWidgets.QPushButton(dialog)
        self.pushButton.setGeometry(QtCore.QRect(220, 360, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 360, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "用户信息输入框"))
        self.label.setText(_translate("dialog", "姓名："))
        self.label_2.setText(_translate("dialog", "身高："))
        self.label_3.setText(_translate("dialog", "体重："))
        self.label_4.setText(_translate("dialog", "电话："))
        self.label_5.setText(_translate("dialog", "年龄："))
        self.label_6.setText(_translate("dialog", "性别："))
        self.toolButton.setText(_translate("dialog", "..."))
        self.toolButton_2.setText(_translate("dialog", "..."))
        self.toolButton_3.setText(_translate("dialog", "..."))
        self.toolButton_4.setText(_translate("dialog", "..."))
        self.pushButton.setText(_translate("dialog", "提交"))
        self.pushButton_2.setText(_translate("dialog", "取消"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = Ui_dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())

