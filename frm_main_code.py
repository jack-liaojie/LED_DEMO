import sys

from PyQt5.QtWidgets import *
import cls_database
from func_json import *
from frm_display_code import cod_display
from module.frm_main import *
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QTableWidget, QVBoxLayout

class cod_main(QWidget, Ui_Form):
	def __init__(self, table_params):
		super(cod_main, self).__init__()
		self.setupUi(self)
		self.table_params = table_params
		self.path="./initialize/config.ini"
		#加载本地数据
		self.load_config()
		self.btn_OK.clicked.connect(self.Ok)
		self.btn_Cancel.clicked.connect(self.Cancel)

	def Cancel(self):
		if QMessageBox.Ok == QMessageBox.information(self, "提示", "确定退出!", QMessageBox.Cancel | QMessageBox.Ok):
			self.save_dictfile()
			self.close()

	def Ok(self):
		self.save_dictfile()
		self.close()
		self.y=cod_display(self)
		self.y.show()

	def save_dictfile(self):
		'''保存设置数据'''
		fileargs ={}
		fileargs['center'] = self.read_table(self.tbwgt_center)
		fileargs['top'] = self.read_table(self.tbwgt_top)
		fileargs['bottom'] = self.read_table(self.tbwgt_bottom)
		write_file(self.path,dict_str(fileargs))

	def read_table(self,tablewidget):
		'''读取配置数据'''
		args={}
		rows = tablewidget.rowCount()
		for row in range(0,rows):
			tag = tablewidget.item(row, 0).text()
			prop = tablewidget.item(row, 1).text()
			args[tag] = prop
		return args


	def load_config(self):
		"""加载配置文件"""
		params = str_dict(read_file(self.path))
		self.get_dict(self.tbwgt_center,params['center'])
		self.get_dict(self.tbwgt_top,params['top'])
		self.get_dict(self.tbwgt_bottom,params['bottom'])
	
	def get_dict(self,tablewidget,tag):
		# 加载数据到表格
		tablewidget.setColumnCount(2)  # 设定列数
		tablewidget.setHorizontalHeaderLabels(['tag','property'])  # 设置表头内容
		i = 0
		for row in tag.items():
			j = 0
			tablewidget.setRowCount(i + 1)
			for cln in row:
				tablewidget.setItem(i, j, QTableWidgetItem(str(cln)))
				j += 1
			i += 1
		self.column = tablewidget.columnCount()
		tablewidget.resizeColumnsToContents()  # 与内容同宽

		
if __name__ == '__main__':
	app = QApplication(sys.argv)
	example = cod_main("hello")
	example.show()
	sys.exit(app.exec_())