import pymysql
import pandas as pd
# 打开数据库连接
# path = r'/Users/v_yuanliangliang/Desktop/qq.xlsx'
# # 首先打开文件
# data = pd.read_excel(path)
# print(data)


conn = pymysql.connect(
    host='43.142.123.148',  # MySQL服务器地址
    user='yuan_liangliang',  # MySQL服务器端口号
    password='12345678aA',  # 用户名
    charset='utf8',  # 密码
    port=3306,  # 端口
    db='yuan_liangliang',  # 数据库名称
)

# 使用cursor()方法获取操作游标
c = conn.cursor()
sql = "select * from user"
# 使用execute方法执行SQL语句
c.execute(sql)
# 使用 fetchone() 方法获取一条数据
res = c.fetchone()
print(res)
# 关闭数据库连接
conn.close()
