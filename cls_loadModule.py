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
        self.lbl_title.setText(args['result'])
        self.lbl_rank.setText(args['data'][0]['rank'])
        self.lbl_name.setText(args['data'][0]['name'])
        self.lbl_city.setText(args['data'][0]['city'])
        self.lbl_horse.setText(args['data'][0]['horse'])
        self.lbl_E.setText(args['data'][0]['E'])
        self.lbl_M.setText(args['data'][0]['M'])
        self.lbl_C.setText(args['data'][0]['C'])
        self.lbl_P.setText(args['data'][0]['P'])
        self.lbl_result.setText(args['data'][0]['result'])
        self.tbwgt_content.setHorizontalHeaderLabels(['名次','姓名','成绩','单位'])  # 设置表头内容
        i = 0
        for row in range(0,len(args["content"])):
            self.tbwgt_content.setRowCount(row + 1)#设置行数
            self.tbwgt_content.setItem(i, 0, QTableWidgetItem(str(args['content'][row]['order'])))
            self.tbwgt_content.setItem(i, 1, QTableWidgetItem(str(args['content'][row]['name'])))
            self.tbwgt_content.setItem(i, 2, QTableWidgetItem(str(args['content'][row]['result'])))
            self.tbwgt_content.setItem(i, 3, QTableWidgetItem(str(args['content'][row]['city'])))
            i += 1

        self.column = self.tbwgt_content.columnCount()

class mod_schedule(QWidget,a):
    def __init__(self, args):
        super(mod_schedule, self).__init__()
        self.setupUi(self)
        self.args = args
        self.lbl_title.setText(args['schedule'])
        self.tbwgt_content.clear()
        self.tbwgt_content.setColumnCount(3)  # 设定列数
        self.tbwgt_content.setHorizontalHeaderLabels(['时间','比赛','赛段'])  # 设置表头内容
        i = 0
        for row in range(0,len(args["content"])):
            self.tbwgt_content.setRowCount(row + 1)#设置行数
            self.tbwgt_content.setItem(i, 0, QTableWidgetItem(str(args['content'][i][0])))
            self.tbwgt_content.setItem(i, 1, QTableWidgetItem(str(args['content'][i][1])))
            # self.tbwgt_content.setItem(i, 2, QTableWidgetItem(str(args['content'][i][2])))
            i += 1

        self.column = self.tbwgt_content.columnCount()

class mod_judge(QWidget,c):
    def __init__(self, args):
        super(mod_judge, self).__init__()
        self.setupUi(self)
        self.args = args
        self.lbl_title.setText(args['judge'])
        self.tbwgt_content.setColumnCount(3)  # 设定列数
        self.tbwgt_content.setHorizontalHeaderLabels(['职位','姓名','单位'])  # 设置表头内容
        i = 0
        for row in range(0,len(args["content"])):
            self.tbwgt_content.setRowCount(row + 1)#设置行数
            self.tbwgt_content.setItem(i, 0, QTableWidgetItem(str(args['content'][i][0])))
            self.tbwgt_content.setItem(i, 1, QTableWidgetItem(str(args['content'][i][1])))
            self.tbwgt_content.setItem(i, 2, QTableWidgetItem(str(args['content'][i][2])))
            self.tbwgt_content.setItem(i, 3, QTableWidgetItem(str(args['content'][i][3])))
            i += 1

        self.column = self.tbwgt_content.columnCount()
        # self.tbwgt_content.resizeColumnsToContents()  # 与内容同宽

class mod_resultlist(QWidget,d):
    def __init__(self, args):
        super(mod_resultlist, self).__init__()
        self.setupUi(self)
        self.args = args
        self.lbl_title.setText(args["r_list"])
        self.tbwgt_content.setColumnCount(5)  # 设定列数
        self.tbwgt_content.setHorizontalHeaderLabels(['名次','姓名','成绩','马名','单位'])  # 设置表头内容
        register = eval(args['content'])#字符串转列表
        i = 0
        for row in range(0,len(register)):
            self.tbwgt_content.setRowCount(row + 1)#设置行数
            self.tbwgt_content.setItem(i, 0, QTableWidgetItem(str(register[i][6])))
            self.tbwgt_content.setItem(i, 1, QTableWidgetItem(str(register[i][1])))
            self.tbwgt_content.setItem(i, 2, QTableWidgetItem(str(register[i][2])))
            self.tbwgt_content.setItem(i, 3, QTableWidgetItem(str(register[i][7])))
            self.tbwgt_content.setItem(i, 4, QTableWidgetItem(str(register[i][3])))
            i += 1

        self.column = self.tbwgt_content.columnCount()

