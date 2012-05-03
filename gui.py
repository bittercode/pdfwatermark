# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'watermarker.ui'
#
# Created: Thu May  3 12:19:02 2012
#      by: pyside-uic 0.2.13 running on PySide 1.0.8
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(329, 454)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.btnFindFile = QtGui.QPushButton(self.centralwidget)
        self.btnFindFile.setObjectName("btnFindFile")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.btnFindFile)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit)
        spacerItem = QtGui.QSpacerItem(20, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout_2.setItem(1, QtGui.QFormLayout.LabelRole, spacerItem)
        spacerItem1 = QtGui.QSpacerItem(20, 12, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout_2.setItem(1, QtGui.QFormLayout.FieldRole, spacerItem1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_2)
        self.verticalLayout.addLayout(self.formLayout_2)
        spacerItem2 = QtGui.QSpacerItem(20, 183, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 329, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.btnFindFile.setText(QtGui.QApplication.translate("MainWindow", "Select PDF", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Watermark Text", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "AddWatermark", None, QtGui.QApplication.UnicodeUTF8))

