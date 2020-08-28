# -*- coding: utf-8 -*-
import sys
import socket
import json
import re

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

		self.F_MatchLongName,self.F_StatusLongName,self.F_MatchID,self.F_PhaseID, \
		self.F_MatchStatusID,self.F_MatchDate,self.F_StartTime,self.F_EndTime,self.f_order, \
		self.F_PhaseID,self.F_PhaseLongName,self.F_StatusID,self.F_EventID,self.F_EventLongName, \
		self.F_DisciplineCode,self.F_DisciplineLongName,self.F_SportID,self.F_SportLongName="","","","","","","","","","","","","","","","","",""

		self.setupUi(self)
		self.load_config()
		self.tbv_register.hide()
		# self.tempform = QWidget
		self.btn_ok.clicked.connect(self.ok)
		self.btn_cancel.clicked.connect(self.cancel)
		self.btn_dbtest.clicked.connect(self.dbtest)
		self.tbv_data.clicked.connect(self.eventselect)
		self.tbv_register.clicked.connect(self.registerselect)

		self.rdo_welcome.clicked.connect(self.welcome)
		self.rdo_judge.clicked.connect(self.welcome)
		self.rdo_schedule.clicked.connect(self.welcome)
		self.rdo_startlist.clicked.connect(self.welcome)
		self.rdo_result.clicked.connect(self.welcome)
		self.rdo_step.clicked.connect(self.welcome)
		self.rdo_resultlist.clicked.connect(self.welcome)
		self.rdo_ranklist.clicked.connect(self.welcome)
		self.rdo_medal.clicked.connect(self.welcome)
		self.rdo_celebrate.clicked.connect(self.welcome)

	def registerselect(self):
		"""成绩运动员选择和步伐选择"""
		row_num = self.tbv_register.selectionModel().currentIndex().row()  # 将选定的行数传递	
		
		if self.rdo_result.isChecked()==True:#运动员选择
			# pass('27-黄伟力', '黄伟力', '飞燕', '四川队', 5, 5, None, 4984, '[Image]四川队', 'Horse: 飞燕')
			self.F_RegisterName=self.tbv_register.item(row_num, 1).text()
			self.F_HorseName=self.tbv_register.item(row_num, 2).text()
			self.F_DelegationName=self.tbv_register.item(row_num, 3).text()
			self.F_RegisterBib=self.tbv_register.item(row_num, 4).text()
			self.F_HorseBib=self.tbv_register.item(row_num, 5).text()
			self.F_CurIRM=self.tbv_register.item(row_num, 6).text()
			self.F_RegisterID=self.tbv_register.item(row_num, 7).text()

			args =	{
						"result":self.F_EventLongName + self.F_MatchLongName,
						"data":self.get_Proc('get_Proc_SCB_EQ_GetDRRiderResult',[self.F_MatchID,self.F_RegisterID,0,'chn']),
						"content":strregex(self.get_Proc('get_Proc_SCB_EQ_GetMatchResultList',[self.F_MatchID,'chn']))
					}#正则表达式Decimal('65.262000000')-->'65.262'

		elif self.rdo_step.isChecked()==True:#步伐选择
			args =	{
						"step":self.F_EventLongName + self.F_MatchLongName,
						"content":self.tbv_register.item(row_num, 1).text()
					}


		self.txt_data.setText(dict_json(args))


	def eventselect(self):
		"""给标题self.tbv_data填充数据"""
		
		# b.F_MatchLongName,e.F_StatusLongName,a.F_MatchID,a.F_PhaseID,a.F_MatchStatusID,a.F_MatchDate,a.F_StartTime,a.F_EndTime,
		# a.f_order,c.F_PhaseID,d.F_PhaseLongName,e.F_StatusID,
		# f.F_EventID,g.F_EventLongName,h.F_DisciplineCode,j.F_DisciplineLongName,k.F_SportID,l.F_SportLongName
		# ('资格赛', 'Startlist', 1, 1, 40, datetime.datetime(2014, 6, 27, 0, 0), datetime.datetime(2014, 6, 23, 9, 0), 
		# None, 1, 1, '资格赛', 40, 1, '盛装舞步个人赛', 'EQ', '马术',
		# 1, '宝骏汽车2014年全国马术盛装舞步锦标赛'),
		if self.ckb_matchselected.isChecked() == False:
			row_num = self.tbv_data.selectionModel().currentIndex().row()  # 将选定的行数传递
			self.F_MatchLongName = self.tbv_data.item(row_num, 0).text()
			self.F_StatusLongName = self.tbv_data.item(row_num, 1).text()
			self.F_MatchID = self.tbv_data.item(row_num, 2).text()
			self.F_PhaseID = self.tbv_data.item(row_num, 3).text()
			self.F_MatchStatusID = self.tbv_data.item(row_num, 4).text()
			self.F_MatchDate = self.tbv_data.item(row_num, 5).text()
			self.F_StartTime = self.tbv_data.item(row_num, 6).text()
			self.F_EndTime = self.tbv_data.item(row_num, 7).text()
			self.f_order = self.tbv_data.item(row_num, 8).text()
			self.F_PhaseID = self.tbv_data.item(row_num, 9).text()
			self.F_PhaseLongName = self.tbv_data.item(row_num, 10).text()
			self.F_StatusID = self.tbv_data.item(row_num, 11).text()
			self.F_EventID = self.tbv_data.item(row_num, 12).text()
			self.F_EventLongName = self.tbv_data.item(row_num, 13).text()
			self.F_DisciplineCode = self.tbv_data.item(row_num, 14).text()
			self.F_DisciplineLongName = self.tbv_data.item(row_num, 15).text()
			self.F_SportID = self.tbv_data.item(row_num, 16).text()
			self.F_SportLongName = self.tbv_data.item(row_num, 17).text()
			for x in range(0,18):
				print(str(x) + "--",self.tbv_data.item(row_num, x).text())
			self.tbv_title.setColumnCount(6)  # 设定列数
			self.tbv_title.setRowCount(1)
			self.tbv_title.setItem(0, 0, QTableWidgetItem(self.F_MatchLongName))
			self.tbv_title.setItem(0, 1, QTableWidgetItem(self.F_StatusLongName))
			self.tbv_title.setItem(0, 2, QTableWidgetItem(self.F_PhaseLongName))
			self.tbv_title.setItem(0, 3, QTableWidgetItem(self.F_EventLongName))
			self.tbv_title.setItem(0, 4, QTableWidgetItem(self.F_DisciplineLongName))
			self.tbv_title.setItem(0, 5, QTableWidgetItem(self.F_SportLongName))
			self.tbv_title.resizeRowsToContents()  # 设置行列高宽与内容匹配


	def dbtest(self):
		pass

	def get_Proc(self,proname,params):

		# agrs = {"dbserver":self.db_ip,"dbport":self.db_port,"dbuser":db_user,"dbpwd":self.db_pwd,"dbdatabase":self.db_database}

		x = get_Results(self.conn)
		y = x.do(proname,params)
		return y


	def load_config(self):
		ini_path="./initialize/led.ini"
		ini_args = str_dict(read_file(ini_path))
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
		self.trv_event.clicked.connect( self.trv_event_Clicked )


		self.read_config()

		self.set_eventinfo()


	def read_config(self):
		"""加载数据库设置"""
		self.conn = {"dbserver":self.txt_dbip.text(),"dbport":self.txt_dbport.text(),"dbuser":self.txt_dbuser.text(), 
		"dbpwd":self.txt_dbpwd.text(),"dbdatabase":self.txt_dbdatabase.text()}
		
	def trv_event_Clicked(self,args):
		"""树列表点击"""
		item = self.trv_event.currentItem()
		if item.text(0) == "root": return
		self.read_SQLresults(self.tbv_data,'get_Proc_SCB_EQ_GetMatchInfo_LJ',[item.text(0),'chn'])


	def ok(self):
		if QMessageBox.Ok == QMessageBox.information(self, "提示", "确定发送!", QMessageBox.Cancel | QMessageBox.Ok):
			self.senddata(self.txt_data.toPlainText())

	def cancel(self):
		if QMessageBox.Ok == QMessageBox.information(self, "提示", "确定退出!", QMessageBox.Cancel | QMessageBox.Ok):
			self.close()
			
	def welcome(self):
				# args =	{
		# 		"schedule":{"title":"盛装舞步预赛"},
		# 		"content":
		# 			[
		# 				{"time":"10:00","sport":"盛装舞步","event":"资格赛"},
		# 				{"time":"11:00","sport":"盛装舞步","event":"资格赛"},
		# 				{"time":"12:00","sport":"盛装舞步","event":"资格赛"}
		# 			]
		# 	}
		args = ""

		self.tbv_register.clear()
		self.tbv_register.hide()
		if self.F_MatchLongName != "" and self.rdo_welcome.isChecked() == True:
			args =	{
					"welcome":self.F_SportLongName,
					"content":self.F_EventLongName + self.F_MatchLongName
				}

		if self.F_MatchLongName != "" and self.rdo_celebrate.isChecked() == True:
			args =	{
					"celebrate":self.F_SportLongName,
					"content":self.F_EventLongName + self.F_MatchLongName
				}

		elif self.F_MatchLongName != "" and self.rdo_schedule.isChecked() == True:
			args =	{
					"schedule":"竞赛日程",
					"content":self.get_Proc('get_Proc_SCB_EQ_GetSchedule',['all','chn'])
				}

		elif self.F_MatchLongName != "" and self.rdo_judge.isChecked() == True:
			args =	{
					"judge":self.F_EventLongName + self.F_MatchLongName + "竞赛裁判",
					"content":self.get_Proc('get_Proc_SCB_EQ_GetJudgeList',[self.F_MatchID,'chn'])
				}

		elif self.F_MatchLongName != "" and self.rdo_step.isChecked() == True:
			self.tbv_register.show()
			self.read_SQLresults(self.tbv_register,'get_Proc_SCB_EQ_GetMatchMovementList',[self.F_MatchID,'chn'])



		elif self.F_MatchLongName != "" and self.rdo_startlist.isChecked() == True:
			args =	{
					"startlist":self.F_EventLongName + self.F_MatchLongName,
					"content":self.get_Proc('get_Proc_SCB_EQ_GetStartList',[self.F_MatchID,'chn'])
				}

		elif self.F_EventLongName != "" and self.rdo_medal.isChecked() == True:
			args =	{
					"medal":self.F_EventLongName,
					"content":self.get_Proc('get_Proc_SCB_EQ_GetMedalList',[self.F_EventID,'chn'])
				}

		elif self.F_EventLongName != "" and self.rdo_ranklist.isChecked() == True:
			args =	{
					"ranklist":self.F_EventLongName,
					"content":self.get_Proc('get_Proc_SCB_EQ_GetMedalList',[self.F_EventID,'chn'])
				}

		elif self.F_MatchLongName != "" and self.rdo_result.isChecked() == True:
			self.tbv_register.show()

			# args =	{
			# 		"Start":self.F_EventLongName + self.F_MatchLongName,
			# 		"content":self.get_Proc('get_Proc_SCB_EQ_GetMatchRegisterList',[self.F_MatchID,'chn'])
			# 	}
			self.read_SQLresults(self.tbv_register,'get_Proc_SCB_EQ_GetMatchRegisterList',[self.F_MatchID,'chn'])

				

		elif self.F_MatchLongName != "" and self.rdo_resultlist.isChecked() == True:
			args =	{
					"r_list":self.F_EventLongName + self.F_MatchLongName,
					# 通过正则表达式将decimal类型转为字符
					# 例如：Decimal('65.262000000')转为'65.262'
					"content":strregex(self.get_Proc('get_Proc_SCB_EQ_GetMatchResultList',[self.F_MatchID,'chn']))
				}

		self.txt_data.setText(dict_json(args))


	def senddata(self,args):

		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		# s.connect((self.udp_ip, int(self.udp_port)))
		# s.send(str(args).encode('utf-8'))
		# s.sendall(str(args).encode('utf-8'))
		s.sendto(str(args).encode('utf-8'), (self.udp_ip, int(self.udp_port)))
		# s.close()

	def set_eventinfo(self):
		# 设置列数
		self.trv_event.setColumnCount(2)
        # 设置头的标题
		self.trv_event.setHeaderLabels(['Key','Value'])
		root= QTreeWidgetItem(self.trv_event)
		root.setText(0,'root')
		
		x = get_Results(self.conn)
		results = y = x.do_field('get_Proc_SCB_GetEvents', ['eq'])
		for row in results['results']:
			item = self.trv_event.currentItem()
			node = QTreeWidgetItem(item)
			node.setText(0,str(row[2]))
			node.setText(1,row[1])	
			root.addChild(node)
		self.trv_event.addTopLevelItem(root)
		self.trv_event.expandAll()


	def read_SQLresults(self, tablewidget, operate_name, params):
		"""
		加载赛事信息到tbv_data
		:return:
		"""
		x = get_Results(self.conn)
		results = x.do_field(operate_name, params)
		tablewidget.setColumnCount(len(results['desc']))  # 设定列数
		tablewidget.setHorizontalHeaderLabels(results['desc'])  # 设置表头内容
		# 加载数据到表格
		i = 0
		for row in results['results']:
			j = 0
			tablewidget.setRowCount(i + 1)
			for cln in row:
				tablewidget.setItem(i, j, QTableWidgetItem(str(cln)))
				j += 1
			i += 1
		self.column = tablewidget.columnCount()
		# tablewidget.resizeRowsToContents()  # 设置行列高宽与内容匹配
		tablewidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)



if __name__ == '__main__':
	app = QApplication(sys.argv)
	example = cod_led("hello")
	example.show()
	sys.exit(app.exec_())