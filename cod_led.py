# -*- coding: utf-8 -*-
import sys
import socket
import json
from func_json import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from module.frm_led import * 
from cls_database import * 

class cod_led(QMainWindow,Ui_MainWindow):
	def __init__(self, arg):
		super(cod_led, self).__init__()
		self.ini_path = ''
		self.arg = arg
		self.setupUi(self)
		self.load_config()
		self.tempform = QWidget
		self.btn_ok.clicked.connect(self.ok)
		self.btn_cancel.clicked.connect(self.cancel)
		# self.rdo_welcome.clicked.connect(self.welcome)
		# self.rdo_judge.clicked.connect(self.judge)
		# self.rdo_schedule.clicked.connect(self.schedule)
		# self.rdo_startlist.clicked.connect(self.startlist)
		# self.rdo_result.clicked.connect(self.result)
		# self.rdo_step.clicked.connect(self.step)
		# self.rdo_resultlist.clicked.connect(self.resultlist)
		# self.rdo_ranklist.clicked.connect(self.ranklist)
		# self.rdo_medal.clicked.connect(self.medal)
		# self.rdo_celebrate.clicked.connect(self.celebrate)
 
	def load_config(self):
		ini_path="./initialize/led.ini"
		ini_args = read_file(ini_path)
		self.udp_ip = ini_args['udp_ip']
		self.udp_port = ini_args['udp_port']
		self.udp_port = ini_args['udp_port']
		self.db_ip = ini_args['db_ip']
		self.db_port = ini_args['db_port']
		self.db_user = ini_args['db_user']
		self.db_pwd = ini_args['db_pwd']
		self.db_database = ini_args['db_database']
		self.txt_ip.setText(self.udp_ip)
		self.txt_port.setText(self.udp_port)
		self.txt_dbip.setText(self.db_ip)
		self.txt_dbport.setText(self.db_port)
		self.txt_dbuser.setText(self.db_user)
		self.txt_dbpwd.setText(self.db_pwd)
		self.txt_dbdatabase.setText(self.db_database)

	def ok(self):
		if QMessageBox.Ok == QMessageBox.information(self, "提示", "确定发送!", QMessageBox.Cancel | QMessageBox.Ok):
			self.senddata()

	def cancel(self):
		if QMessageBox.Ok == QMessageBox.information(self, "提示", "确定退出!", QMessageBox.Cancel | QMessageBox.Ok):
			self.close()
	
	def senddata(self):
		# args =	{
		# 		"schedule":{"title":"盛装舞步预赛"},
		# 		"content":
		# 			[
		# 				{"time":"10:00","sport":"盛装舞步","event":"资格赛"},
		# 				{"time":"11:00","sport":"盛装舞步","event":"资格赛"},
		# 				{"time":"12:00","sport":"盛装舞步","event":"资格赛"}
		# 			]
		# 	}
		args =	{
				"welcome":{"title":"盛装舞步预赛"},
				"content":{"name":"welcome to Equestrain festivate"}
			}

		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.sendto(str(args).encode('utf-8'), (self.udp_ip, int(self.udp_port)))
		s.close()
		print("true")

	def get_db():
		x = get_Results(args)
		y = x.do_field('get_venuelist', ['1'])
  
		pass
if __name__ == '__main__':
	app = QApplication(sys.argv)
	example = cod_led("hello")
	example.show()
	sys.exit(app.exec_())