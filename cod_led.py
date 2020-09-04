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
		self.ckb_five.clicked.connect(self.fivestart)
		self.ckb_twenty.clicked.connect(self.twentystart)
		self.ckb_scrolling.clicked.connect(self.scrolling)
	
	def scrolling(self):
		if self.ckb_scrolling.isChecked :self.ckb_scrolling.isChecked =False
		args =	{
					"scrolling":"scrolling"
				}
		x = dict_json(args)
		self.txt_data.setText(x)
		self.senddata(x)

	def fivestart(self):
		if self.ckb_twenty.isChecked :self.ckb_twenty.isChecked =False
		args =	{
					"fivestart":"fivestart"
				}
		x = dict_json(args)
		self.txt_data.setText(x)
		self.senddata(x)

	def twentystart(self):
		if self.ckb_five.isChecked :self.ckb_five.isChecked =False

		args =	{
					"twentystart":"twentystart"
				}
		x = dict_json(args)
		self.txt_data.setText(x)
		self.senddata(x)

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
		# if QMessageBox.Ok == QMessageBox.information(self, "提示", "确定发送!", QMessageBox.Cancel | QMessageBox.Ok):
		self.senddata(self.txt_data.toPlainText())

	def cancel(self):
		# if QMessageBox.Ok == QMessageBox.information(self, "提示", "确定退出!", QMessageBox.Cancel | QMessageBox.Ok):
		self.close()
			
	def welcome(self):
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
					"k_list":self.F_EventLongName,
					"content":strregex(self.get_Proc('get_Proc_SCB_EQ_GetMatchResultList',[self.F_MatchID,'chn']))
					# "content":self.get_Proc('get_Proc_SCB_EQ_GetMedalList',[self.F_EventID,'chn'])
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



#------------------------------------------------------------------------------------UDP控制系统
import datetime
import uuid
def generateUUID():
    id = uuid.uuid1()	# 还有uuid2、uuid3、uuid4、uuid5等其他方法
    return id