class mod_ranklist(QWidget,g):
    def __init__(self, args):
        super(mod_ranklist, self).__init__()
        self.setupUi(self)
        self.args = args
        self.lbl_title.setText(args["k_list"])
        self.tbwgt_content.setColumnCount(5)  # 设定列数
        self.tbwgt_content.setHorizontalHeaderLabels(['名次','姓名','成绩','马名','单位'])  # 设置表头内容
        register = args['content']#字符串转列表
        i = 0
        for row in range(0,len(register)):
            self.tbwgt_content.setRowCount(row + 1)#设置行数
            self.tbwgt_content.setItem(i, 0, QTableWidgetItem(str(register[i][6])))
            self.tbwgt_content.setItem(i, 1, QTableWidgetItem(str(register[i][1])))
            self.tbwgt_content.setItem(i, 2, QTableWidgetItem(str(register[i][2])))
            self.tbwgt_content.setItem(i, 3, QTableWidgetItem(str(register[i][7])))
            self.tbwgt_content.setItem(i, 4, QTableWidgetItem(str(register[i][3])))
            i += 1

        self.column = self.tbwgt_content.columnCount()

class mod_medal(QWidget,h):
    def __init__(self, args):
        super(mod_medal, self).__init__()
        self.setupUi(self)
        self.args = args
        self.lbl_title.setText(args["medal"])
        self.tbwgt_content.setColumnCount(5)  # 设定列数
        self.tbwgt_content.setHorizontalHeaderLabels(['名次','姓名','成绩','马名','单位'])  # 设置表头内容
        register = args['content']#字符串转列表
        i = 0
        for row in range(0,len(register)):
            self.tbwgt_content.setRowCount(row + 1)#设置行数
            self.tbwgt_content.setItem(i, 0, QTableWidgetItem(str(register[i][6])))
            self.tbwgt_content.setItem(i, 1, QTableWidgetItem(str(register[i][1])))
            self.tbwgt_content.setItem(i, 2, QTableWidgetItem(str(register[i][2])))
            self.tbwgt_content.setItem(i, 3, QTableWidgetItem(str(register[i][7])))
            self.tbwgt_content.setItem(i, 4, QTableWidgetItem(str(register[i][3])))
            i += 1

        self.column = self.tbwgt_content.columnCount()



class mod_startlist(QWidget,e):
    def __init__(self, args):
        super(mod_startlist, self).__init__()
        self.setupUi(self)
        self.args = args
        self.lbl_title.setText(args['startlist'])
        self.tbwgt_content.setColumnCount(5)  # 设定列数
        self.tbwgt_content.setHorizontalHeaderLabels(['名次','姓名','马名','单位'])  # 设置表头内容
        i = 0
        for row in range(0,len(args["content"])):
            self.tbwgt_content.setRowCount(row + 1)#设置行数
            self.tbwgt_content.setItem(i, 0, QTableWidgetItem(str(args['content'][i][0])))
            self.tbwgt_content.setItem(i, 1, QTableWidgetItem(str(args['content'][i][1])))
            self.tbwgt_content.setItem(i, 2, QTableWidgetItem(str(args['content'][i][2])))
            self.tbwgt_content.setItem(i, 3, QTableWidgetItem(str(args['content'][i][5])))
            i += 1

        self.column = self.tbwgt_content.columnCount()

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

    # args =  {
    #     "result" :"盛装舞步预赛",
    #     "data":
    #         [
    #             {"sport": "盛装舞步","event":"资格赛",
    #              "order":"3","rank": "1","name":"廖杰","city":"山西","horse":"火龙驹","result":"343.33",
    #              "E":"23","M":"123","C":"242","P":"234"}
    #         ],
    #     "content":
    #         [   {"order":"1","name":"吉喆","result":"222","city":"山东"},
    #             {"order":"2","name":"吉喆","result":"222","city":"山东"},
    #             {"order":"3","name":"吉喆","result":"222","city":"山东"}
    #         ]
    # }

    app = QApplication(sys.argv)
    demo = mod_resultlist(args)
    demo.show()
    sys.exit(app.exec_())
