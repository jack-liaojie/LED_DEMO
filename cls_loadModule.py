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
    def __init__(self, args,scrolltime):
        super(mod_result, self).__init__()
        self.setupUi(self)
        self.scrolltime= scrolltime
        self.args = args
        self.lbl_title.setText(str(args['result']))
        self.lbl_order.setText(str(args['data'][0][7]))#序号
        self.lbl_rank.setText(str(args['data'][0][24]))#当前场名次
        self.lbl_name.setText(str(args['data'][0][8]))#姓名
        self.lbl_city.setText(str(args['data'][0][6]))#队名
        self.lbl_horse.setText(str(args['data'][0][9]))#马名
        self.lbl_E.setText(str(args['data'][0][13]))#E成绩
        self.lbl_M.setText(str(args['data'][0][16]))#M成绩
        self.lbl_C.setText(str(args['data'][0][15]))#C成绩
        self.lbl_result.setText(str(args['data'][0][23]))#当场成绩
        self.tbwgt_content.setHorizontalHeaderLabels(['名次','姓名','单位','成绩'])  # 设置表头内容
        self.lbl_counttimer.setText("  ")
        self.register = eval(args['content'])#字符串转列表
        self.timer = QTimer()
        self.timer.timeout.connect(self.ReverseTime)
        self.rownum = 0 
        self.temptime = 0
        self.loaddata()

    def showtimer(self):
        self.lbl_counttimer.setText(str(self.scrolltime))

    def endtimer(self): 
        self.timer.stop()
        self.scrolltime = self.temptime
        self.lbl_counttimer.setText("  ")

    def starttimer(self,arg): 
        self.showtimer()
        self.scrolltime = arg
        self.temptime = self.scrolltime
        self.timer.start(1000)

    def ReverseTime(self):
        if self.scrolltime == -1 :
            self.endtimer()
        else :
            self.lbl_counttimer.setText('{:0>2s}'.format(str(self.scrolltime)))
            self.scrolltime -= 1

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
            self.tbwgt_content.setItem(i, 0, QTableWidgetItem(str(self.register[row][6])))#名次
            #单元格字体大于4字节，字体缩小
            if len(str(self.register[row][1]))> 4 :
                item = QTableWidgetItem(str(self.register[row][1]))
                font = QFont()
                font.setFamily("微软雅黑")
                font.setPointSize(30)
                item.setFont(font)
                self.tbwgt_content.setItem(i, 1, item)
            else :
                self.tbwgt_content.setItem(i, 1, QTableWidgetItem(str(self.register[row][1])))#姓名

            # self.tbwgt_content.setItem(i, 2, QTableWidgetItem(str(self.register[row][3])))#单位
            self.tbwgt_content.setItem(i, 2, QTableWidgetItem(str(self.register[row][7])))#成绩
            #单元格字体大于4字节，字体缩小
            # item = QTableWidgetItem(str(self.register[row][2]))#马名
            # font = QFont()
            # font.setFamily("微软雅黑")
            # font.setPointSize(25)
            # font.setBold(True)
            # item.setFont(font)
            # item.setTextAlignment(Qt.AlignLeading|Qt.AlignTop)
            # brush = QBrush(QColor(255, 255, 0))
            # brush.setStyle(Qt.NoBrush)
            # item.setForeground(brush)
            i += 1
        row += 1
            # self.tbwgt_content.setItem(i, 1, item)
            # i += 1
        #调整单元格自动适应文字大小
        self.tbwgt_content.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tbwgt_content.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.tbwgt_content.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.tbwgt_content.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        # self.tbwgt_content.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
        # self.tbwgt_content.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)


        i = 0#i代表的是表格行数
        for row in range(row,row+5):#row代表的是数据data的行数
            
            if row>= len(self.register) : #判断数据显示是否到头
                self.rownum = 0 
                return

            self.tbwgt_content_2.setRowCount(i + 2)#设置行数
            self.tbwgt_content_2.setItem(i, 0, QTableWidgetItem(str(self.register[row][6])))
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

            # self.tbwgt_content_2.setItem(i, 2, QTableWidgetItem(str(self.register[row][3])))
            self.tbwgt_content_2.setItem(i, 2, QTableWidgetItem(str(self.register[row][7])))
            #单元格字体大于4字节，字体缩小
            # item = QTableWidgetItem(str(self.register[row][2]))
            # font = QFont()
            # font.setFamily("微软雅黑")
            # font.setPointSize(25)
            # font.setBold(True)
            # item.setFont(font)
            # item.setTextAlignment(Qt.AlignLeading|Qt.AlignTop)
            # brush = QBrush(QColor(255, 255, 0))
            # brush.setStyle(Qt.NoBrush)
            # item.setForeground(brush)
            # i += 1
            # self.tbwgt_content_2.setItem(i, 1, item)
            i += 1
            row += 1
        #调整单元格自动适应文字大小
        self.tbwgt_content_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tbwgt_content_2.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.tbwgt_content_2.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.tbwgt_content_2.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.tbwgt_content_2.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
        # self.tbwgt_content.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)

        self.rownum = row


