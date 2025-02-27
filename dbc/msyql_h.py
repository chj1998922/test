import pymysql
from settings import MYSQL_CONFIG, ENV

class MySQLConnection:
    def __init__(self, db_key):
        config = MYSQL_CONFIG[ENV][db_key]
        self.connection = pymysql.connect(
            host=config["host"],
            port=config["port"],
            user=config["user"],
            password=config["password"],
            database=config["database"],
        )

    def execute_query(self, query, params=None):
        """执行 SQL 查询"""
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()

    def close(self):
        """关闭连接"""
        self.connection.close()
