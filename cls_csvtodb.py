# -*- coding: utf-8 -*-
import pymssql
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView
import csv

class InputCSV(object):
    """docstring for ClassName"""
    def __init__(self, arg):
        super(InputCSV, self).__init__()
        self.arg = arg
#1
    def readfile(filename):
        rows = []
        with open(filename, 'r',encoding='utf-8') as f:
            reader = csv.reader(f)
            # print(type(reader))
            for row in reader:
                rows.append(row)
        return rows

    def writefile(filename,params):
        with open(filename,'w',encoding='gbk') as f:
            csv_writer = csv.writer(f)
            for row in params:
                csv_writer.writerow(row)
        f.close()


class open_db(object):
    __stance = None
    __Flag = False

    def __new__(cls, *args, **kwargs):
        # 初始化一个实例
        if cls.__stance is None:
            cls.__stance = super().__new__(cls)
        # 返回给__init__实例
        return cls.__stance

    def __init__(self, server, user, password, database):
        if not open_db.__Flag:
            open_db.__Flag = True
        self.conn = pymssql.connect(server, user, password, database)
        self.cursor = self.conn.cursor()

    def __enter__(self):
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()


class get_Results(object):
    def __init__(self):
        super().__init__()
        self.description = []
        self.conn = {"server": '127.0.0.1', "user": 'sa', "password": '111', "database": 'db_demo'}
    
    def get_sport(param):
        return f"exec Proc_GetSports @LanguageCode={param[0]}"

    def add_sport(param):
        return f""" exec proc_AddSport 
                        @SportCode={param[0]},
                        @OpenDate={param[1]},
                        @CloseDate={param[2]},
                        @Order={param[3]},
                        @SportInfo={param[4]},
                        @languageCode={param[5]},
                        @SportLongName={param[6]},
                        @SportShortName={param[7]},
                        @SportComment={param[8]},
                        @SportConfigValue={param[9]},
                        @Result={param[10]}
                """

    def update_sport(param):
        return f"""exec proc_EditSport
                            @Order='{param[0]}',
                            @SportCode='{param[1]}',
                            @SportLongName='{param[2]}',
                            @SportShortName='{param[3]}',
                            @OpenDate='{param[4]}',
                            @CloseDate='{param[5]}',
                            @SportID='{param[6]}',
                            @SportInfo='{param[7]}',
                            @languageCode='{param[8]}',
                            @SportComment='{param[9]}',
                            @SportConfigValue='{param[10]}',
                            @result = {param[11]} """

    def del_sport(param):
        return f""" exec proc_DelSport
                    @SportID={param[0]},
                    @Result={param[0]}"""

    def proc_AddDiscipline(param):
        return f"""EXEC proc_AddDiscipline @SportID={param[0]},@DisciplineID={param[1]},
                       @Order={param[2]},@DisciplineInfo={param[3]},@DisciplineLongName={param[4]},
                       @DisciplineShortName={param[5]},@DisciplineComment={param[6]},
                       @Result={param[7]}, @LanguageCode={param[8]}"""

    def get_sportDisciplines(param):
        return f"""EXEC Proc_GetSportDisciplines @SportID={param[0]},
                        @LanguageCode={param[1]}"""

    def get_Languages(param):
        return f""" EXEC Proc_GetLanguages """

    def get_venuelist(param):
        return f"EXEC  Proc_GetVenueList @DisciplineCode={param[0]}"

    def get_disciplineEvents(param):
        return f"""EXEC Proc_GetDisciplineEvents @DisciplineID={param[0]},
                        @LanguageCode={param[1]}"""

    def del_disciplineEvents(param):
        pass
        # return f"""EXEC Proc_GetDisciplineEvents @DisciplineID={param[0]},
        #                 @LanguageCode={param[1]}"""

    def get_IRMs(param):
        return f"""EXEC Proc_GetIRMs @DisciplineID={param[0]},
                        @LanguageCode={param[1]}"""

    def get_Functions(param):
        return f"""EXEC Proc_GetFunctions @DisciplineID={param[0]},
                        @LanguageCode={param[1]}"""

    def add_Function(param):
        return f"""EXEC Proc_AddFunction @DisciplineID={param[0]},@FunctionLongName={param[1]},
                       @FunctionShortName={param[2]},@FunctionComment={param[3]},
                       @FunctionCode={param[4]}, @FunctionCategoryCode={param[5]},
                       @Result={param[6]},@LanguageCode={param[7]}"""

    def edit_Function(param):
        return f"""EXEC Proc_EditFunction @DisciplineID={param[0]},@FunctionLongName={param[1]},
                       @FunctionShortName={param[2]},@FunctionComment={param[3]},
                       @FunctionCode={param[4]}, @FunctionCategoryCode={param[5]},
                       @Result={param[6]},@LanguageCode={param[7]},@FunctionID=={param[8]}"""

    def del_Function(param):
        return f"""EXEC Proc_DelFunction @FunctionID={param[0]},@Result={param[1]}"""

    def get_Positions(param):
        return f"""EXEC Proc_GetPositions @DisciplineID={param[0]},
                        @LanguageCode={param[1]}"""

    def add_Position(param):
        return f"""EXEC Proc_AddPosition @DisciplineID={param[0]},@PositionLongName={param[1]},
                       @PositionShortName={param[2]},@PositionComment={param[3]},
                       @PositionCode={param[4]},@Result={param[5]},@LanguageCode={param[6]}"""

    def edit_Position(param):
        return f"""EXEC Proc_EditPosition @DisciplineID={param[0]},@PositionLongName={param[1]},
                       @PositionShortName={param[2]},@PositionComment={param[3]},
                       @PositionCode={param[4]},@Result={param[5]},@LanguageCode={param[6]},@PositionID={param[7]}"""

    def del_Position(param):
        return f"""EXEC Proc_DelPosition @PositionID={param[0]},@Result={param[1]}"""

    def edit_SportActive(param):
        return f"""EXEC Proc_UpdateSportActive @LanguageCode={param[0]},@Active={param[1]},
                        @Result={param[2]}"""

    def edit_LanguageActive(param):
        return f"""EXEC Proc_UpdateLanguageActive @SportID={param[0]},@Active={param[1]},
                        @Result={param[2]}"""

    def edit_DisciplineActive(param):
        return f"""EXEC Proc_UpdateDisciplineActive @DisciplineID={param[0]},@Active={param[1]},
                        @Result={param[2]}"""

    def GetDisciplineAthletes(param):
        return f"exec Proc_InitialDownload_GetDisciplineAthletes @DisciplineCode={param[0]}"

    def clear_athletes(param):
        return f"exec Proc_InitialDownload_GetDisciplineAthletes "

    def Proc_GetOperatorsInfo(param):
        return f"""EXEC Proc_GetOperatorsInfo """

    def Proc_GetOperatorRoles(param):
        return f"""EXEC Proc_GetOperatorRoles @PersonID={param[0]}"""

    def get_default(param):
        return "Looking forward to the Weekend"

    def DelRegisterByDiscipline(param):
        return f"""DECLARE @return_value int exec Proc_InitialDownload_DelRegisterByDiscipline 
                @DisciplineID = {param[0]}, @Result=@return_value select @return_value"""

    def IntiTempRegisterTable(param):
        return f"""DECLARE @Result int EXEC Proc_InitialDownload_IntiTempRegisterTable @Result output
                select @Result"""

    def Insert2TempTable(param):
        # i = 0
        # for x in param:
        #      param[i] = x if x != '' else "N''"
        #      i += 1

        return f"""DECLARE @Result int  exec Proc_InitialDownload_Insert2TempTable
        @DisciplineCode = N'{param[0]}',
        @Field1 = N'{param[1]}',
        @Field2 = N'{param[2]}',
        @Field3 = N'{param[3]}',
        @Field4 = N'{param[4]}',
        @Field5 = N'{param[5]}',
        @Field6 = N'{param[6]}',
        @Field7 = N'{param[7]}',
        @Field8 = N'{param[8]}',
        @Field9 = N'{param[9]}',
        @Field10 = N'{param[10]}',
        @Field11 = N'{param[11]}',
        @Field12 = N'{param[12]}',
        @Field13 = N'{param[13]}',
        @Field14 = N'{param[14]}',
        @Field15 = N'{param[15]}',
        @Field16 = N'{param[16]}',
        @Field17 = N'{param[17]}',
        @Field18 = N'{param[18]}',
        @Field19 = N'{param[19]}',
        @Field20 = N'{param[20]}',
        @Result= @Result output 
        select @Result"""

    def UpdateRegister2DB(param):
        return f"""DECLARE @Result int 
        exec Proc_InitialDownload_UpdateRegister2DB
        @DisciplineCode = N'{param[0]}',
        @Result = @Result output
                select @Result"""

    def IntiTempUnOfficialTable(param):
        return f"""DECLARE @Result int 
                exec Proc_InitialDownload_IntiTempUnOfficialTable
                @Result = @Result output
                select @Result"""

    def InsertUnOfficials2TempTable(param):
        # i = 0
        # for x in param:
        #      y = x if x != '' else ' '
        #      param[i]=y
        #      i += 1
        return f"""DECLARE @Result int 
        exec Proc_InitialDownload_InsertUnOfficials2TempTable
        @DisciplineCode = N'{param[0]}',
        @Field1 = N'{param[1]}',
        @Field2 = N'{param[2]}',
        @Field3 = N'{param[3]}',
        @Field4 = N'{param[4]}',
        @Field5 = N'{param[5]}',
        @Field6 = N'{param[6]}',
        @Field7 = N'{param[7]}',
        @Field8 = N'{param[8]}',
        @Field9 = N'{param[9]}',
        @Field10 = N'{param[10]}',
        @Field11 = N'{param[11]}',
        @Field12 = N'{param[12]}',
        @Result=@Result output
        select @Result"""

    def UpdateUnOfficials2DB(param):
        return f"""DECLARE @Result int 
        exec Proc_InitialDownload_AutoSwitch_UpdateUnOfficials2DB
        @DisciplineCode = N'{param[0]}',
        @Result=@Result output
        select @Result"""


    switcher = {
        'UpdateUnOfficials2DB':UpdateUnOfficials2DB,
        'InsertUnOfficials2TempTable':InsertUnOfficials2TempTable,
        'IntiTempUnOfficialTable':IntiTempUnOfficialTable,
        'UpdateRegister2DB':UpdateRegister2DB,
        'Insert2TempTable':Insert2TempTable,
        'IntiTempRegisterTable':IntiTempRegisterTable,
        'DelRegisterByDiscipline':DelRegisterByDiscipline, 
        'GetDisciplineAthletes':GetDisciplineAthletes,
        'edit_SportActive': edit_SportActive,
        'edit_LanguageActive': edit_LanguageActive,
        'edit_DisciplineActive': edit_DisciplineActive,
        'get_sport': get_sport,
        'add_sport': add_sport,
        'update_sport': update_sport,
        'del_sport': del_sport,
        'get_venuelist': get_venuelist,
        'get_disciplineEvents': get_disciplineEvents,
        'del_disciplineEvents': del_disciplineEvents,
        'get_sportDisciplines': get_sportDisciplines,
        'get_Languages': get_Languages,
        'get_IRMs': get_IRMs,
        'get_Functions': get_Functions,
        'add_Function': add_Function,
        'edit_Function': edit_Function,
        'del_Function': del_Function,
        'get_Positions': get_Positions,
        'add_Position': add_Position,
        'edit_Position': edit_Position,
        'del_Position': del_Position,
        'Proc_GetOperatorsInfo': Proc_GetOperatorsInfo,
        'Proc_GetOperatorRoles': Proc_GetOperatorRoles
    }

    def get_SQL_results(self, tablewidget, operate_name, params):
        """
        加载数据到表控件上，执行Proc_GetSports存储过程，输入语言类型CHN.
        :operate_name:sql 名称
        :params:sql 参数
        :return:数据集
        """
        results = self.do_field(operate_name, params)
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
        tablewidget.resizeColumnsToContents()  # 与内容同宽
        tablewidget.resizeRowsToContents()  # 设置行列高宽与内容匹配
        tablewidget.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 不可编辑
        tablewidget.setSelectionBehavior(QAbstractItemView.SelectRows)  # 单行选择
        tablewidget.setContextMenuPolicy(Qt.CustomContextMenu)  # 允许右键产生子菜单
        return results

    def do_field(self, operation, param):
        self.results = []
        self.description = []
        with open_db(self.conn['server'], self.conn['user'], self.conn['password'], self.conn['database']) as db:
            db.execute(self.switcher.get(operation)(param))

            self.results = db.fetchall()  # 得到结果集

            for field in db.description:
                self.description.append(field[0])
        return {'desc': self.description, 'results': self.results}

    def do(self, operation, param):
        with open_db(self.conn['server'], self.conn['user'], self.conn['password'], self.conn['database']) as db:
            print(self.switcher.get(operation, self.get_default)(param))
            db.execute(self.switcher.get(operation, self.get_default)(param))
            
            self.results = db.fetchall()  # 得到结果集
        return self.results

    def do_one(self, operation, param):
        self.results=0
        with open_db(self.conn['server'], self.conn['user'], self.conn['password'], self.conn['database']) as db:
            db.execute(self.switcher.get(operation, self.get_default)(param))
            self.results = db.fetchone()  # 得到结果值
        return self.results

