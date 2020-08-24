
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
        self.conn = {"server": agrs['dbserver'], "user": agrs['dbuser'], "password": agrs['dbpwd'], 
                    "database": agrs['dbdatabase']}

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


    switcher = {
        "get_venuelist":get_venuelist,
        "get_Proc_EQ_GetIPadScoreList" :get_Proc_EQ_GetIPadScoreList,
        'get_Proc_AutoSwitch_SearchMatches': get_Proc_AutoSwitch_SearchMatches,
        'get_Proc_EQ_GetMatchResultList': get_Proc_EQ_GetMatchResultList,
        "get_Proc_EQ_GetMatchResultDetailList":get_Proc_EQ_GetMatchResultDetailList
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
        return strtojs_format({'desc': self.description, 'results': self.results})

    def do(self, operation, param):
        with open_db(self.conn['server'], self.conn['user'], self.conn['password'], self.conn['database']) as db:
            db.execute(self.switcher.get(operation, self.get_default)(param))
            self.results = db.fetchall()  # 得到结果集
        
        #返回json格式的文本
        return strtojs_format(self.results)


if __name__ == '__main__':
    agrs = {"dbserver":".","dbport":"1433","dbuser":"sa","dbpwd":"111","dbdatabase":"n_eq"}
    x = get_Results(agrs)
    # y = x.do_field('get_venuelist', ['1'])
    # y = x.do_field('get_Proc_EQ_GetIPadScoreList', ['1','1324','2','chn'])
    # y = x.do_field('get_Proc_AutoSwitch_SearchMatches ', ['EQ','-1','全部','-1','-1','-1'])
    y = x.do_field('get_Proc_EQ_GetMatchResultDetailList', ['2','4958'])

    print(y)
