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

class mod_ranklist(QWidget,d):
    def __init__(self, args):
        super(mod_ranklist, self).__init__()
        self.setupUi(self)
        self.args = args
        self.lbl_title.setText(args['ranklist'])
        self.tbwgt_content.setColumnCount(4)  # 设定列数
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
    args =	{
    "resultlist":"盛装舞步个人赛资格赛",
    "content":"[(19, '刘丽娜', 'Don Dinero', '新疆队', '17', '17', '1', '70.087', 1, 'Q', '70.087', None, '[Image]新疆队', '[Image]IRM_Q', '新疆队', '刘丽娜 / Don Dinero'), (26, '刘涛', 'Razida', '新疆队', '19', '19', '2', '70.043', 2, 'Q', '70.043', None, '[Image]新疆队', '[Image]IRM_Q', '新疆队', '刘涛 / Razida'), (22, '黄焯钦', '爱将', '广东队', '11', '11', '3', '68.683', 3, 'Q', '68.683', None, '[Image]广东队', '[Image]IRM_Q', '广东队', '黄焯钦 / 爱将'), (15, '顾兵', '玉面飞龙', '广东队', '12', '12', '4', '68.596', 4, 'Q', '68.596', None, '[Image]广东队', '[Image]IRM_Q', '广东队', '顾兵 / 玉面飞龙'), (11, '兰超', 'Weltroon', '新疆队', '18', '18', '5', '66.490', 5, 'Q', '66.490', None, '[Image]新疆队', '[Image]IRM_Q', '新疆队', '兰超 / Weltroon'), (7, '谭志勤', '如意', '广东队', '13', '13', '6', '65.262', 6, 'Q', '65.262', None, '[Image]广东队', '[Image]IRM_Q', '广东队', '谭志勤 / 如意'), (23, '贾海涛', '快乐舞伴', '浙江队', '6', '6', '7', '65.087', 7, 'Q', '65.087', None, '[Image]浙江队', '[Image]IRM_Q', '浙江队', '贾海涛 / 快乐舞伴'), (2, '黄丽兴', '洛克菲诺', '广东队', '14', '14', '8', '63.157', 8, 'Q', '63.157', None, '[Image]广东队', '[Image]IRM_Q', '广东队', '黄丽兴 / 洛克菲诺'), (1, '贾海涛', 'Corrinne Solyst', '浙江队', '10', '10', '9', '62.631', 9, 'Q', '62.631', None, '[Image]浙江队', '[Image]IRM_Q', '浙江队', '贾海涛 / Corrinne Solyst'), (8, '格日勒', 'Donneradel', '浙江队', '9', '9', '10', '62.280', 10, 'Q', '62.280', None, '[Image]浙江队', '[Image]IRM_Q', '浙江队', '格日勒 / Donneradel'), (5, '张红钊', '吉格乐', '新疆队', '20', '20', '11', '60.350', 11, 'Q', '60.350', None, '[Image]新疆队', '[Image]IRM_Q', '新疆队', '张红钊 / 吉格乐'), (13, '海米提·地力木热提', '瑞乌尔当斯', '新疆队', '21', '21', '12', '59.560', 12, 'Q', '59.560', None, '[Image]新疆队', '[Image]IRM_Q', '新疆队', '海米提·地力木热提 / 瑞乌尔当斯'), (10, '李兵', 'Germanik', '北京队', '27', '27', '13', '59.034', 13, 'Q', '59.034', None, '[Image]北京队', '[Image]IRM_Q', '北京队', '李兵 / Germanik'), (25, '米尔扎提·吐尔洪', 'Lullaby', '新疆队', '22', '22', '13', '59.034', 14, 'Q', '59.648', None, '[Image]新疆队', '[Image]IRM_Q', '新疆队', '米尔扎提·吐尔洪 / Lullaby'), (4, '王超', 'Del La Cruzz 2', '北京队', '28', '28', '15', '58.508', 15, 'Q', '58.508', None, '[Image]北京队', '[Image]IRM_Q', '北京队', '王超 / Del La Cruzz 2'), (6, '柯艳霞', '玉麒麟', '四川队', '1', '1', '15', '58.508', 16, 'Q', '58.508', None, '[Image]四川队', '[Image]IRM_Q', '四川队', '柯艳霞 / 玉麒麟'), (16, '和兵兵', 'Varanko V', '江苏队', '24', '24', '17', '57.456', 17, 'Q', '57.456', None, '[Image]江苏队', '[Image]IRM_Q', '江苏队', '和兵兵 / Varanko V'), (9, '包哈斯图力古尔', 'Lucky', '江苏队', '23', '23', '18', '57.280', 18, 'Q', '57.280', None, '[Image]江苏队', '[Image]IRM_Q', '江苏队', '包哈斯图力古尔 / Lucky'), (14, '胡子康', '八面玲珑', '广东队', '16', '16', '19', '54.912', 19, None, '54.912', None, '[Image]广东队', '', '广东队', '胡子康 / 八面玲珑'), (21, '赵玉龙', '清风', '北京队', '29', '29', '20', '54.824', 20, None, '54.999', None, '[Image]北京队', '', '北京队', '赵玉龙 / 清风'), (24, '蔡晓军', '舞蹈家', '北京队', '26', '26', '21', '54.034', 21, None, '54.034', None, '[Image]北京队', '', '北京队', '蔡晓军 / 舞蹈家'), (12, '蓝志豪', '小飞侠', '四川队', '2', '2', '22', '51.139', 22, None, '51.139', None, '[Image]四川队', '', '四川队', '蓝志豪 / 小飞侠'), (20, '黄敏康', '兰星', '四川队', '4', '4', '23', '50.964', 23, None, '50.964', None, '[Image]四川队', '', '四川队', '黄敏康 / 兰星'), (27, '黄伟力', '飞燕', '四川队', '5', '5', '24', '49.122', 24, None, '49.122', None, '[Image]四川队', '', '四川队', '黄伟力 / 飞燕')]"
}
    app = QApplication(sys.argv)
    demo = mod_resultlist(args)
    demo.show()
    sys.exit(app.exec_())