class mobilemessage(object):
	"""docstring for mobilemessage"""
	def __init__(self, arg):
		super(mobilemessage, self).__init__()
		self.arg = arg
		self.receive(self.arg)

	def receive(self,arg):

		if (self.arg["Key"] == "C8kPeuWjMxOqm4Ca" and self.arg["MessageType"] == "Welcome"):
			# a = {
			#   "Key": "C8kPeuWjMxOqm4Ca",
			#   "ClientID": "client1",
			#   "MessageType": "Welcome",
			#   "MessageID": "b981cbdd-341a-4275-bdc5-e2dcf4f0bd40",
			#   "Timestamp": "2020-08-31 20:21:59.059"
			# }
			# {
			#   "RequestMessageID": "a5f1a2c3-0c73-4906-95f1-8ba229675b4a",
			#   "Status": "Success",
			#   "Message": "XXX成功",
			#   "MessageType": "CelebrateResponse",
			#   "MessageID": "79192a32-c6b9-44f4-8982-87c7283680b8",
			#   "Timestamp": "2020-09-01 13:26:05.973"
			# }
			response = {}
			response["RequestMessageID"]=self.arg["MessageID"]
			response["MessageType"]="WelcomeResponse"
			response["Timestamp"]= datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%3f')[:-3]  # 2019-01-28 11:09:01.529
			response["MessageID"]= generateUUID()
			response["Message"]= "欢迎屏成功"
			response["Status"]= "Success"
			sendmessage(response)

		elif (self.arg["Key"] == "C8kPeuWjMxOqm4Ca" and self.arg['MessageType'] == "Judge"):
		# {
		#   "Key": "C8kPeuWjMxOqm4Ca",
		#   "ClientID": "client1",
		#   "MessageType": "Judge",
		#   "MessageID": "8a3a979a-9194-40f0-a372-15f9dc248411",
		#   "Timestamp": "2020-09-01 13:26:11.806"
		# }
		# {
		#   "RequestMessageID": "1f37b3ae-a91d-434d-b96a-9e3d63174085",
		#   "Status": "Success",
		#   "Message": "XXX成功",
		#   "MessageType": "JudgeResponse",
		#   "MessageID": "822ba200-67bb-4fee-acf1-f4f36cb12954",
		#   "Timestamp": "2020-09-01 13:26:06.128"
		# }
			pass
			
		elif (self.arg["Key"] == "C8kPeuWjMxOqm4Ca" and self.arg['MessageType'] == "HeartBeat"):#心跳
		# {
		#   "Data": {
		#     "TimerInfos": {
		#       "1": {
		#         "TimerNumber": 1,
		#         "IsIncrease": true,
		#         "IsRunning": false,
		#         "IsDisplay": true,
		#         "TotalTime": "00:05"
		#       },
		#       "2": {
		#         "TimerNumber": 1,
		#         "IsIncrease": false,
		#         "IsRunning": false,
		#         "IsDisplay": true,
		#         "TotalTime": "00:05"
		#       }
		#     },
		#     "Title": "盛装舞步个人赛预赛",
		#     "CurrentScreen": "StartList"
		#   },
		#   "RequestMessageID": "6fe9a19f-aaf5-4220-adca-358995b2eebb",
		#   "Status": "Success",
		#   "Message": "XXX成功",
		#   "MessageType": "HeartBeatResponse",
		#   "MessageID": "195fe6e4-c257-43aa-bbb2-f92aaa162205",
		#   "Timestamp": "2020-09-01 13:26:06.080"
		# }

		# {
		# "Data": {
		# "Battery": 88,
		# "ReceivePort": 4000,
		# "Version": "1.0"
		# },
		# "ClientID": "client1",
		# "MessageType": "HeartBeat",
		# "MessageID": "80b15a9a-7693-4f29-86df-67e982417591",
		# "Timestamp": "2020-09-01 13:26:11.820"
		# }
			pass
			
		elif (self.arg["Key"] == "C8kPeuWjMxOqm4Ca" and self.arg['MessageType'] == "Celebrate"):
		# {
		#   "Key": "C8kPeuWjMxOqm4Ca",
		#   "ClientID": "client1",
		#   "MessageType": "Celebrate",
		#   "MessageID": "c569558e-8373-403e-bf06-22586b709eea",
		#   "Timestamp": "2020-09-01 13:26:11.817"
		# }
			pass
			
		elif (self.arg["Key"] == "C8kPeuWjMxOqm4Ca" and self.arg['MessageType'] == "MatchNext"):
		# {
		#   "Key": "C8kPeuWjMxOqm4Ca",
		#   "ClientID": "client1",
		#   "MessageType": "MatchNext",
		#   "MessageID": "8b796e33-da9e-47b7-9678-aa41f6e6478a",
		#   "Timestamp": "2020-09-01 13:26:11.826"
		# }

		# {
		#   "Data": {
		#     "Title": "盛装舞步个人赛预赛"
		#   },
		#   "RequestMessageID": "57a53646-2057-4296-bebc-200219cdf7c9",
		#   "Status": "Success",
		#   "Message": "XXX成功",
		#   "MessageType": "MatchNextResponse",
		#   "MessageID": "78a64be8-ef48-4d89-b582-2888eafdb535",
		#   "Timestamp": "2020-09-01 13:26:06.131"
		# }
			pass
			
		elif (self.arg["Key"] == "C8kPeuWjMxOqm4Ca" and self.arg['MessageType'] == "Medal"):
		# {
		#   "Key": "C8kPeuWjMxOqm4Ca",
		#   "ClientID": "client1",
		#   "MessageType": "Medal",
		#   "MessageID": "34fe5672-483a-4cb3-86cd-ce81ab408c87",
		#   "Timestamp": "2020-09-01 13:26:11.808"
		# }
		# {
		#   "RequestMessageID": "5adb26ed-b903-4560-a8e6-6c96e1128287",
		#   "Status": "Success",
		#   "Message": "XXX成功",
		#   "MessageType": "MedalResponse",
		#   "MessageID": "db5a3b1e-32d4-4bd1-bd97-cbb0f35b8498",
		#   "Timestamp": "2020-09-01 13:26:06.137"
		# }
			pass
			
		elif (self.arg["Key"] == "C8kPeuWjMxOqm4Ca" and self.arg['MessageType'] == "MatchPrevious"):
		# {
		#   "Key": "C8kPeuWjMxOqm4Ca",
		#   "ClientID": "client1",
		#   "MessageType": "MatchPrevious",
		#   "MessageID": "886bc405-9a75-478b-a201-da63e1dc473d",
		#   "Timestamp": "2020-09-01 13:26:11.841"
		# }
		# {
		#   "Data": {
		#     "Title": "盛装舞步个人赛预赛"
		#   },
		#   "RequestMessageID": "c147bfa5-793e-4797-aec5-9ffc0c3423f5",
		#   "Status": "Success",
		#   "Message": "XXX成功",
		#   "MessageType": "MatchPreviousResponse",
		#   "MessageID": "62efaf0a-6f94-4360-bd86-ed850cc285eb",
		#   "Timestamp": "2020-09-01 13:26:06.135"
		# }
			pass
			
		elif (self.arg["Key"] == "C8kPeuWjMxOqm4Ca" and self.arg['MessageType'] == "RankList"):
		# {
		#   "Key": "C8kPeuWjMxOqm4Ca",
		#   "ClientID": "client1",
		#   "MessageType": "RankList",
		#   "MessageID": "ca472bd6-22af-4e64-9aa7-4a6e18d8a6cc",
		#   "Timestamp": "2020-09-01 13:26:11.813"
		# }
			pass
			
		elif (self.arg["Key"] == "C8kPeuWjMxOqm4Ca" and self.arg['MessageType'] == "Result"):
		# {
		#   "Key": "C8kPeuWjMxOqm4Ca",
		#   "ClientID": "client1",
		#   "MessageType": "Result",
		#   "MessageID": "c6d11c3b-1dde-43fa-8fea-dc449391ffc6",
		#   "Timestamp": "2020-09-01 13:26:11.810"
		# }
		# {
		#   "RequestMessageID": "db287f37-094b-4e56-94d3-f482680ae0a0",
		#   "Status": "Success",
		#   "Message": "XXX成功",
		#   "MessageType": "ResultResponse",
		#   "MessageID": "86db966e-b087-4724-889f-396e8541cd1f",
		#   "Timestamp": "2020-09-01 13:26:06.143"
		# }

			pass
			
		elif (self.arg["Key"] == "C8kPeuWjMxOqm4Ca" and self.arg['MessageType'] == "ResultList"):
		# {
		#   "Key": "C8kPeuWjMxOqm4Ca",
		#   "ClientID": "client1",
		#   "MessageType": "ResultList",
		#   "MessageID": "05f940e4-179e-4925-806b-99909355160d",
		#   "Timestamp": "2020-09-01 13:26:11.832"
		# }
		# {
		#   "RequestMessageID": "1a91b2c3-ecc0-4751-b0cc-a203afda91a2",
		#   "Status": "Success",
		#   "Message": "XXX成功",
		#   "MessageType": "ResultListResponse",
		#   "MessageID": "45b91f3e-5f7e-4442-b346-3d40132433b8",
		#   "Timestamp": "2020-09-01 13:26:06.141"
		# }
			pass
			
		elif (self.arg["Key"] == "C8kPeuWjMxOqm4Ca" and self.arg['MessageType'] == "Schedule"):
		# {
		#   "Key": "C8kPeuWjMxOqm4Ca",
		#   "ClientID": "client1",
		#   "MessageType": "Schedule",
		#   "MessageID": "db55fc49-9c1e-4289-b872-c782c2e81a84",
		#   "Timestamp": "2020-09-01 13:26:11.815"
		# }
		# {
		#   "RequestMessageID": "7fc71213-ebeb-4550-9453-aabeb97a3f34",
		#   "Status": "Success",
		#   "Message": "XXX成功",
		#   "MessageType": "ScheduleResponse",
		#   "MessageID": "58b554ad-94fb-41b7-b49c-f48b9254cd6b",
		#   "Timestamp": "2020-09-01 13:26:06.145"
		# }
			pass
						
		elif (self.arg["Key"] == "C8kPeuWjMxOqm4Ca" and self.arg['MessageType'] == "StartList"):
		# {
		#   "Key": "C8kPeuWjMxOqm4Ca",
		#   "ClientID": "client1",
		#   "MessageType": "StartList",
		#   "MessageID": "a0e78c76-3227-4161-825b-51c0334f45f8",
		#   "Timestamp": "2020-09-01 13:26:11.827"
		# }
		# {
		#   "RequestMessageID": "cc11c006-55af-4a9f-8b74-6d4e4f6929d9",
		#   "Status": "Success",
		#   "Message": "XXX成功",
		#   "MessageType": "StartListResponse",
		#   "MessageID": "557031fd-1a09-464a-9864-0bf7874bb6b9",
		#   "Timestamp": "2020-09-01 13:26:06.147"
		# }
			pass
						
		elif (self.arg["Key"] == "C8kPeuWjMxOqm4Ca" and self.arg['MessageType'] == "Step"):
		# {
		#   "Key": "C8kPeuWjMxOqm4Ca",
		#   "ClientID": "client1",
		#   "MessageType": "Step",
		#   "MessageID": "73823223-f028-4c9c-b66f-9e7c118309c4",
		#   "Timestamp": "2020-09-01 13:26:11.713"
		# }
		# {
		#   "RequestMessageID": "48a42d3f-dca0-4c5b-b686-f550860bbf3a",
		#   "Status": "Success",
		#   "Message": "XXX成功",
		#   "MessageType": "StepResponse",
		#   "MessageID": "28d627b5-c960-459a-9d4b-edd9c5b44f40",
		#   "Timestamp": "2020-09-01 13:26:06.149"
		# }
			pass
						
		elif (self.arg["Key"] == "C8kPeuWjMxOqm4Ca" and self.arg['MessageType'] == "TimerHide"):
		# {
		#   "Data": {
		#     "TimerNumber": 1
		#   },
		#   "Key": "C8kPeuWjMxOqm4Ca",
		#   "ClientID": "client1",
		#   "MessageType": "TimerHide",
		#   "MessageID": "7f7ed859-1ff4-47de-adcd-259c082e8197",
		#   "Timestamp": "2020-09-01 13:26:11.830"
		# }
		# {
		#   "Data": {
		#     "TimerNumber": 1
		#   },
		#   "RequestMessageID": "3fce1ac0-385f-4764-8c61-4fcb6b0b0a75",
		#   "Status": "Success",
		#   "Message": "XXX成功",
		#   "MessageType": "TimerHideResponse",
		#   "MessageID": "39bcbfbd-8b13-47a7-a6c1-f2ab5ad1aefe",
		#   "Timestamp": "2020-09-01 13:26:06.154"
		# }
			pass
						
		elif (self.arg["Key"] == "C8kPeuWjMxOqm4Ca" and self.arg['MessageType'] == "TimerDisplay"):
		# {
		#   "Data": {
		#     "TimerNumber": 1
		#   },
		#   "Key": "C8kPeuWjMxOqm4Ca",
		#   "ClientID": "client1",
		#   "MessageType": "TimerDisplay",
		#   "MessageID": "e1843fa3-4162-49f9-8c8b-ecb1e1fb5a08",
		#   "Timestamp": "2020-09-01 13:26:11.839"
		# }
		# {
		#   "Data": {
		#     "TimerNumber": 1
		#   },
		#   "RequestMessageID": "b55427a8-c6f5-4911-a752-60ab13061553",
		#   "Status": "Success",
		#   "Message": "XXX成功",
		#   "MessageType": "TimerDisplayResponse",
		#   "MessageID": "63b01b47-de58-4297-b2aa-13803df9f8da",
		#   "Timestamp": "2020-09-01 13:26:06.152"
		# }
			pass
						
		elif (self.arg["Key"] == "C8kPeuWjMxOqm4Ca" and self.arg['MessageType'] == "TimerPause"):
		# {
		#   "Data": {
		#     "TimerNumber": 1
		#   },
		#   "Key": "C8kPeuWjMxOqm4Ca",
		#   "ClientID": "client1",
		#   "MessageType": "TimerPause",
		#   "MessageID": "78bf00a0-b0eb-40a4-8426-dd2e747899ae",
		#   "Timestamp": "2020-09-01 13:26:11.834"
		# }
		# {
		#   "RequestMessageID": "640e8318-b29c-4e50-8320-ddb1e1628037",
		#   "Status": "Success",
		#   "Message": "XXX成功",
		#   "MessageType": "TimerPauseResponse",
		#   "MessageID": "28790179-6f3a-4de9-8f32-edfb36fd64a3",
		#   "Timestamp": "2020-09-01 13:26:06.160"
		# }
			pass
						
		elif (self.arg["Key"] == "C8kPeuWjMxOqm4Ca" and self.arg['MessageType'] == "TimerPauseForAppResponse"):
		# {
		#   "RequestMessageID": "5f2a4bed-851c-4eb7-81cc-af7c46a67018",
		#   "Status": "Success",
		#   "Message": "XXX成功",
		#   "Data": {
		#     "TimerNumber": 1
		#   },
		#   "Key": "C8kPeuWjMxOqm4Ca",
		#   "ClientID": "client1",
		#   "MessageType": "TimerPauseForAppResponse",
		#   "MessageID": "5a323631-b467-4a08-81e8-9d4aab8d1bd9",
		#   "Timestamp": "2020-09-01 13:26:11.843"
		# }
		# {
		#   "Data": {
		#     "CurrentTime": "00:03:56.246",
		#     "TimerNumber": 1
		#   },
		#   "MessageType": "TimerPauseForApp",
		#   "MessageID": "c7ecd33e-f0d4-456b-87c7-91787ad77934",
		#   "Timestamp": "2020-09-01 13:26:06.157"
		# }
			pass
						
		elif (self.arg["Key"] == "C8kPeuWjMxOqm4Ca" and self.arg['MessageType'] == "TimerReset"):
		# {
		#   "Data": {
		#     "TimerNumber": 1
		#   },
		#   "Key": "C8kPeuWjMxOqm4Ca",
		#   "ClientID": "client1",
		#   "MessageType": "TimerReset",
		#   "MessageID": "cee6099f-7b05-4c23-bae8-6adef3f458b9",
		#   "Timestamp": "2020-09-01 13:26:11.836"
		# }
		# {
		#   "RequestMessageID": "fba47535-e407-45a5-a4f2-6b654ade42f9",
		#   "Status": "Success",
		#   "Message": "XXX成功",
		#   "MessageType": "TimerResetResponse",
		#   "MessageID": "d992d57e-e228-430d-b5f8-34a9addb6c9d",
		#   "Timestamp": "2020-09-01 13:26:06.163"
		# }
			pass
						
		elif (self.arg["Key"] == "C8kPeuWjMxOqm4Ca" and self.arg['MessageType'] == "TimerResetForAppResponse"):
		# {
		#   "RequestMessageID": "349d1ea7-27d6-4b24-bdc4-ff27ec0b5d67",
		#   "Status": "Success",
		#   "Message": "XXX成功",
		#   "Data": {
		#     "TimerNumber": 1
		#   },
		#   "Key": "C8kPeuWjMxOqm4Ca",
		#   "ClientID": "client1",
		#   "MessageType": "TimerResetForAppResponse",
		#   "MessageID": "921fa705-ba7f-400a-ad87-2e7acbeaf628",
		#   "Timestamp": "2020-09-01 13:26:11.846"
		# }

		# {
		#   "Data": {
		#     "CurrentTime": "00:05",
		#     "TimerNumber": 1
		#   },
		#   "MessageType": "TimerResetForApp",
		#   "MessageID": "6844fa41-0c15-47d6-8837-3474de2b4d12",
		#   "Timestamp": "2020-09-01 13:26:06.161"
		# }
			pass
						
		elif (self.arg["Key"] == "C8kPeuWjMxOqm4Ca" and self.arg['MessageType'] == "TimerStart"):
		# {
		#   "Data": {
		#     "TimerNumber": 1
		#   },
		#   "Key": "C8kPeuWjMxOqm4Ca",
		#   "ClientID": "client1",
		#   "MessageType": "TimerStart",
		#   "MessageID": "ef58fbf7-cc94-46ee-b408-801606dc0365",
		#   "Timestamp": "2020-09-01 13:26:11.837"
		# }
		# {
		#   "RequestMessageID": "5b7c1259-12af-41ad-8a64-de981b4e3772",
		#   "Status": "Success",
		#   "Message": "XXX成功",
		#   "MessageType": "TimerStartResponse",
		#   "MessageID": "d6607e6d-2571-453b-a152-42ff2ba1b4bd",
		#   "Timestamp": "2020-09-01 13:26:06.169"
		# }
			pass
						
		elif (self.arg["Key"] == "C8kPeuWjMxOqm4Ca" and self.arg['MessageType'] == "TimerStartForAppResponse"):
		# {
		#   "RequestMessageID": "54957d69-d424-480c-a614-38ccba273fba",
		#   "Status": "Success",
		#   "Message": "XXX成功",
		#   "Data": {
		#     "TimerNumber": 1
		#   },
		#   "Key": "C8kPeuWjMxOqm4Ca",
		#   "ClientID": "client1",
		#   "MessageType": "TimerStartForAppResponse",
		#   "MessageID": "c637ff42-5afb-49d7-bf21-1ae58c5dd802",
		#   "Timestamp": "2020-09-01 13:26:11.848"
		# }

		# {
		#   "Data": {
		#     "CurrentTime": "00:04:26.246",
		#     "TimerNumber": 1,
		#     "IsIncrease": true,
		#     "IsRunning": false,
		#     "IsDisplay": true,
		#     "TotalTime": "00:05"
		#   },
		#   "MessageType": "TimerStartForApp",
		#   "MessageID": "70376b6e-2860-4681-b0ed-372a53913c65",
		#   "Timestamp": "2020-09-01 13:26:06.166"
		# }

			pass
						
	
	def sendmessage(self,arg):
		server.sendto(arg.encode('utf-8'), addr)
		
		# self.start_udp((self.udp_ip,int(self.udp_port)),datapath)

	def start_udp(self,arg,path="./initialize/data.ini"):
		global server
		try:
			u_thread = UDPThread()
			server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			# 绑定 客户端口和地址:
			server.bind(arg)

			u_thread.sinOut.connect(self.load_data)
			u_thread.start()
			
		except IOError as identifier:
			u_thread.finished
		finally:
			self.udp_stop

	def udp_stop():
		global server
		global datapath
		u_thread.flag = False
		server.close()
		server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			

class UDPThread(QThread):
	"""线程类用于接收UDP（手机端或控制电脑的操作指令）"""
	sinOut = pyqtSignal(str)

	def __init__(self):
		super(UDPThread, self).__init__()
		self.flag = True
	
	def __del__(self):
		self.flag = False
		self.wait()

	def run(self): 
		global server
		global datapath
		global udpconn

		while self.flag == True:
			try:
				data, addr = server.recvfrom(10240) #1024是接收字节 # resultlist 是关键字出现就报错
				# data = server.recv(10024) #1024是接收字节
				sx = str(data.decode('utf-8'))
				server.sendto("ok".encode('utf-8'), addr)
				server.close()
			except WindowsError as identifier:
				sx = str(data.decode('utf-8'))#读出发送的json字符串数据
				server.close()
				server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
				# 绑定 客户端口和地址:
				server.bind(udpconn)
			finally:
				write_file(datapath,sx) #先将数据存储到本地
				time.sleep(0.99)
				self.sinOut.emit(sx)#发送数据到处理程序



if __name__ == '__main__':
	app = QApplication(sys.argv)
	example = cod_led("hello")
	example.show()
	sys.exit(app.exec_())