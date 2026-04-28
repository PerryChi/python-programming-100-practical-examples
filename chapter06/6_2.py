import sqlite3

conn = sqlite3.connect('data.db')

# 定义一条SQL插入语句
vsql = 'insert into person(name, sex, age, department, telephone, bz)' \
    'VALUES("李明", "男", "18", "保安部", "13562813857", "新员工")'

# 执行SQL语句
conn.execute(vsql)
# 定义一个列表，列表每个元素是元组，为SQL语句提供参数
person = [
    ("张三", "男", "19", "保安部", "13562813526", "新员工"),
    ("李四", "女", "19", "保安部", "13562819456", "新员工"),
]

# 定义一条SQL语句，留出参数位
vsql2 = 'insert into person(name, sex, age, department, telephone, bz)' \
    'VALUES(?, ?, ?, ?, ?, ?)'

# 执行多条SQL语句，两次增加人员信息
conn.executemany(vsql2, person)

# 定义一条SQL编写的脚本
vsql3 = '''
    delete from persion where name="张三";
    update person set age=22 where name="李四"；
    insert into person(name, sex, age, department, telephone, bz)
    VALUES("王五", "男", "28", "保安部", "13562819123", "新员工"),
'''

# 执行SQL脚本
conn.executescript(vsql3)

# 提交事务
conn.commit()
# 关闭连接
conn.close()