class mod_schedule(QWidget,a):
    def __init__(self, args):
        super(mod_schedule, self).__init__()
        self.setupUi(self)
        self.args = args
        self.lbl_title.setText(args['schedule'])
        self.tbwgt_content.clear()
        self.tbwgt_content.setColumnCount(6)  # 设定列数
        self.tbwgt_content.setHorizontalHeaderLabels(['时间','比赛','赛段'])  # 设置表头内容
        i = 1
        for row in range(0,len(args["content"])):
            self.tbwgt_content.setRowCount(row + 2)#设置行数
            self.tbwgt_content.setItem(i, 1, QTableWidgetItem(str(args['content'][row][0])))
            self.tbwgt_content.setItem(i, 3, QTableWidgetItem(str(args['content'][row][1])))
            # self.tbwgt_content.setItem(i, 2, QTableWidgetItem(str(args['content'][i][2])))
            i += 1

        #调整单元格自动适应文字大小
        self.tbwgt_content.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tbwgt_content.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.tbwgt_content.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.tbwgt_content.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
class mod_judge(QWidget,c):
    def __init__(self, args):
        super(mod_judge, self).__init__()
        self.setupUi(self)
        self.args = args
        self.lbl_title.setText(args['judge'])
        self.tbwgt_content.setColumnCount(6)  # 设定列数
        self.tbwgt_content.setHorizontalHeaderLabels(['职位','姓名','单位'])  # 设置表头内容
        i = 2
        for row in range(0,len(args["content"])):
            self.tbwgt_content.setRowCount(i + 1)#设置行数
            self.tbwgt_content.setItem(i, 1, QTableWidgetItem(str(args['content'][row][0])))
            self.tbwgt_content.setItem(i, 2, QTableWidgetItem(str(args['content'][row][1])))
            self.tbwgt_content.setItem(i, 4, QTableWidgetItem(str(args['content'][row][2])))
            # self.tbwgt_content.setItem(i, 3, QTableWidgetItem(str(args['content'][row][3])))
            i += 1

        #调整单元格自动适应文字大小
        self.tbwgt_content.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tbwgt_content.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.tbwgt_content.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.tbwgt_content.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)

