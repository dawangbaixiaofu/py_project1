import pymysql
import Single
try:
    conn1 = Single.Connection(host='localhost', user='root', port=3306, password='729813', database='test')
    conn = Single.Connection(host='localhost', user='root', port=3306, password='729813', database='test')
except:
    print("connection error!")
# 指定不同类型的cursor来获取不同类型的查询数据；对于大型查询来说使用fetchall_unbuffered()更加有效;返回一个迭代器对象
# DictCursor这种类型的cursor返回数据对象是一个字典
cur = conn.cursor(cursor=pymysql.cursors.SSCursor)
sql_statements = 'select * from test_view;'
rows = cur.execute(sql_statements)
print(rows)
raw_data = cur.fetchall_unbuffered()
print(raw_data)

for i in raw_data:
    print(i)

# 验证单例模式的连接是否成功
print(conn, conn1)

conn.commit()
cur.close()
conn.close()
