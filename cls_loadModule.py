# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Develop\0_PYTHON\projects\vscode_py\qt5designer\a.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import *
from module.frm_schedule import Ui_Form as a
from module.frm_result import Ui_Form as b
from module.frm_judge import Ui_Form as c
from module.frm_resultlist import Ui_Form as d
from module.frm_startlist import Ui_Form as e
from module.frm_welcome import Ui_Form as f
from module.frm_ranklist import Ui_Form as g
from module.frm_medal import Ui_Form as h
from module.frm_celebrate import Ui_Form as i
from module.frm_step import Ui_Form as j
from func_json import *


class mod_result(QWidget,b):
	def __init__(self, args):
		super(mod_result, self).__init__()
		self.setupUi(self)
		self.args = args
		self.lbl_order.setText(str(args['data'][0][7]))#序号
		self.lbl_rank.setText(str(args['data'][0][24]))#当前场名次
		self.lbl_name.setText(str(args['data'][0][8]))#姓名
		self.lbl_city.setText(str(args['data'][0][6]))#队名
		self.lbl_horse.setText(str(args['data'][0][9]))#马名
		self.lbl_E.setText(str(args['data'][0][13]))#E成绩
		self.lbl_M.setText(str(args['data'][0][16]))#M成绩
		self.lbl_C.setText(str(args['data'][0][15]))#C成绩
		self.lbl_E_rank.setText(str(args['data'][0][18]))#E名次
		self.lbl_M_rank.setText(str(args['data'][0][21]))#M名次
		self.lbl_C_rank.setText(str(args['data'][0][20]))#C名次
		self.lbl_result.setText(str(args['data'][0][23]))#当场成绩
		self.tbwgt_content.setHorizontalHeaderLabels(['名次','姓名','单位','成绩'])  # 设置表头内容
		self.register = eval(args['content'])#字符串转列表
		self.rownum = 0
		self.loaddata()


	def loaddata(self):

		row = self.rownum
		self.tbwgt_content.clear()
		self.tbwgt_content_2.clear()

		i = 0#i代表的是表格行数
		for row in range(row,row+5):#row代表的是数据data的行数

			if row>= len(self.register) : #判断数据显示是否到头
				self.rownum = 0
				return

			self.tbwgt_content.setRowCount(i + 2)#设置行数

			# 名次
			item = QTableWidgetItem(str(self.register[row][6]))
			item.setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)#垂直水平都居中
			font = QFont("微软雅黑", 30, 75)
			item.setFont(font)
			self.tbwgt_content.setItem(i, 0, item)
			self.tbwgt_content.resizeColumnToContents(0)
			self.tbwgt_content.resizeRowToContents(0)

			# 姓名
			if len(str(self.register[row][1]))> 4 :#单元格字体大于4字节，字体缩小
				item = QTableWidgetItem(str(self.register[row][1]))
				font = QFont("微软雅黑",20,75)
				item.setFont(font)
				self.tbwgt_content.setItem(i, 1, item)
			else :
				item = QTableWidgetItem(str(self.register[row][1]))
				font = QFont("微软雅黑", 30, 75)
				item.setFont(font)
				self.tbwgt_content.setItem(i, 1, item)
			self.tbwgt_content.resizeColumnToContents(1)#与内容同宽
			self.tbwgt_content.resizeRowToContents(1)

			# 马名
			item = QTableWidgetItem(str(self.register[row][2]))
			item.setTextAlignment(Qt.AlignVCenter | Qt.AlignLeft)  # 垂直水平都居中
			font = QFont("微软雅黑", 30, 75)
			item.setFont(font)
			self.tbwgt_content.setItem(i, 2, item)
			self.tbwgt_content.resizeColumnToContents(2)#与内容同宽
			self.tbwgt_content.resizeRowToContents(2)

			# 成绩
			item = QTableWidgetItem(str(self.register[row][7]))
			font = QFont()
			font.setFamily("微软雅黑")
			font.setPointSize(30)
			font.setBold(True)
			item.setFont(font)
			item.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)
			self.tbwgt_content.setItem(i, 3, item)
			# self.tbwgt_content.resizeColumnToContents(3)#与内容同宽
			self.tbwgt_content.resizeRowToContents(3)

			i += 1
		row += 1
		#调整单元格自动适应文字大小


		i = 0#i代表的是表格行数
		for row in range(row,row+5):#row代表的是数据data的行数

			if row>= len(self.register) : #判断数据显示是否到头
				self.rownum = 0
				return

			self.tbwgt_content_2.setRowCount(i + 2)#设置行数

			# 名次
			item = QTableWidgetItem(str(self.register[row][6]))
			item.setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)#垂直水平都居中
			font = QFont("微软雅黑", 30, 75)
			item.setFont(font)
			self.tbwgt_content_2.setItem(i, 0, item)
			self.tbwgt_content_2.resizeColumnToContents(0)
			self.tbwgt_content_2.resizeRowToContents(0)

			# 姓名
			if len(str(self.register[row][1]))> 4 :#单元格字体大于4字节，字体缩小
				item = QTableWidgetItem(str(self.register[row][1]))
				font = QFont("微软雅黑",20,75)
				item.setFont(font)
				self.tbwgt_content_2.setItem(i, 1, item)
			else :
				item = QTableWidgetItem(str(self.register[row][1]))
				font = QFont("微软雅黑", 30, 75)
				item.setFont(font)
				self.tbwgt_content_2.setItem(i, 1, item)
			self.tbwgt_content_2.resizeColumnToContents(1)#与内容同宽
			self.tbwgt_content_2.resizeRowToContents(1)

			# 马名
			item = QTableWidgetItem(str(self.register[row][2]))
			item.setTextAlignment(Qt.AlignVCenter | Qt.AlignLeft)  # 垂直水平都居中
			font = QFont("微软雅黑", 30, 75)
			item.setFont(font)
			self.tbwgt_content_2.setItem(i, 2, item)
			self.tbwgt_content_2.resizeColumnToContents(2)#与内容同宽
			self.tbwgt_content_2.resizeRowToContents(2)

			# 成绩
			item = QTableWidgetItem(str(self.register[row][7]))
			font = QFont()
			font.setFamily("微软雅黑")
			font.setPointSize(30)
			font.setBold(True)
			item.setFont(font)
			item.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)
			self.tbwgt_content_2.setItem(i, 3, item)
			# self.tbwgt_content_2.resizeColumnToContents(3)#与内容同宽
			self.tbwgt_content_2.resizeRowToContents(3)

			i += 1
			row += 1
		self.rownum = row


