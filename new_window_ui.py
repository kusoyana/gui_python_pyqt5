# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\study_pyqt5\new_window.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(320, 240)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 180, 321, 41))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.gridLayoutWidget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.subEnrollButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.subEnrollButton.setObjectName("subEnrollButton")
        self.horizontalLayout_5.addWidget(self.subEnrollButton)
        self.subCancelButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.subCancelButton.setObjectName("subCancelButton")
        self.horizontalLayout_5.addWidget(self.subCancelButton)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 321, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.nameLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.nameLabel.setMinimumSize(QtCore.QSize(80, 0))
        self.nameLabel.setObjectName("nameLabel")
        self.horizontalLayout_2.addWidget(self.nameLabel)
        self.nameZLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.nameZLineEdit.setObjectName("nameZLineEdit")
        self.horizontalLayout_2.addWidget(self.nameZLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.furiLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.furiLabel.setMinimumSize(QtCore.QSize(80, 0))
        self.furiLabel.setObjectName("furiLabel")
        self.horizontalLayout_3.addWidget(self.furiLabel)
        self.furiLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.furiLineEdit.setObjectName("furiLineEdit")
        self.horizontalLayout_3.addWidget(self.furiLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.classLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.classLabel.setMinimumSize(QtCore.QSize(80, 0))
        self.classLabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.classLabel.setObjectName("classLabel")
        self.horizontalLayout_4.addWidget(self.classLabel)
        self.classComboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.classComboBox.setCurrentText("")
        self.classComboBox.setIconSize(QtCore.QSize(16, 16))
        self.classComboBox.setObjectName("classComboBox")
        self.horizontalLayout_4.addWidget(self.classComboBox)
        self.classSpinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.classSpinBox.setMinimum(1)
        self.classSpinBox.setMaximum(6)
        self.classSpinBox.setObjectName("classSpinBox")
        self.horizontalLayout_4.addWidget(self.classSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.subEnrollButton.setText(_translate("Dialog", "登録"))
        self.subCancelButton.setText(_translate("Dialog", "キャンセル"))
        self.nameLabel.setText(_translate("Dialog", "名前"))
        self.furiLabel.setText(_translate("Dialog", "フリガナ"))
        self.classLabel.setText(_translate("Dialog", "学年"))

