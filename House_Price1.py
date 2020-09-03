import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import norm
from scipy import stats

path = r'C:\Users\ASUS\Downloads'
train_data = pd.read_csv(path + r'\train.csv')
# 对房屋售价进行分析
train_data['SalePrice'].describe()
# histogram of SalePrice
sns.distplot(train_data['SalePrice'])
plt.show()

# 偏度和峰度的衡量，检验是否符合正态分布
train_data['SalePrice'].skew()
train_data['SalePrice'].kurt()

# 重要变量筛选；相关系数矩阵 热力图
corrmat = train_data.corr()
f, ax = plt.subplots(figsize=(12, 9))
sns.heatmap(corrmat, vmax=.8, square=True)
plt.show()

# 选取对SalePrice前10大的重要影响变量
k = 10
cols = corrmat.nlargest(k, columns=['SalePrice']).index

corrmat_top_ten = corrmat.loc[cols, cols]
sns.heatmap(corrmat_top_ten, cbar=True, annot=True, square=True,
            fmt='.2f', annot_kws={'size': 10}, yticklabels=cols.values,
            xticklabels=cols.values)
plt.show()
# conclusion:根据相关系数矩阵剔除共线性变量后，剩余变量如下cols


# 观察各个变量之间的散点图
sns.set()
cols = ['SalePrice', 'OverallQual', 'GrLivArea', 'GarageCars', 'TotalBsmtSF', 'FullBath', 'YearBuilt']
sns.pairplot(train_data[cols], height=2.5)
plt.show()
# conclusion:  'TotalBsmtSF' has a linear relationship with 'GrLivArea'

sns.scatterplot(x=train_data['TotalBsmtSF'], y=train_data['GrLivArea'])
plt.show()
# 根据相关系数矩阵热力图保留'GrLivArea',删除'TotalBsmtSF'
cols = ['SalePrice', 'OverallQual', 'GrLivArea', 'GarageCars', 'FullBath', 'YearBuilt']

# 缺失值情况
total = train_data.isnull().sum().sort_values(ascending=False)
percent = (train_data.isnull().sum() / train_data.isnull().count()).sort_values(ascending=False)
missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])

# 缺失值分析
missing_cols = missing_data[missing_data['Percent'] > .15].index
cols_del = set(missing_cols).intersection(set(cols))
cols = set(cols).difference(cols_del)
# conclusion: 入模变量没有缺失值

# outlier分析,分为单变量分析（分析SalePrice）和双变量分析（分析x and y散点图）
sns.scatterplot(x=train_data['GrLivArea'], y=train_data['SalePrice'])
plt.show()

sns.scatterplot(x=train_data['TotalBsmtSF'], y=train_data['SalePrice'])
plt.show()
# conclusion： 'GrLivArea'取值最大的两个样本为异常点

# 入模变量正态分布 分析
sns.distplot(train_data['SalePrice'], fit=norm)
plt.show()

stats.probplot(train_data['SalePrice'], dist=norm, fit=True, plot=plt)
plt.show()

# 偏度和峰度
train_data['SalePrice'].skew()
train_data['SalePrice'].kurt()
# conclusion：数据右偏，峰度大于0

# 对数转换
train_data['SalePrice'] = np.log(train_data['SalePrice'])
sns.distplot(train_data['SalePrice'], fit=norm)
plt.show()
stats.probplot(train_data['SalePrice'], dist=norm, fit=True, plot=plt)
plt.show()

# 入模变量中的类别性变量和数值型变量
category = ['FullBath', 'GarageCars', 'OverallQual']
values = ['GrLivArea', 'YearBuilt', 'SalePrice']

# 总体查看入模变量是否符合正态分布情况
for i in values:
    sns.distplot(train_data[i], fit=norm)
    plt.show()
    stats.probplot(train_data[i], plot=plt)
    plt.show()

# 对'GrLivArea'进行对数转换
train_data['GrLivArea'] = np.log(train_data['GrLivArea'])
sns.distplot(train_data['GrLivArea'], fit=norm)
plt.show()
stats.probplot(train_data['GrLivArea'], plot=plt)
plt.show()