class mod_resultlist(QWidget,d):
    def __init__(self, args,scrolltime):
        super(mod_resultlist, self).__init__()
        self.setupUi(self)
        self.lbl_title.setText(args["r_list"])
        self.tbwgt_content.setColumnCount(5)  # 设定列数
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
        self.tbwgt_content.clear()
        self.tbwgt_content_2.clear()
        
        i = 0#i代表的是表格行数
        for row in range(row,row+5):#row代表的是数据data的行数

            if row>= len(self.register) : #判断数据显示是否到头
                self.rownum = 0 
                return

            self.tbwgt_content.setRowCount(i + 2)#设置行数
            self.tbwgt_content.setItem(i, 0, QTableWidgetItem(str(self.register[row][6])))
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

            self.tbwgt_content.setItem(i, 2, QTableWidgetItem(str(self.register[row][3])))
            self.tbwgt_content.setItem(i, 3, QTableWidgetItem(str(self.register[row][7])))
            #单元格字体大于4字节，字体缩小
            item = QTableWidgetItem(str(self.register[row][2]))
            font = QFont()
            font.setFamily("微软雅黑")
            font.setPointSize(25)
            font.setBold(True)
            item.setFont(font)
            item.setTextAlignment(Qt.AlignLeading|Qt.AlignTop)
            brush = QBrush(QColor(255, 255, 0))
            brush.setStyle(Qt.NoBrush)
            item.setForeground(brush)
            i += 1
            self.tbwgt_content.setItem(i, 1, item)
            i += 1
        row += 1
        #调整单元格自动适应文字大小
        self.tbwgt_content.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tbwgt_content.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.tbwgt_content.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.tbwgt_content.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.tbwgt_content.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
        # self.tbwgt_content.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)



        i = 0#i代表的是表格行数
        for row in range(row,row+5):#row代表的是数据data的行数
            
            if row>= len(self.register) : #判断数据显示是否到头
                self.rownum = 0 
                return

            self.tbwgt_content_2.setRowCount(i + 2)#设置行数
            self.tbwgt_content_2.setItem(i, 0, QTableWidgetItem(str(self.register[row][6])))
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

            self.tbwgt_content_2.setItem(i, 2, QTableWidgetItem(str(self.register[row][3])))
            self.tbwgt_content_2.setItem(i, 3, QTableWidgetItem(str(self.register[row][7])))
            #单元格字体大于4字节，字体缩小
            item = QTableWidgetItem(str(self.register[row][2]))
            font = QFont()
            font.setFamily("微软雅黑")
            font.setPointSize(25)
            font.setBold(True)
            item.setFont(font)
            item.setTextAlignment(Qt.AlignLeading|Qt.AlignTop)
            brush = QBrush(QColor(255, 255, 0))
            brush.setStyle(Qt.NoBrush)
            item.setForeground(brush)
            i += 1
            self.tbwgt_content_2.setItem(i, 1, item)
            i += 1
            row += 1
            
        #调整单元格自动适应文字大小
        self.tbwgt_content_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tbwgt_content_2.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.tbwgt_content_2.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.tbwgt_content_2.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.tbwgt_content_2.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
        # self.tbwgt_content.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)
        self.rownum = row



class mod_startlist(QWidget,e):
    def __init__(self, args,scrolltime):
        super(mod_startlist, self).__init__()
        self.setupUi(self)
        self.args = args
        self.lbl_title.setText(args['startlist'])
        self.tbwgt_content.setColumnCount(5)  # 设定列数
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
        self.tbwgt_content.clear()
        self.tbwgt_content_2.clear()
        
        i = 0#i代表的是表格行数
        for row in range(row,row+5):#row代表的是数据data的行数

            if row>= len(self.register) : #判断数据显示是否到头
                self.rownum = 0 
                return


            self.tbwgt_content.setRowCount(i + 2)#设置行数
            self.tbwgt_content.setItem(i, 0, QTableWidgetItem(str(self.register[row][0])))
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

            self.tbwgt_content.setItem(i, 2, QTableWidgetItem(str(self.register[row][5])))
            #单元格字体大于4字节，字体缩小
            item = QTableWidgetItem(str(self.register[row][2]))
            font = QFont()
            font.setFamily("微软雅黑")
            font.setPointSize(25)
            font.setBold(True)
            item.setFont(font)
            item.setTextAlignment(Qt.AlignLeading|Qt.AlignTop)
            brush = QBrush(QColor(255, 255, 0))
            brush.setStyle(Qt.NoBrush)
            item.setForeground(brush)
            i += 1
            self.tbwgt_content.setItem(i, 1, item)
            i += 1
        row += 1
        #调整单元格自动适应文字大小
        self.tbwgt_content.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tbwgt_content.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.tbwgt_content.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.tbwgt_content.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)


        i = 0#i代表的是表格行数
        for row in range(row,row+5):#row代表的是数据data的行数
            
            if row>= len(self.register) : #判断数据显示是否到头
                self.rownum = 0 
                return

            self.tbwgt_content_2.setRowCount(i + 2)#设置行数
            self.tbwgt_content_2.setItem(i, 0, QTableWidgetItem(str(self.register[row][0])))
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

            self.tbwgt_content_2.setItem(i, 2, QTableWidgetItem(str(self.register[row][5])))
            #单元格字体大于4字节，字体缩小
            item = QTableWidgetItem(str(self.register[row][2]))
            font = QFont()
            font.setFamily("微软雅黑")
            font.setPointSize(25)
            font.setBold(True)
            item.setFont(font)
            item.setTextAlignment(Qt.AlignLeading|Qt.AlignTop)
            brush = QBrush(QColor(255, 255, 0))
            brush.setStyle(Qt.NoBrush)
            item.setForeground(brush)
            i += 1
            self.tbwgt_content_2.setItem(i, 1, item)
            i += 1

            row += 1

        #调整单元格自动适应文字大小
        self.tbwgt_content_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tbwgt_content_2.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.tbwgt_content_2.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.tbwgt_content_2.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)

        self.rownum = row