class mod_schedule(QWidget,a):
	def __init__(self, args,scrolltime):
		super(mod_schedule, self).__init__()
		self.setupUi(self)
		self.args = args
		self.tbwgt_content.clear()
		self.tbwgt_content.setColumnCount(6)  # 设定列数
		# self.tbwgt_content.setHorizontalHeaderLabels(['时间','比赛','赛段'])  # 设置表头内容
		self.scrolltime= scrolltime
		self.register = args['content']
		self.timer = QTimer()
		self.timer.timeout.connect(self.loaddata)
		self.rownum = 0 
		self.loaddata()
		self.timer.start(self.scrolltime)

	def endtimer(self): 
		self.timer.stop()

	def starttimer(self,args): 
		self.timer.start(args)

	def loaddata(self):

		row = self.rownum
		if row>= len(self.register) : #判断数据显示是否到头,重新加载不空屏显示。
			row = 0 

		self.tbwgt_content.clear()

		i = 0#i代表的是表格行数
		for row in range(row,len(self.register)):#row代表的是数据data的行数

			if row>= len(self.register) : #判断数据显示是否到头
				self.rownum = 0 
				return
			# (1, 1, 1, 'Jun 23 2014  9:00AM', '2020-10-06', '盛装舞步个人赛', '资格赛', '资格赛', '09:00')
			self.tbwgt_content.setRowCount(i + 2)#设置行数
			self.tbwgt_content.setItem(i, 1, QTableWidgetItem(str(self.register[row][4])))
			self.tbwgt_content.setItem(i, 2, QTableWidgetItem(str(self.register[row][8])))
			self.tbwgt_content.setItem(i, 3, QTableWidgetItem(str(self.register[row][5])))
			self.tbwgt_content.setItem(i, 4, QTableWidgetItem(str(self.register[row][6])))

			i += 1
		row += 1
		#调整单元格自动适应文字大小
		self.tbwgt_content.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
		self.tbwgt_content.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
		self.tbwgt_content.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
		self.tbwgt_content.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
		self.tbwgt_content.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)

		self.rownum = row

