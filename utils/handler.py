from sqlalchemy import create_engine
import pandas as pd

class MysqlHelper:
    def __init__(self):
        # 初始化数据库连接，使用pymysql模块
        db_info = {
            'user': "root",
            'password': "*",
            'host': "*",
            'port': 3306,
            'database': "invest"
        }
        self.engine = create_engine(
            'mysql+pymysql://%(user)s:%(password)s@%(host)s:%(port)d/%(database)s?charset=utf8' % db_info,
            encoding='utf-8')

    def get_engine(self):
        return self.engine


class DataHelper:
    def __init__(self, engine):
        self.conn = engine

    def get_single(self, name, begin, end):
        sql = f'select * from {name} where trade_date >= {begin} and trade_date <= {end}'
        t = pd.read_sql(sql=sql, con=self.engine).drop('index', axis=1)
        return t

    def get_multi(self, names, begin, end):
        re = {}
        for name in names:
            re[name] = self.get_single(name, begin, end)
        return re
