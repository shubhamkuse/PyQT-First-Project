# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demolao.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(431, 283)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Generate_show = QtGui.QTextEdit(self.centralwidget)
        self.Generate_show.setGeometry(QtCore.QRect(150, 220, 271, 31))
        self.Generate_show.setObjectName(_fromUtf8("Generate_show"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 71, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.Y3 = QtGui.QLineEdit(self.centralwidget)
        self.Y3.setGeometry(QtCore.QRect(180, 130, 71, 22))
        self.Y3.setObjectName(_fromUtf8("Y3"))
        self.R3 = QtGui.QLineEdit(self.centralwidget)
        self.R3.setGeometry(QtCore.QRect(330, 130, 71, 22))
        self.R3.setObjectName(_fromUtf8("R3"))
        self.X2 = QtGui.QLineEdit(self.centralwidget)
        self.X2.setGeometry(QtCore.QRect(20, 90, 71, 22))
        self.X2.setObjectName(_fromUtf8("X2"))
        self.X1 = QtGui.QLineEdit(self.centralwidget)
        self.X1.setGeometry(QtCore.QRect(20, 50, 71, 22))
        self.X1.setObjectName(_fromUtf8("X1"))
        self.X3 = QtGui.QLineEdit(self.centralwidget)
        self.X3.setGeometry(QtCore.QRect(20, 130, 71, 22))
        self.X3.setObjectName(_fromUtf8("X3"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(350, 20, 46, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.Y1 = QtGui.QLineEdit(self.centralwidget)
        self.Y1.setGeometry(QtCore.QRect(180, 50, 71, 22))
        self.Y1.setObjectName(_fromUtf8("Y1"))
        self.Generate = QtGui.QPushButton(self.centralwidget)
        self.Generate.setGeometry(QtCore.QRect(0, 220, 101, 31))
        self.Generate.setObjectName(_fromUtf8("Generate"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 20, 71, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.R1 = QtGui.QLineEdit(self.centralwidget)
        self.R1.setGeometry(QtCore.QRect(330, 50, 71, 22))
        self.R1.setObjectName(_fromUtf8("R1"))
        self.Y2 = QtGui.QLineEdit(self.centralwidget)
        self.Y2.setGeometry(QtCore.QRect(180, 90, 71, 22))
        self.Y2.setObjectName(_fromUtf8("Y2"))
        self.R2 = QtGui.QLineEdit(self.centralwidget)
        self.R2.setGeometry(QtCore.QRect(330, 90, 71, 22))
        self.R2.setObjectName(_fromUtf8("R2"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "X-Co-ordinate", None))
        self.label_3.setText(_translate("MainWindow", "Radii", None))
        self.Generate.setText(_translate("MainWindow", "Generate", None))
        self.label_2.setText(_translate("MainWindow", "Y-Co-ordinate", None))