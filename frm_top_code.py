# -*- coding: utf-8 -*-
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QListWidgetItem, QWidget, QMessageBox, QApplication
from module.frm_top import *
from cls_thread import *

class cod_top(QWidget,Ui_Form):
	"""docstring for frm_Top"""
	def __init__(self, arg):
		super(cod_top, self).__init__()
		self.lbl_title = arg
		self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_login_form = cod_top("hell")
    # 显示登陆页面
    my_login_form.show()
    sys.exit(app.exec_())