class mod_judge(QWidget,c):
	def __init__(self, args):
		super(mod_judge, self).__init__()
		self.setupUi(self)
		self.args = args
		self.tbwgt_content.setColumnCount(6)  # 设定列数
		self.tbwgt_content.setHorizontalHeaderLabels(['职位','姓名','单位'])  # 设置表头内容
		i = 0
		for row in range(0,len(args["content"])):
			self.tbwgt_content.setRowCount(i + 1)#设置行数
			item = QTableWidgetItem(str(args['content'][row][0]))
			font = QFont()
			font.setFamily("微软雅黑")
			font.setPointSize(80)
			item.setFont(font)
			self.tbwgt_content.setItem(i, 2, item)
			# self.tbwgt_content.resizeColumnToContents(1)

			item = QTableWidgetItem(str(args['content'][row][1]))
			font = QFont()
			font.setFamily("微软雅黑")
			font.setPointSize(80)
			item.setFont(font)
			self.tbwgt_content.setItem(i, 3, item)
			self.tbwgt_content.resizeColumnToContents(3)

			item = QTableWidgetItem(str(args['content'][row][2]))
			font = QFont()
			font.setFamily("微软雅黑")
			font.setPointSize(80)
			item.setFont(font)
			self.tbwgt_content.setItem(i, 5, item)
			self.tbwgt_content.resizeColumnToContents(5)
			i += 1

		#调整单元格自动适应文字大小

class mod_resultlist(QWidget,d):
	def __init__(self, args,scrolltime):
		super(mod_resultlist, self).__init__()
		self.setupUi(self)
		self.tbwgt_content.setColumnCount(9)  # 设定列数
		self.tbwgt_content.setHorizontalHeaderLabels(['名次','姓名','成绩','马名','单位'])  # 设置表头内容
		self.scrolltime= scrolltime

		self.register = eval(args['content'])#字符串转列表
		self.timer = QTimer()
		self.timer.timeout.connect(self.loaddata)
		self.rownum = 0 
		self.loaddata()
		self.timer.start(self.scrolltime)

	def endtimer(self): 
		self.timer.stop()

	def starttimer(self,args): 
		self.timer.start(args)

	def loaddata(self):

		row = self.rownum
		if row>= len(self.register) : #判断数据显示是否到头,重新加载不空屏显示。
			row = 0 

		self.tbwgt_content.clear()

		i = 0#i代表的是表格行数
		for row in range(row,row+8):#row代表的是数据data的行数

			if row>= len(self.register) : #判断数据显示是否到头
				self.rownum = 0 
				return

			self.tbwgt_content.setRowCount(i + 1)#设置行数
			self.tbwgt_content.setItem(i, 1, QTableWidgetItem(str(self.register[row][6])))#名次
			self.tbwgt_content.resizeColumnToContents(1)

			#单元格字体大于4字节，字体缩小
			if len(str(self.register[row][1]))> 4 :
				item = QTableWidgetItem(str(self.register[row][1]))
				font = QFont()
				font.setFamily("微软雅黑")
				font.setPointSize(30)
				item.setFont(font)
				self.tbwgt_content.setItem(i, 2, item)
			else :
				self.tbwgt_content.setItem(i, 2, QTableWidgetItem(str(self.register[row][1]))) #姓名
			self.tbwgt_content.resizeColumnToContents(2)

			item = QTableWidgetItem(str(self.register[row][2]))
			font = QFont()
			font.setFamily("微软雅黑")
			font.setPointSize(25)
			font.setBold(True)
			item.setFont(font)
			# item.setTextAlignment(Qt.AlignLeading|Qt.AlignTop)
			brush = QBrush(QColor(255, 206, 0))
			brush.setStyle(Qt.NoBrush)
			item.setForeground(brush)
			self.tbwgt_content.setItem(i, 3, item)
			self.tbwgt_content.resizeColumnToContents(3)#马名

			self.tbwgt_content.setItem(i, 5, QTableWidgetItem(str(self.register[row][3]))) #单位
			self.tbwgt_content.resizeColumnToContents(5)

			self.tbwgt_content.setItem(i, 7, QTableWidgetItem(str(self.register[row][7]))) #成绩
			self.tbwgt_content.resizeColumnToContents(7)
			i += 1
		row += 1

		self.rownum = row