class doProdure(object):
    """docstring for doProdure"""
    def __init__(self, arg):
        super(doProdure, self).__init__()
        self.arg = arg

    def OnBnExportAthletes():
        x = get_Results()
        y = x.do('GetDisciplineAthletes',["eq"])
        print(y)

    def OnBtnCleanAthletes():
        x = get_Results()
        y = x.do('DelRegisterByDiscipline',[1])
        print(y)
    
    def OnBtnImportAthletes():

        x = get_Results()
        y = x.do('IntiTempRegisterTable',["eq"])  #初始化临时表人员和报项信息导入成功
        print(y)
        params = InputCSV.readfile("equestrain.csv")
        for param in params:
            param.insert(0,"eq") #插入代码在头一个单词
            print(param)
            y = x.do('Insert2TempTable',param) #将人员和报项信息导入到数据库中的临时表
        y = x.do('UpdateRegister2DB',['eq'])  #将临时表中的人员和报项信息更新到数据库中

    def OnBtnImportUnOfficals():
        x = get_Results()
        y = x.do('IntiTempUnOfficialTable',["eq"])    #初始化临时表非竞赛官员信息导入
        print(y)
        params = InputCSV.readfile("equestrain.csv")#将人员和报项信息导入到数据库中的临时表
        for param in params:
            param.insert(0,"eq")
            print(param)
            y = x.do('InsertUnOfficials2TempTable',param)
        y = x.do('UpdateUnOfficials2DB',['eq'])    #将临时表中的非竞赛官员信息导入更新到数据库中
        print(y)

if __name__ == '__main__':

    doProdure.OnBtnImportAthletes()
