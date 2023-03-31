# # # 先要安装几个库 sqlalchemy, pandas,mysql-connector-python
#
from sqlalchemy import create_engine
import pandas as pd
from sqlalchemy import text
# # 定义路径
path = r"/Users/v_yuanliangliang/Desktop/qq.xlsx"
# # 首先打开文件
data = pd.read_excel(path)
engine = create_engine('mysql+mysqlconnector://yuan_liangliang:12345678aA@43.142.123.148:3306/yuan_liangliang')
data.to_sql(name='user1',con=engine, if_exists="append", index=False, chunksize=1000)
with engine.connect() as con:
    sql = "SELECT * FROM user1;"  # 这里是sql语句
    tables = con.execute(text(sql))  # 执行后使用.fetchall()得到全部的语句
    print(tables.fetchone())
# from sqlalchemy import create_engine
# from sqlalchemy import text
#
# if __name__ == '__main__':
#     # engine = create_engine("mysql+pymysql://用户名:密码@127.0.0.1:3306/数据库名")
#     engine = create_engine(
#         'mysql+pymysql://yuan_liangliang:12345678aA@43.142.123.148:3306/yuan_liangliang')
#
#     with engine.connect() as con:
#         sql = "SELECT * FROM user1;" # 这里是sql语句
#         tables = con.execute(text(sql)) # 执行后使用.fetchall()得到全部的语句
#         print(tables.fetchone())
#
