
import pymssql
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView
import csv
from func_json import *

            
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
    def __init__(self,args):
        super().__init__()
        self.description = []
        self.conn = {"server": args['dbserver'], "user": args['dbuser'], "password": args['dbpwd'], 
                    "database": args['dbdatabase']}

    def get_sport(param):
        return f"exec Proc_GetSports @LanguageCode={param[0]}"

    def get_sportDisciplines(param):
        return f"""EXEC Proc_GetSportDisciplines @SportID={param[0]},
                        @LanguageCode={param[1]}"""

    def get_disciplineEvents(param):
        return f"""EXEC Proc_GetDisciplineEvents @DisciplineID={param[0]},
                        @LanguageCode={param[1]}"""

    def get_Proc_EQ_GetIPadScoreList(param):
        return f"""exec Proc_EQ_GetIPadScoreList 
                    @MatchID='{param[0]}',
                    @RegisterID='{param[1]}',
                    @JudgeNum='{param[2]}',
                    @LanguageCode='{param[3]}'
                    """

    def get_Proc_AutoSwitch_SearchMatches(param):
        #--场次列表
        return f""" exec Proc_AutoSwitch_SearchMatches 
                    @DisciplineCode='{param[0]}',
                    @EventID='{param[1]}',
                    @DateTime='{param[2]}',
                    @VenueID='{param[3]}',
                    @PhaseID='{param[4]}',
                    @CourtID='{param[5]}'
                """

    def get_Proc_EQ_GetMatchResultList(param):
        return f"""exec Proc_EQ_GetMatchResultList 
                    @MatchID='{param[0]}',
                    @ShowFrom='{param[1]}',
                    @LanguageCode='{param[2]}'
                """
    def get_Proc_EQ_GetMatchResultDetailList(param): 
        return f"""exec Proc_EQ_GetMatchResultDetailList 
                    @MatchID='{param[0]}',
                    @RegisterID='{param[1]}'
                """

    def get_venuelist(param):
        return f"EXEC  Proc_GetVenueList @DisciplineCode={param[0]}"

    def get_Proc_Report_EQ_GetEventResult(param):
        #返回项目成绩
        return f"""exec Proc_Report_EQ_GetEventResult
                    @EventID='{param[0]}',
                    @LanguageCode='{param[1]}'
                    """
    def get_Proc_LED_EQ_GetCompetitionSchedule(param):
        # 返回竞赛日程表
        return f"""exec Proc_LED_EQ_GetCompetitionSchedule
                    @DisciplineID='{param[0]}',
                    @DateTime='{param[1]}',
                    @LanguageCode='{param[2]}'
                    """

    def get_Proc_Report_EQ_GetMatchInfo(param):
        """得到标题信息"""
        return f"""exec Proc_Report_EQ_GetMatchInfo
                    @MatchID='{param[0]}',
                    @LanguageCode='{param[1]}'
                """

    def get_Proc_EQ_GetMatchInfo(param):
        """得到标题信息"""
        return f"""exec Proc_EQ_GetMatchInfo
                    @MatchID='{param[0]}',
                    @LanguageCode='{param[1]}'
                """
    def get_Proc_Report_EQ_GetMatchJudges(param):
        return f"""exec Proc_Report_EQ_GetMatchJudges
                    @MatchID='{param[0]}',
                    @LanguageCode='{param[1]}'
                """

    def get_Proc_EQ_GetMatchOfficial(param):
        return f"""exec Proc_Report_EQ_GetMatchJudges
                    @MatchID='{param[0]}',
                    @LanguageCode='{param[1]}'
                """
    def get_Proc_EQ_GetMatchResultList(param):

        return f"""exec Proc_EQ_GetMatchResultList
                    @MatchID='{param[0]}',
                    @ShowFrom='{param[1]}',
                    @LanguageCode='{param[2]}'
                """
    def get_Proc_EQ_GetMFList(param):
        """得到步伐信息"""
        return f"""exec Proc_EQ_GetMFList
                    @MatchConfigID='{param[0]}',
                    @LanguageCode='{param[1]}'
                """
    def get_Proc_SCB_EQ_GetMatchInfo_LJ(param):
         return f"""exec Proc_SCB_EQ_GetMatchInfo_LJ
                    @EventID = '{param[0]}',
                    @LanguageCode='{param[1]}'
                """

    def get_Proc_SCB_GetEvents(param):
         return f"""exec Proc_SCB_GetEvents
                    @DisciplineCode='{param[0]}'
                """
    def get_Proc_SCB_EQ_GetSchedule(param):
        return f"""exec Proc_SCB_EQ_GetSchedule
                    @DateTime = '{param[0]}',
                    @LanguageCode='{param[1]}'
                """
    def get_Proc_SCB_EQ_GetJudgeList(param):
        return f"""exec Proc_SCB_EQ_GetJudgeList
                    @MatchID='{param[0]}',
                    @LanguageCode='{param[1]}'
                """

    def get_Proc_SCB_EQ_GetStartList(param):
        return f"""exec Proc_SCB_EQ_GetStartList
                    @MatchID='{param[0]}',
                    @LanguageCode='{param[1]}'
                """
    def get_Proc_SCB_EQ_GetMatchResultList(param):
        return f"""exec Proc_SCB_EQ_GetMatchResultList
                    @MatchID='{param[0]}',
                    @LanguageCode='{param[1]}'
                """

    def get_Proc_SCB_EQ_GetMatchRegisterList(param):
        return f"""exec Proc_SCB_EQ_GetMatchRegisterList
                    @MatchID='{param[0]}',
                    @LanguageCode='{param[1]}'
                """
    def get_Proc_SCB_EQ_GetDRRiderResult(param):
        return f"""exec Proc_SCB_EQ_GetDRRiderResult
                    @MatchID='{param[0]}',
                    @RegisterID='{param[1]}',
                    @IsCut='{param[2]}',
                    @LanguageCode='{param[3]}'
                """
    def get_Proc_SCB_EQ_GetMedalList(param):
        return f"""exec Proc_SCB_EQ_GetMedalList
                    @EventID='{param[0]}',
                    @LanguageCode='{param[1]}'
                """
    def get_Proc_SCB_EQ_GetMatchMovementList(param):
        return f"""exec Proc_SCB_EQ_GetMatchMovementList
                    @MatchID='{param[0]}',
                    @LanguageCode='{param[1]}'
                """
    def get_Proc_EQ_InitialDownload_InsertRiderHorse2DB_LJ(param):
        return f"""exec Proc_EQ_InitialDownload_InsertRiderHorse2DB_LJ
                """
    def get_Proc_InitialDownload_Insert2sheet(param):
        return f"""DECLARE @Result int exec Proc_InitialDownload_Insert2sheet
                    @Field1='{param[0]}',
                    @Field2='{param[1]}',
                    @Field3='{param[2]}',
                    @Field4='{param[3]}',
                    @Field5='{param[4]}',
                    @Field6='{param[5]}',
                    @Field7='{param[6]}',
                    @Field8='{param[7]}',
                    @Field9='{param[8]}',
                    @Field10='{param[9]}',
                    @Result=@Result output
                    select @Result"""
    def get_default(param):
        pass

    switcher = {
        'get_sport': get_sport,
        'get_Proc_SCB_EQ_GetMatchMovementList':get_Proc_SCB_EQ_GetMatchMovementList,
        'get_Proc_SCB_EQ_GetMedalList':get_Proc_SCB_EQ_GetMedalList,
        'get_Proc_SCB_EQ_GetDRRiderResult':get_Proc_SCB_EQ_GetDRRiderResult,
        'get_Proc_SCB_EQ_GetMatchRegisterList':get_Proc_SCB_EQ_GetMatchRegisterList,
        'get_Proc_SCB_EQ_GetMatchResultList':get_Proc_SCB_EQ_GetMatchResultList,
        'get_Proc_SCB_EQ_GetStartList':get_Proc_SCB_EQ_GetStartList,
        'get_Proc_SCB_EQ_GetJudgeList':get_Proc_SCB_EQ_GetJudgeList,
        'get_Proc_SCB_EQ_GetSchedule':get_Proc_SCB_EQ_GetSchedule,
        'get_Proc_SCB_GetEvents': get_Proc_SCB_GetEvents,
        'get_disciplineEvents': get_disciplineEvents,
        'get_sportDisciplines': get_sportDisciplines,
        "get_Proc_EQ_GetMFList" : get_Proc_EQ_GetMFList,
        "get_Proc_SCB_EQ_GetMatchInfo_LJ" : get_Proc_SCB_EQ_GetMatchInfo_LJ,
        "get_Proc_EQ_GetMatchOfficial":get_Proc_EQ_GetMatchOfficial,
        "get_Proc_Report_EQ_GetMatchJudges":get_Proc_Report_EQ_GetMatchJudges,
        "get_Proc_Report_EQ_GetMatchInfo":get_Proc_Report_EQ_GetMatchInfo,
        "get_Proc_EQ_GetMatchInfo":get_Proc_EQ_GetMatchInfo,
        "get_Proc_Report_EQ_GetEventResult" : get_Proc_Report_EQ_GetEventResult,
        "get_Proc_EQ_GetIPadScoreList" :get_Proc_EQ_GetIPadScoreList,
        'get_Proc_AutoSwitch_SearchMatches': get_Proc_AutoSwitch_SearchMatches,
        'get_Proc_EQ_GetMatchResultList': get_Proc_EQ_GetMatchResultList,
        "get_Proc_EQ_GetMatchResultDetailList":get_Proc_EQ_GetMatchResultDetailList,
        "get_Proc_EQ_InitialDownload_InsertRiderHorse2DB_LJ":get_Proc_EQ_InitialDownload_InsertRiderHorse2DB_LJ,
        "get_Proc_InitialDownload_Insert2sheet":get_Proc_InitialDownload_Insert2sheet,
        "get_Proc_LED_EQ_GetCompetitionSchedule":get_Proc_LED_EQ_GetCompetitionSchedule,
        "get_default": get_default
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
        #返回json格式的文本
        # return strtojs_format({'desc': self.description, 'results': self.results})
        return ({'desc': self.description, 'results': self.results})

    def do(self, operation, param):
        with open_db(self.conn['server'], self.conn['user'], self.conn['password'], self.conn['database']) as db:
            db.execute(self.switcher.get(operation, self.get_default)(param))
            self.results = db.fetchall()  # 得到结果集
        
        #返回json格式的文本
        return (self.results)
        # return strtojs_format(self.results)

    def exesql(self, operation):
        with open_db(self.conn['server'], self.conn['user'], self.conn['password'], self.conn['database']) as db:
            db.execute(operation)


if __name__ == '__main__':
    args = {"dbserver":".","dbport":"1433","dbuser":"sa","dbpwd":"111","dbdatabase":"bj_eq"}
    x = get_Results(args)
    # y = x.do_field('get_venuelist', ['1'])
    # y = x.do_field('get_Proc_EQ_GetIPadScoreList', ['1','1324','2','chn'])
    # y = x.do_field('get_Proc_AutoSwitch_SearchMatches ', ['EQ','-1','全部','-1','-1','-1'])
    # y = x.do_field('get_Proc_EQ_GetMatchResultDetailList', ['2','4958'])

    # y = x.do('get_Proc_Report_EQ_GetEventResult', ['1','chn'])
    # y = x.do_field('get_Proc_EQ_GetMatchInfo', ['1','chn'])
    # print(y)
    # y = x.do_field('get_Proc_Report_EQ_GetMatchInfo', ['1','chn'])
    # y = x.do_field('get_Proc_Report_EQ_GetMatchJudges', ['1','chn'])
    # y = x.do_field('get_Proc_EQ_GetMatchOfficial', ['1','chn'])
    # y = x.do_field('get_Proc_EQ_GetMFList', ['1','chn'])
    # y = x.do_field('get_Proc_SCB_EQ_GetSchedule', ['1','chn'])
    # y = x.do_field('get_Proc_SCB_EQ_GetMatchInfo_LJ', ['1','chn'])
    # y = x.do_field('get_sport', ['chn'])
    # y = x.do_field('get_sportDisciplines', ['1','chn'])
    # y = x.do_field('get_Proc_SCB_GetEvents', ['eq'])
    # y = x.do_field('get_disciplineEvents', ['1','chn'])
    # y = x.do_field('get_Proc_EQ_GetMatchResultList', ['1','1','chn'])
    # y = x.do_field('get_Proc_SCB_EQ_GetMatchResultList', ['1','chn'])
    # y = x.do_field('get_Proc_SCB_EQ_GetMatchRegisterList', ['1','chn'])
    # y = x.do_field('get_Proc_SCB_EQ_GetDRRiderResult', ['1','7966','0','chn'])
    y = x.do_field('get_Proc_SCB_EQ_GetMedalList', ['1','chn'])
    # y = x.do_field('get_Proc_SCB_EQ_GetMatchMovementList', ['1','chn'])
    # y = x.do_field('get_Proc_EQ_InitialDownload_InsertRiderHorse2DB_LJ',[''])
    # y = x.do_field('get_Proc_InitialDownload_Insert2sheet',['1','法国','个人','廖杰','','Corrinne Solyst','10','','','A'])
    # y = x.do_field('get_Proc_LED_EQ_GetCompetitionSchedule',[1, 'ALL', 'CHN', 1])
    # x.exesql('truncate table Sheet1$')
    
    print(y)