class mod_ranklist(QWidget,g):
    def __init__(self, args,scrolltime):
        super(mod_ranklist, self).__init__()
        self.setupUi(self)
        self.args = args
        self.lbl_title.setText(args["k_list"])
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
        self.tbwgt_content.clear()
        self.tbwgt_content_2.clear()
        
        i = 0#i代表的是表格行数
        for row in range(row,row+5):#row代表的是数据data的行数

            if row>= len(self.register) : #判断数据显示是否到头
                self.rownum = 0 
                return

            self.tbwgt_content.setRowCount(i + 2)#设置行数
            self.tbwgt_content.setItem(i, 0, QTableWidgetItem(str(self.register[row][6])))
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

            self.tbwgt_content.setItem(i, 2, QTableWidgetItem(str(self.register[row][3])))
            self.tbwgt_content.setItem(i, 3, QTableWidgetItem(str(self.register[row][7])))
            #单元格字体大于4字节，字体缩小
            item = QTableWidgetItem(str(self.register[row][2]))
            font = QFont()
            font.setFamily("微软雅黑")
            font.setPointSize(25)
            font.setBold(True)
            item.setFont(font)
            item.setTextAlignment(Qt.AlignLeading|Qt.AlignTop)
            brush = QBrush(QColor(255, 255, 0))
            brush.setStyle(Qt.NoBrush)
            item.setForeground(brush)
            i += 1
            self.tbwgt_content.setItem(i, 1, item)
            i += 1
        row += 1
        #调整单元格自动适应文字大小
        self.tbwgt_content.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tbwgt_content.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.tbwgt_content.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.tbwgt_content.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.tbwgt_content.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
        # self.tbwgt_content.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)



        i = 0#i代表的是表格行数
        for row in range(row,row+5):#row代表的是数据data的行数
            
            if row>= len(self.register) : #判断数据显示是否到头
                self.rownum = 0 
                return

            self.tbwgt_content_2.setRowCount(i + 2)#设置行数
            self.tbwgt_content_2.setItem(i, 0, QTableWidgetItem(str(self.register[row][6])))
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

            self.tbwgt_content_2.setItem(i, 2, QTableWidgetItem(str(self.register[row][3])))
            self.tbwgt_content_2.setItem(i, 3, QTableWidgetItem(str(self.register[row][7])))
            #单元格字体大于4字节，字体缩小
            item = QTableWidgetItem(str(self.register[row][2]))
            font = QFont()
            font.setFamily("微软雅黑")
            font.setPointSize(25)
            font.setBold(True)
            item.setFont(font)
            item.setTextAlignment(Qt.AlignLeading|Qt.AlignTop)
            brush = QBrush(QColor(255, 255, 0))
            brush.setStyle(Qt.NoBrush)
            item.setForeground(brush)
            i += 1
            self.tbwgt_content_2.setItem(i, 1, item)
            i += 1
            row += 1
            
        #调整单元格自动适应文字大小
        self.tbwgt_content_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tbwgt_content_2.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.tbwgt_content_2.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.tbwgt_content_2.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.tbwgt_content_2.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
        # self.tbwgt_content.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)
        self.rownum = row