class mod_startlist(QWidget,e):
	def __init__(self, args,scrolltime):
		super(mod_startlist, self).__init__()
		self.setupUi(self)
		self.args = args
		self.tbwgt_content.setColumnCount(8)  # 设定列数
		self.tbwgt_content.setHorizontalHeaderLabels(['名次','姓名','马名','单位'])  # 设置表头内容
		self.register = args['content']
		self.timer = QTimer()
		self.timer.timeout.connect(self.loaddata)
		self.scrolltime= scrolltime
		self.rownum = 0 
		self.loaddata()
		self.timer.start(self.scrolltime)

	def endtimer(self): 
		self.timer.stop()

	def starttimer(self,args): 
		self.timer.start(args)

	def loaddata(self):

		row = self.rownum
		if row>= len(self.register) : #判断数据显示是否到头,重新加载不空屏显示。
			row = 0 

		self.tbwgt_content.clear()

		i = 0#i代表的是表格行数
		for row in range(row,row+8):#row代表的是数据data的行数

			if row>= len(self.register) : #判断数据显示是否到头
				self.rownum = 0 
				return


			self.tbwgt_content.setRowCount(i + 2)#设置行数
			self.tbwgt_content.setItem(i, 1, QTableWidgetItem(str(self.register[row][0])))#顺序
			self.tbwgt_content.resizeColumnToContents(1)

			#单元格字体大于4字节，字体缩小
			if len(str(self.register[row][1]))> 4 :
				item = QTableWidgetItem(str(self.register[row][1]))
				font = QFont()
				font.setFamily("微软雅黑")
				font.setPointSize(30)
				item.setFont(font)
				self.tbwgt_content.setItem(i, 2, item)
			else :
				self.tbwgt_content.setItem(i, 2, QTableWidgetItem(str(self.register[row][1])))#姓名
			self.tbwgt_content.resizeColumnToContents(2)

			self.tbwgt_content.setItem(i, 5, QTableWidgetItem(str(self.register[row][5])))#代表队
			self.tbwgt_content.resizeColumnToContents(5)

			#单元格字体大于4字节，字体缩小
			item = QTableWidgetItem(str(self.register[row][2]))
			font = QFont()
			font.setFamily("微软雅黑")
			font.setPointSize(25)
			font.setBold(True)
			item.setFont(font)
			# item.setTextAlignment(4)#Qt.AlignLeading|Qt.AlignTop
			brush = QBrush(QColor(255, 206, 0))
			brush.setStyle(Qt.NoBrush)
			item.setForeground(brush)
			# i += 1
			self.tbwgt_content.setItem(i, 3, item)
			self.tbwgt_content.resizeColumnToContents(3)#马名

			i += 1
		row += 1
		self.rownum = row


