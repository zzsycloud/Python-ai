class DBConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.is_open = False
        return cls._instance

    def __enter__(self):
        print("建立数据库连接")
        self.is_open = True
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_value is not None:
            print(f"捕获到异常：{exc_value}")
        print("关闭数据库连接")
        self.is_open = False
        return True

    def execute_sql(self, sql):
        if not self.is_open:
            print("无法执行SQL：数据库连接未打开")
            return
        print(f"执行SQL语句：{sql}")


conn1 = DBConnection()
conn2 = DBConnection()
print(f"conn1 is conn2 ? {conn1 is conn2}")

with conn1 as connection:
    connection.execute_sql("select * from student")
    1 / 0

conn1.execute_sql("select * from student")
