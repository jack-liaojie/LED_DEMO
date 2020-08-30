# -*- coding: utf-8 -*-
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QListWidgetItem, QWidget, QMessageBox, QApplication
from module.frm_bottom import *
from cls_thread import *

class cod_bottom(QWidget,Ui_Form):
	"""docstring for frm_Top"""
	def __init__(self, arg):
		super(cod_bottom, self).__init__()
		self.arg = arg
		self.setupUi(self)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_login_form = cod_bottom("hell")
    # 显示登陆页面
    my_login_form.show()
    sys.exit(app.exec_())