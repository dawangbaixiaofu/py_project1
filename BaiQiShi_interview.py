import pandas as pd
import numpy as np
import datetime

path = r"D:\Github\ThinkingWriting\shapener.xlsx"
df = pd.read_excel(path, sheet_name='df', header=0)
frame = pd.read_excel(path, sheet_name='frame', header=0)
df1 = df.loc[:, ['apply_date']].groupby(df['cert_no']).max()
print(df, "\n", df1)
res = pd.merge(left=df, right=df1, on=['cert_no', 'apply_date'], how='right')
print(res)


education_level = set(df['education'])
for level in education_level:
    res[level] = res.education.map(lambda x: 1 if x == level else 0)
res.drop(columns='education', inplace=True)
print(res)


def date_calculate(apply_date):
    now = datetime.datetime.strptime('2019-10-01', '%Y-%m-%d')
    if now - apply_date >= datetime.timedelta(days=150):
        return 1
    else:
        return 0


res["MOB_5"] = res['apply_date'].map(date_calculate)
print(res)

cols = [x for x in frame.columns if x.find('multi') != -1 or x.find('union') != -1]
cols.extend(['cert_no', 'apply_date'])
frame = frame.loc[:, cols]
res = pd.merge(left=res, right=frame, on=['cert_no', 'apply_date'], how='inner')
print(res)
