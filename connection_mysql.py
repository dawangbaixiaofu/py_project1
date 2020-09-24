import sqlite3
import pandas as pd
import pymysql
import Single
try:
    conn1 = Single.Connection(host='localhost', user='root', port=3306, password='729813', database='test')
    conn = Single.Connection(host='localhost', user='root', port=3306, password='729813', database='test')
except:
    print("connection error!")
# 指定不同类型的cursor来获取不同类型的查询数据；对于大型查询来说使用fetchall_unbuffered()更加有效;返回一个迭代器对象
# DictCursor这种类型的cursor返回数据对象是一个字典
# cur = conn.cursor()
sql_statements = 'select * from test_view;'
# cur.execute(sql_statements)
# columnDes = cur.description
# columnNames = [columnDes[i][0] for i in range(len(columnDes))]
# raw_data = cur.fetchall()
# df = pd.DataFrame([list(i) for i in raw_data], columns=columnNames)

df = pd.read_sql(sql_statements,conn)
print(df)
# 验证单例模式的连接是否成功
print(conn, conn1)

conn.commit()
conn.close()