class mod_ranklist(QWidget,g):
	def __init__(self, args,scrolltime):
		super(mod_ranklist, self).__init__()
		self.setupUi(self)
		self.args = args
		self.tbwgt_content.setColumnCount(5)  # 设定列数
		self.tbwgt_content.setHorizontalHeaderLabels(['名次','姓名','成绩','马名','单位'])  # 设置表头内容
		self.scrolltime= scrolltime
		self.register = eval(args['content'])#字符串转列表
		self.timer = QTimer()
		self.timer.timeout.connect(self.loaddata)
		self.rownum = 0 
		self.loaddata()
		self.timer.start(scrolltime)

	def endtimer(self): 
		self.timer.stop()

	def starttimer(self): 
		self.timer.start(self.scrolltime)

	def loaddata(self):

		row = self.rownum
		if row>= len(self.register) : #判断数据显示是否到头,重新加载不空屏显示。
			row = 0 

		self.tbwgt_content.clear()
		self.tbwgt_content_2.clear()
		
		i = 0#i代表的是表格行数
		for row in range(row,row+5):#row代表的是数据data的行数

			if row>= len(self.register) : #判断数据显示是否到头
				self.rownum = 0 
				return

			self.tbwgt_content.setRowCount(i + 2)#设置行数
			self.tbwgt_content.setItem(i, 0, QTableWidgetItem(str(self.register[row][6])))
			self.tbwgt_content.resizeColumnToContents(0)

			#单元格字体大于4字节，字体缩小
			if len(str(self.register[row][1]))> 4 :
				item = QTableWidgetItem(str(self.register[row][1]))
				font = QFont()
				font.setFamily("微软雅黑")
				font.setPointSize(30)
				item.setFont(font)
				self.tbwgt_content.setItem(i, 1, item)
			else :
				self.tbwgt_content.setItem(i, 1, QTableWidgetItem(str(self.register[row][1])))
			self.tbwgt_content.resizeColumnToContents(1)

			self.tbwgt_content.setItem(i, 2, QTableWidgetItem(str(self.register[row][3])))
			# self.tbwgt_content.resizeColumnToContents(2)

			self.tbwgt_content.setItem(i, 3, QTableWidgetItem(str(self.register[row][7])))
			# self.tbwgt_content.resizeColumnToContents(3)

			#单元格字体大于4字节，字体缩小
			item = QTableWidgetItem(str(self.register[row][2]))
			font = QFont()
			font.setFamily("微软雅黑")
			font.setPointSize(25)
			font.setBold(True)
			item.setFont(font)
			item.setTextAlignment(Qt.AlignLeading|Qt.AlignTop)
			brush = QBrush(QColor(255, 206, 0))
			brush.setStyle(Qt.NoBrush)
			item.setForeground(brush)
			i += 1
			self.tbwgt_content.setItem(i, 1, item)
			self.tbwgt_content.resizeColumnToContents(1)

			i += 1
		row += 1

		i = 0#i代表的是表格行数
		for row in range(row,row+5):#row代表的是数据data的行数
			
			if row>= len(self.register) : #判断数据显示是否到头
				self.rownum = 0 
				return

			self.tbwgt_content_2.setRowCount(i + 2)#设置行数
			self.tbwgt_content_2.setItem(i, 0, QTableWidgetItem(str(self.register[row][6])))
			self.tbwgt_content_2.resizeColumnToContents(0)

			#单元格字体大于4字节，字体缩小
			if len(str(self.register[row][1]))> 4 :
				item = QTableWidgetItem(str(self.register[row][1]))
				font = QFont()
				font.setFamily("微软雅黑")
				font.setPointSize(30)
				item.setFont(font)
				self.tbwgt_content_2.setItem(i, 1, item)
			else :
				self.tbwgt_content_2.setItem(i, 1, QTableWidgetItem(str(self.register[row][1])))
			self.tbwgt_content_2.resizeColumnToContents(1)

			self.tbwgt_content_2.setItem(i, 2, QTableWidgetItem(str(self.register[row][3])))
			# self.tbwgt_content_2.resizeColumnToContents(2)

			self.tbwgt_content_2.setItem(i, 3, QTableWidgetItem(str(self.register[row][7])))
			# self.tbwgt_content_2.resizeColumnToContents(3)

			#单元格字体大于4字节，字体缩小
			item = QTableWidgetItem(str(self.register[row][2]))
			font = QFont()
			font.setFamily("微软雅黑")
			font.setPointSize(25)
			font.setBold(True)
			item.setFont(font)
			item.setTextAlignment(Qt.AlignLeading|Qt.AlignTop)
			brush = QBrush(QColor(255, 206, 0))
			brush.setStyle(Qt.NoBrush)
			item.setForeground(brush)
			i += 1
			self.tbwgt_content_2.setItem(i, 1, item)
			self.tbwgt_content_2.resizeRowToContents(1)
			self.tbwgt_content_2.resizeColumnToContents(1)

			i += 1
			row += 1
			
		self.rownum = row


