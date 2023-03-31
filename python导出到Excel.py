import pymysql
import xlwt

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
sql = "select * from user1"
# 使用execute方法执行SQL语句
c.execute(sql)
# 使用 fetchone() 方法获取一条数据
res = c.fetchall()
print(res)
# 关闭数据库连接
conn.close()

# 2.创建excel表格类型文件
#用Workbook方法来创建一个excel表格类型文件
# 其中的第一个参数是设置数据的编码格式，这里是’utf-8’的形式，
# style_compression设置是否压缩，不是很常用，赋值为0表示不压缩
book = xlwt.Workbook(encoding='utf-8',style_compression=0)

# 3.在excel表格类型文件中建立一张sheet表单
# cell_overwrite_ok用于确认同一个cell单元是否可以重设值，这里赋值为True就表示可重设值。
sheet = book.add_sheet('20212年看的电影',cell_overwrite_ok=True)

# 4.自定义列名
# 用一个元组col自定义列的数量以及各列的属性名
col = ("username","password")

#5.将列属性元组col写进sheet表单中，三列

sheet.write(0,0,col[0])
sheet.write(0,1,col[1])

#6.数据写入表单
datalist = ((res))

for i in range(0, 40):
    data = datalist[i]
    for j in range(0, 2):
        sheet.write(i + 1, j, data[j])

#7.保存，每个人的都不一样，需自己改写
savepath = '/Users/v_yuanliangliang/Desktop/11.xlsx'
book.save(savepath)
