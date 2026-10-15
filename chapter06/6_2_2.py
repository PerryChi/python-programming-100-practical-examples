import sqlite3

# 连接数据库的函数
def connect_db():
    # 连接数据库，参数制定数据库文件路径
    conn = sqlite3.connect('data.db')
    print('\n已连接上数据库···')
    # 随时关闭数据库连接
    conn.close()


# 执行SQL语句的函数
def run_sql(sql):
    with sqlite3.connect('data.db') as conn:
        # 生成一个cursor对象
        curs = conn.cursor()
        # 执行SQL语句
        curs.execute(sql)
        # 执行事务提交
        conn.commit()
        # 返回插入 删除 修改时影响到的记录数，以此怕段掺入或删除是否成功
        return curs.rowcount


# 在数据库中新建一张数据表
def create_table():
    # 建表的SQL语句
    vsql = '''
        create table if not exists person(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            name varchar2(10),
            sex char(2),
            age int,
            department varchar2(20),
            telephone varchar2(11),
            bz varchar(20)
        );
    '''
    # 调用函数执行SQL语句
    run_sql(vsql)
    print('\n用户信息表创建成功!')


# 采集用户信息
def person_info():
    vname = input("请登入姓名:")
    vsex = input("请登入性别:")
    vage = input("请登入年龄:")
    vdepartment = input("请登入部门:")
    vtelephone = input("请登入电话:")
    vbz = input("请登入备注说明:")
    # 组合成SQL语句
    vsql = 'insert into person(name, sex, age, department, telephone, bz) values ("'\
            + vname + '","' + vsex + '","' + vage + '","'\
            + vdepartment + '","' + vtelephone + '","' + vbz + \
        '")'
    print(vsql)
    # 返回SQL语句
    return vsql


# 增加一条记录
def add_row():
    # 调用函数，取得SQL语句
    vsql = person_info()
    # 调用函数执行SQL语句，并取得返回值
    vcount = run_sql(vsql)
    # 如果返回值等于1，说明插入一条记录
    if (vcount == 1):
        print('\n人员信息增加成功!')
    else:
        print('\n人员信息增加失败!')


# 删除一条记录
def del_row():
    vname = input("请录入要删除的人员的姓名:")
    # 按照姓名条件，结合成删除记录的SQL语句
    vsql = 'delete from person where name="'+ vname +'"'
    # 执行SQL语句，并取得返回值
    vcount = run_sql(vsql)
    # 如何返回值等于1，说明删除了一条记录
    if vcount == 1:
        print("\n人员信息删除成功！")
    else:
        print("\n人员信息删除失败！")


# 显示数据表中所有数据
def list():
    vsql = 'select * from person'
    with sqlite3.connect('data.db') as conn:
        curs = conn.cursor()
        curs.execute(vsql)
        ret = curs.fetchall()
    # 终端上打印相关信息
    print("\n人员信息列表如下:")
    print("序号   姓名    性别    年龄    部门    电话号码    备注")
    print('-' * 90)
    for item in ret:
        print(str(item[0]).ljust(10), end='')
        print(item[1].ljust(9), end='')
        print(item[2].ljust(8), end='')
        print(str(item[3]).ljust(10), end='')
        print(item[4].ljust(20), end='')
        print(item[5].ljust(20), end='')
        print(item[6].ljust(20))
    print('\n')
        

# 主函数
if __name__ == '__main__':
    # 给变量 v_menu 赋值提示信息
    v_menu = '''
========================================================================================================================================
        1. 连接数据库
        2. 构建一个用户信息表(person)
        3. 向用户信息表增加记录
        4. 删除一条记录
        5. 显示用户信息
        q. 推出程序
        '''

    while True:
        # 列出菜单供用户选择
        print(v_menu)
        # 接收用户的选择
        v_choose = input("请选择相应的操作(1~5): ")
        if v_choose == '1':
            # 连接数据库测试
            connect_db()
        elif v_choose == '2':
            # 新建一张数据表
            create_table()
        elif v_choose == '3':
            # 向数据表中增加一条记录
            add_row()
        elif v_choose == '4':
            # 删除一条数据
            del_row()
        elif v_choose == '5':
            # 列出数据表中所有数据
            list()
        elif v_choose == 'q':
            break
        else:
            break