class mod_medal(QWidget,h):
	def __init__(self, args):
		super(mod_medal, self).__init__()
		self.setupUi(self)
		self.args = args
		self.tbwgt_content.setColumnCount(8)  # 设定列数
		self.tbwgt_content.setHorizontalHeaderLabels(['名次','姓名','成绩','马名','单位'])  # 设置表头内容

		self.register = args['content']#字符串转列表
		self.rownum = 0
		self.loaddata()

	def loaddata(self):

		row = self.rownum

		self.tbwgt_content.clear()
		self.tbwgt_content.setIconSize(QSize(200, 100))
		#['Rank', 'RegisterName', 'HorseName', 'F_DelegationShortName', 'F_EventPointsCharDes1',
		# 'Order', 'Medal', 'MedalImage', 'F_DelegationLongName', 'HorseBib',
		# 'RegisterHorseName', 'DelegationFlag', 'MedalEvent']
		#(1, '刘涛', 'Razida', '新疆队', '73.059',
		# 1, '金牌', '[Image]金牌', '新疆队', '19',
		# '刘涛 / Razida', '[Image]新疆队', '金牌-盛装舞步个人赛')
		i = 0#i代表的是表格行数
		for row in range(row,len(self.register)):#row代表的是数据data的行数

			self.tbwgt_content.setRowCount(i + 1)#设置行数

			item = QTableWidgetItem(str(self.register[row][10]))
			if self.register[row][0] == 1:
				icon = QIcon(r'.\resource\g.png')
			elif self.register[row][0] == 2:
				icon = QIcon(r'.\resource\s.png')
			elif self.register[row][0] == 3:
				icon = QIcon(r'.\resource\b.png')
			elif self.register[row][0] > 3:
				return
			item.setIcon(QIcon(icon))
			self.tbwgt_content.setItem(i, 1,item)#奖牌图ico
			self.tbwgt_content.resizeColumnToContents(1)

			self.tbwgt_content.setItem(i, 3, QTableWidgetItem(str(self.register[row][3])))#代表队
			self.tbwgt_content.resizeColumnToContents(3)

			i += 1

		self.rownum = row


class mod_welcome(QWidget,f):
	def __init__(self, args):
		super(mod_welcome, self).__init__()
		self.setupUi(self)
		self.args = args
		self.lbl_content.setText(args['content'])

class mod_step(QWidget,j):
	def __init__(self, args):
		super(mod_step, self).__init__()
		self.setupUi(self)
		self.args = args
		self.lbl_content.setText(args['content'])

class mod_celebrate(QWidget,i):
	def __init__(self, args):
		super(mod_celebrate, self).__init__()
		self.setupUi(self)
		self.args = args
		# self.lbl_title.setText(args['celebrate'])

if __name__ == '__main__':

	app = QApplication(sys.argv)
	demo = mod_result("d")
	demo.show()
	sys.exit(app.exec_())
