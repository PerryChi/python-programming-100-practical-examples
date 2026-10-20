import os
import pymysql

class SimpleMysqlClass:
    def __init__(self, host, user, password, db_name):
        self.host = host
        self.user = user
        self.password = password
        self.db_name = db_name
        self.connection = self.create_connection()
        self.cursor = self.create_cursor()

    # 建立一个数据库连接
    def create_connection(self):
        self.connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.db_name)
        return self.connection

    # 建立一个游标
    def create_cursor(self):
        self.cursor = self.connection.cursor()
        return self.cursor

    # 执行查询
    def query_sql(self, sql):
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            return data
        except Exception:
            raise Exception('执行SQL语句: ' + sql + ', 出现异常，请检查')

    # 执行增删改相关SQL语句
    def execute(self, sql):
        try:
            re = self.cursor.execute(sql)
            self.connection.commit()
            return re
        except Exception:
            self.connection.rollback()
            return -1

    # 列出数据库中的表
    def list_tables(self):
        sql_1 = 'show tables'
        try:
            self.cursor.execute(sql_1)
            table_list = self.cursor.fetchall()
            return table_list
        except Exception:
            raise Exception('执行的SQL语句: ' + sql_1 + ', 出现异常，请检查！')

    # 关闭连接
    def close(self):
        self.connection.close()



if __name__ == '__main__':
    # 对类进行实例化
    mysql_obj = SimpleMysqlClass('localhost', 'root', os.getenv('DBPASSWORD'), 'example6_5')
    re = mysql_obj.query_sql('select * from person')
    for row in re:
        print('序号: ' + str(row[0]) + '姓名: ' + row[1] + '电子邮件: ' + row[2])

    add_count = mysql_obj.execute('insert into person(user, email) values("王好", "wanghao@163.com")')
    if add_count >= 1:
        print('增加人员成功！')
    else:
        print('增加人员失败！')

    del_count = mysql_obj.execute('delete from person where user="王好"')
    if del_count >= 0:
        print('删除记录' + str(del_count) + '条')
    else:
        print('出现错误！')

    table_names = mysql_obj.list_tables()
    print('数据库的表列举如下：')
    for name in table_names:
        print(name[0])

    # 关闭数据库连接，节省计算机资源
    mysql_obj.close()