# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\2020EQ\CODE\LED\module\frm_schedule.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(795, 485)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tbwgt_content = QtWidgets.QTableWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbwgt_content.sizePolicy().hasHeightForWidth())
        self.tbwgt_content.setSizePolicy(sizePolicy)
        self.tbwgt_content.setMinimumSize(QtCore.QSize(300, 300))
        self.tbwgt_content.setMaximumSize(QtCore.QSize(1666666, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.tbwgt_content.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.tbwgt_content.setFont(font)
        self.tbwgt_content.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tbwgt_content.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tbwgt_content.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tbwgt_content.setAutoScroll(False)
        self.tbwgt_content.setTabKeyNavigation(False)
        self.tbwgt_content.setProperty("showDropIndicator", False)
        self.tbwgt_content.setDragDropOverwriteMode(False)
        self.tbwgt_content.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tbwgt_content.setShowGrid(False)
        self.tbwgt_content.setGridStyle(QtCore.Qt.NoPen)
        self.tbwgt_content.setCornerButtonEnabled(False)
        self.tbwgt_content.setRowCount(5)
        self.tbwgt_content.setColumnCount(5)
        self.tbwgt_content.setObjectName("tbwgt_content")
        self.tbwgt_content.horizontalHeader().setVisible(False)
        self.tbwgt_content.horizontalHeader().setCascadingSectionResizes(True)
        self.tbwgt_content.horizontalHeader().setDefaultSectionSize(400)
        self.tbwgt_content.horizontalHeader().setMinimumSectionSize(200)
        self.tbwgt_content.verticalHeader().setVisible(False)
        self.tbwgt_content.verticalHeader().setDefaultSectionSize(200)
        self.tbwgt_content.verticalHeader().setMinimumSectionSize(100)
        self.horizontalLayout.addWidget(self.tbwgt_content)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
