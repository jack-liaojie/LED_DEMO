# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\2020EQ\CODE\LED\module\frm_bottom.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1365, 262)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_ico_left = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_ico_left.sizePolicy().hasHeightForWidth())
        self.lbl_ico_left.setSizePolicy(sizePolicy)
        self.lbl_ico_left.setText("")
        self.lbl_ico_left.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_ico_left.setObjectName("lbl_ico_left")
        self.horizontalLayout.addWidget(self.lbl_ico_left)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lbl_ico = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_ico.sizePolicy().hasHeightForWidth())
        self.lbl_ico.setSizePolicy(sizePolicy)
        self.lbl_ico.setLineWidth(0)
        self.lbl_ico.setText("")
        self.lbl_ico.setPixmap(QtGui.QPixmap("E:\\2020EQ\\CODE\\LED\\module\\../resource/longines.jpg"))
        self.lbl_ico.setScaledContents(True)
        self.lbl_ico.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_ico.setWordWrap(True)
        self.lbl_ico.setObjectName("lbl_ico")
        self.horizontalLayout.addWidget(self.lbl_ico)
        spacerItem1 = QtWidgets.QSpacerItem(37, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.lbl_ico_right = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_ico_right.sizePolicy().hasHeightForWidth())
        self.lbl_ico_right.setSizePolicy(sizePolicy)
        self.lbl_ico_right.setText("")
        self.lbl_ico_right.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_ico_right.setObjectName("lbl_ico_right")
        self.horizontalLayout.addWidget(self.lbl_ico_right)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