class mod_medal(QWidget,h):
    def __init__(self, args,scrolltime):
        super(mod_medal, self).__init__()
        self.setupUi(self)
        self.args = args
        self.scrolltime = scrolltime
        self.lbl_title.setText(args["medal"])
        self.tbwgt_content.setColumnCount(5)  # 设定列数
        self.tbwgt_content.setHorizontalHeaderLabels(['名次','姓名','成绩','马名','单位'])  # 设置表头内容

        self.register = args['content']#字符串转列表
        self.timer = QTimer()
        self.timer.timeout.connect(self.loaddata)
        self.rownum = 0 
        self.loaddata()
        self.timer.start(self.scrolltime)

    def endtimer(self): 
        self.timer.stop()

    def starttimer(self): 
        self.timer.start(self.scrolltime)

    def loaddata(self):

        row = self.rownum
        self.tbwgt_content.clear()
        
        i = 0#i代表的是表格行数
        for row in range(row,row+5):#row代表的是数据data的行数
            
            if row>= len(self.register) : #判断数据显示是否到头
                self.rownum = 0 
                return

            self.tbwgt_content.setRowCount(i + 2)#设置行数
            self.tbwgt_content.setItem(i, 0, QTableWidgetItem(str(self.register[row][5])))
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

            self.tbwgt_content.setItem(i, 2, QTableWidgetItem(str(self.register[row][3])))
            self.tbwgt_content.setItem(i, 3, QTableWidgetItem(str(self.register[row][4])))
            self.tbwgt_content.setItem(i, 4, QTableWidgetItem(str(self.register[row][6]).replace("None","")))
            #单元格字体大于4字节，字体缩小
            item = QTableWidgetItem(str(self.register[row][2]))
            font = QFont()
            font.setFamily("微软雅黑")
            font.setPointSize(25)
            font.setBold(True)
            item.setFont(font)
            item.setTextAlignment(Qt.AlignLeading|Qt.AlignTop)
            brush = QBrush(QColor(255, 255, 0))
            brush.setStyle(Qt.NoBrush)
            item.setForeground(brush)
            i += 1
            self.tbwgt_content.setItem(i, 1, item)
            i += 1
        
        row += 1
            
        #调整单元格自动适应文字大小
        self.tbwgt_content.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tbwgt_content.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.tbwgt_content.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.tbwgt_content.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.tbwgt_content.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
        # self.tbwgt_content.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)
        
        i = 0#i代表的是表格行数
        for row in range(row,row+5):#row代表的是数据data的行数
            
            if row>= len(self.register) : #判断数据显示是否到头
                self.rownum = 0 
                return

            self.tbwgt_content_2.setRowCount(i + 2)#设置行数
            self.tbwgt_content_2.setItem(i, 0, QTableWidgetItem(str(self.register[row][5])))
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

            self.tbwgt_content_2.setItem(i, 2, QTableWidgetItem(str(self.register[row][3])))
            self.tbwgt_content_2.setItem(i, 3, QTableWidgetItem(str(self.register[row][4])))
            self.tbwgt_content_2.setItem(i, 4, QTableWidgetItem(str(self.register[row][6]).replace("None","")))
            #单元格字体大于4字节，字体缩小
            item = QTableWidgetItem(str(self.register[row][2]))
            font = QFont()
            font.setFamily("微软雅黑")
            font.setPointSize(25)
            font.setBold(True)
            item.setFont(font)
            item.setTextAlignment(Qt.AlignLeading|Qt.AlignTop)
            brush = QBrush(QColor(255, 255, 0))
            brush.setStyle(Qt.NoBrush)
            item.setForeground(brush)
            i += 1
            self.tbwgt_content_2.setItem(i, 1, item)
            i += 1
            row += 1
            
        #调整单元格自动适应文字大小
        self.tbwgt_content_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tbwgt_content_2.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.tbwgt_content_2.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.tbwgt_content_2.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.tbwgt_content_2.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)

        self.rownum = row



class mod_welcome(QWidget,f):
    def __init__(self, args):
        super(mod_welcome, self).__init__()
        self.setupUi(self)
        self.args = args
        self.lbl_title.setText(args['welcome'])
        self.lbl_content.setText(args['content'])

class mod_step(QWidget,j):
    def __init__(self, args):
        super(mod_step, self).__init__()
        self.setupUi(self)
        self.args = args
        self.lbl_title.setText(args['step'])
        self.lbl_content.setText(args['content'])

class mod_celebrate(QWidget,i):
    def __init__(self, args):
        super(mod_celebrate, self).__init__()
        self.setupUi(self)
        self.args = args
        self.lbl_title.setText(args['celebrate'])
        self.lbl_content.setText(args['content'])

if __name__ == '__main__':

    args =  {
        "result" :"盛装舞步预赛",
        "data":
            [
                {"sport": "盛装舞步","event":"资格赛",
                 "order":"3","rank": "1","name":"廖杰","city":"山西","horse":"火龙驹","result":"343.33",
                 "E":"23","M":"123","C":"242","P":"234"}
            ],
        "content":
            [   {"order":"1","name":"吉喆","result":"222","city":"山东"},
                {"order":"2","name":"吉喆","result":"222","city":"山东"},
                {"order":"3","name":"吉喆","result":"222","city":"山东"}
            ]
    }

    app = QApplication(sys.argv)
    demo = mod_result(args)
    demo.show()
    sys.exit(app.exec_())
