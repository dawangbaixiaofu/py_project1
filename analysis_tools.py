import pandas as pd
df = pd.DataFrame({'类别':['水果','水果','水果','蔬菜','蔬菜','肉类','肉类'],
                '产地':['美国','中国','中国','中国','新西兰','新西兰','美国'],
                '水果':['苹果','梨','草莓','番茄','黄瓜','羊肉','牛肉'],
               '数量':[5,5,9,3,2,10,8],
               '价格':[5,5,10,3,3,13,20]})

# pivot_table()
# crosstab()
# 使用交叉表统计不同国家对应的不同种类水果的数量总和
pt = pd.pivot_table(data=df,index='产地',columns='水果',values='数量',fill_value=0,aggfunc=sum,margins=True)
print(pt)
# 使用交叉表统计不同国家对应的不同类别的分组频数，不用考虑数量这一列
ct = pd.crosstab(index=df['产地'],columns=df['类别'])
print(ct)
# 使用交叉表也可以实现透视表的功能
pt = pd.crosstab(index=df['产地'],columns=df['类别'],values=df['数量'],aggfunc=sum,margins=True)
print(pt)