import os
import time
import subprocess
import pymysql
from pathlib import Path


# 生成一个备份文件名，名字由日期时间组成
# 便于通过文件名知道备份时间
def create_filename(db_name):
    file_name = db_name + '_backup-' + time.strftime('%Y%m%d-%H%M%S') + '.sql'
    return file_name

# 对数据库进行备份的函数
def db_backup(host, db_name, user, password):
    print('调用函数生成一个备份文件的名字')
    filename = create_filename(db_name)
    # 执行备份文件的路径和名字
    path_name = str(Path(__file__).parent / filename)
    # 生成备份命令
    backupcmd = 'mysqldump -h ' + host + ' -u ' + user + ' -p' + password + ' ' + db_name + ' > ' + path_name
    print('备份路径: ', path_name)
    print('备份命令: ', backupcmd)
    # os.system方法已过时
    # os.system(backupcmd)
    subprocess.run(backupcmd, shell=True)
    print('备份完成！')


# 创建数据库的函数
def create_db(host, db_name, user, password):
    # 建立数据库连接
    conn = pymysql.connect(host=host, port=3306, user=user, password=password)
    # 建立一个游标
    cur = conn.cursor()
    # 创建一个空数据库
    cur.execute('create database ' + db_name)
    # 关闭游标和连接
    cur.close()
    conn.close()
    print('数据库创建成功！')


# 创建数据库的函数
def delete_db(host, db_name, user, password):
    # 建立数据库连接
    conn = pymysql.connect(host=host, port=3306, user=user, password=password)
    # 建立一个游标
    cur = conn.cursor()
    # 创建一个空数据库
    cur.execute(f"DROP DATABASE `{db_name}`")
    # 关闭游标和连接
    cur.close()
    conn.close()
    print('数据库删除成功！')


# 恢复数据库的函数
def db_recover(host, db_name, user, password, filename):
    path_name = str(Path(__file__).parent / filename)
    recovercmd = 'mysql -h ' + host + ' -u ' + user + ' -p' + password + ' ' + db_name + ' < ' + path_name
    print('恢复路径: ', path_name)
    print('恢复命令: ', recovercmd)
    subprocess.run(recovercmd, shell=True)
    print('数据恢复完成！')


# 主函数main进行测试
if __name__ == '__main__':
    # 初始化变量值
    host = 'localhost'
    db_name = 'example6_5'
    user = 'root'
    password = os.environ.get('DBPASSWORD')
    # 调用备份函数进行备份
    # db_backup(host, db_name, user, password)
    # 为测试，调用函数删除数据库
    # delete_db(host, db_name, user, password)
    # 由于恢复数据库数据时，MySQL要求该数据库必须先存在才能恢复
    # 因此调用函数生成一空数据库供恢复测试用
    # create_db(host, db_name, user, password)
    # 选一个备份文件，从中恢复数据
    filename = 'example6_5_backup-20261017-220323.sql'
    # 调用函数进行数据恢复
    db_recover(host, db_name, user, password, filename)
    
