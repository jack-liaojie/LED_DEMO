# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\2020EQ\CODE\LED\module\frm_medal.ui'
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
        self.tbwgt_content = QtWidgets.QTableWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbwgt_content.sizePolicy().hasHeightForWidth())
        self.tbwgt_content.setSizePolicy(sizePolicy)
        self.tbwgt_content.setMinimumSize(QtCore.QSize(300, 300))
        self.tbwgt_content.setMaximumSize(QtCore.QSize(1666666, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(231, 234, 213))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 234, 213))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 234, 213))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 234, 213))
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
        self.tbwgt_content.setWordWrap(False)
        self.tbwgt_content.setCornerButtonEnabled(False)
        self.tbwgt_content.setRowCount(0)
        self.tbwgt_content.setColumnCount(10)
        self.tbwgt_content.setObjectName("tbwgt_content")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        item.setFont(font)
        item.setBackground(QtGui.QColor(231, 234, 213))
        brush = QtGui.QBrush(QtGui.QColor(231, 234, 213))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tbwgt_content.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwgt_content.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwgt_content.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwgt_content.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbwgt_content.setHorizontalHeaderItem(4, item)
        self.tbwgt_content.horizontalHeader().setVisible(False)
        self.tbwgt_content.horizontalHeader().setCascadingSectionResizes(False)
        self.tbwgt_content.horizontalHeader().setDefaultSectionSize(300)
        self.tbwgt_content.horizontalHeader().setHighlightSections(False)
        self.tbwgt_content.horizontalHeader().setMinimumSectionSize(200)
        self.tbwgt_content.horizontalHeader().setStretchLastSection(False)
        self.tbwgt_content.verticalHeader().setVisible(False)
        self.tbwgt_content.verticalHeader().setDefaultSectionSize(200)
        self.tbwgt_content.verticalHeader().setMinimumSectionSize(200)
        self.tbwgt_content.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.tbwgt_content)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tbwgt_content.horizontalHeaderItem(0)
        item.setText(_translate("Form", "新建列"))
        item = self.tbwgt_content.horizontalHeaderItem(1)
        item.setText(_translate("Form", "新建列"))
        item = self.tbwgt_content.horizontalHeaderItem(2)
        item.setText(_translate("Form", "新建列"))
        item = self.tbwgt_content.horizontalHeaderItem(3)
        item.setText(_translate("Form", "新建列"))
        item = self.tbwgt_content.horizontalHeaderItem(4)
        item.setText(_translate("Form", "新建列"))
