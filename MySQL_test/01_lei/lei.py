import mysql.connector

class MySQLHandler:
    """
    MySQLHandler 封装了对 MySQL 数据库的常见操作，
    包括从设置中读取配置、建立连接、查询、批量插入/更新以及建表操作。
    """
    def __init__(self, settings):
        # 从 settings 中获取配置，若未配置则使用默认值
        self.host = settings.get('host', 'localhost')
        self.port = settings.get('port', 3306)
        self.user = settings.get('user', 'root')
        self.password = settings.get('password', '')
        self.database = settings.get('database', None)
        self.conn = None
        self.cursor = None

    def connect(self):
        """建立数据库连接，并获取 cursor"""
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database,
                autocommit=False  # 关闭自动提交，可在操作后根据情况手动提交
            )
            # 使用 dictionary=True 使查询结果以字典形式返回
            self.cursor = self.conn.cursor(dictionary=True)
            print("数据库连接成功！")
        except mysql.connector.Error as err:
            print(f"数据库连接错误: {err}")
            raise

    def close(self):
        """关闭 cursor 与数据库连接"""
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        print("数据库连接已关闭。")

    def execute_query(self, query, params=None):
        """
        执行 INSERT/UPDATE/DELETE 等修改性操作的 SQL 语句，
        成功后提交事务，失败时回滚。
        """
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
        except mysql.connector.Error as err:
            self.conn.rollback()
            print(f"SQL 执行错误: {err}")
            raise

    def fetch_all(self, query, params=None):
        """
        执行查询 SQL 语句，并返回所有结果
        """
        try:
            self.cursor.execute(query, params)
            result = self.cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            print(f"查询错误: {err}")
            raise

    def insert_bulk(self, table, columns, data):
        """
        批量插入数据
        :param table: 表名
        :param columns: 字段列表，例如 ['username', 'email']
        :param data: 数据列表，每个元素是一个 tuple，表示一行数据
        """
        cols = ', '.join(columns)
        placeholders = ', '.join(['%s'] * len(columns))
        query = f"INSERT INTO {table} ({cols}) VALUES ({placeholders})"
        try:
            self.cursor.executemany(query, data)
            self.conn.commit()
            print(f"成功插入 {self.cursor.rowcount} 条数据。")
        except mysql.connector.Error as err:
            self.conn.rollback()
            print(f"批量插入错误: {err}")
            raise

    def update_bulk(self, table, update_field, new_value, condition_field, condition_value_list):
        """
        批量更新数据示例
        :param table: 表名
        :param update_field: 需要更新的字段名称
        :param new_value: 更新后的值
        :param condition_field: WHERE 条件字段
        :param condition_value_list: 满足条件的值列表
        该方法将对 condition_field 值在 condition_value_list 内的记录进行更新。
        """
        placeholders = ', '.join(['%s'] * len(condition_value_list))
        query = f"UPDATE {table} SET {update_field} = %s WHERE {condition_field} IN ({placeholders})"
        params = [new_value] + condition_value_list
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
            print(f"成功更新 {self.cursor.rowcount} 条数据。")
        except mysql.connector.Error as err:
            self.conn.rollback()
            print(f"批量更新错误: {err}")
            raise

    def create_table(self, create_table_sql):
        """
        创建表操作，传入完整的建表 SQL 语句。
        """
        try:
            self.cursor.execute(create_table_sql)
            self.conn.commit()
            print("表创建成功。")
        except mysql.connector.Error as err:
            self.conn.rollback()
            print(f"建表错误: {err}")
            raise

# 示例：其他模块可以频繁调用此类
if __name__ == '__main__':
    # 配置参数可以从 settings 文件中读取，这里直接用字典举例
    settings = {
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'password': 'yourpassword',  # 替换为你的数据库密码
        'database': 'testdb'
    }
    db_handler = MySQLHandler(settings)
    db_handler.connect()

    # 示例：创建一个用户表
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) NOT NULL,
        email VARCHAR(100) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """
    db_handler.create_table(create_table_sql)

    # 示例：批量插入数据
    user_data = [
        ('alice', 'alice@example.com'),
        ('bob', 'bob@example.com'),
        ('charlie', 'charlie@example.com')
    ]
    db_handler.insert_bulk('users', ['username', 'email'], user_data)

    # 示例：查询数据
    results = db_handler.fetch_all("SELECT * FROM users")
    print("查询结果：", results)

    # 示例：批量更新，假设将用户名为 bob 和 charlie 的用户更新为 'updated'
    db_handler.update_bulk('users', 'username', 'updated', 'username', ['bob', 'charlie'])

    # 再次查询结果
    results = db_handler.fetch_all("SELECT * FROM users")
    print("更新后查询结果：", results)

    db_handler.close()
