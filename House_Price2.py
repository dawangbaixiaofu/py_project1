import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
import patsy as patsy
import scipy.stats as stats
import seaborn as sns
from sklearn import linear_model
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler

path = r'C:\Users\ASUS\Downloads'
train = pd.read_csv(path + r'\train.csv')
test = pd.read_csv(path + r'\test.csv')
missing = train.isnull().sum()
missing = missing[missing > 0]
missing.sort_values(inplace=True)
plt.figure(figsize=(15, 10))
sns.barplot(x=missing.index, y=missing)
plt.xticks(rotation=90)
plt.show()

# 正态性检验
p = stats.shapiro(train['SalePrice'].fillna(0))[1]
whether_norm = p >= 0.01

# 画出所有变量的直方分布图
quantitative = [x for x in train.columns if train[x].dtypes != 'object']
quantitative.remove('Id')

f = pd.melt(train, value_vars=quantitative)  # 把每列数据 转化为两列，一列是value_vars对应的列名，一列是每一列对应的数值
g = sns.FacetGrid(data=f, col='variable', col_wrap=2, sharex=False, sharey=False)
g.map(sns.distplot, "value")
plt.show()

# 对qualitative变量相对SalePrice画箱线图
qualitative = [x for x in train.columns if train[x].dtypes == 'object']
# 对分类型变量缺失值进行处理
for i in qualitative:
    train[i] = train[i].astype('category')  #在转化为category类型的时候，None值不能进行转化，所以要添加一个新的类别MISSING
    if train[i].isnull().any():
        train[i] = train[i].cat.add_categories(["MISSING"])
        train[i].fillna("MISSING",inplace=True)


def box_plot(x,y,*args,**kwargs):  # 为了在子图中把x轴label旋转90，重写box_plot
    sns.boxplot(x=x, y=y)
    plt.xticks(rotation=90)


f = pd.melt(frame=train, id_vars=['SalePrice'], value_vars=qualitative)
g = sns.FacetGrid(data=f, col='variable', sharex=False, sharey=False)
g.map(box_plot, 'value', 'SalePrice')

plt.show()

# 对类别性变量进行单因素方差分析
def anova(frame):
    anv = pd.DataFrame()
    anv['feature'] = qualitative
    p_values = []
    for col in qualitative:
        sample = []
        for value in frame[col].unique():
            rows = frame[frame[col]==value]['SalePrice'].values
            sample.append(rows)
        p = stats.f_oneway(*sample)[1]
        p_values.append(p)
    anv['p_values'] = p_values
    return anv

a = anova(train)
# 按照p值有小到大进行排序，找出p值最小的前几个变量



# 对类别性变量进行编码,编码顺序按照每个类别对应的SalePrice均值大小进行排序
def encode(frame,feature):
    order = pd.DataFrame()
    order['val'] = frame[feature].unique()
    order.index = order['val']
    order['y_mean'] = frame['SalePrice'].groupby([feature]).mean()
    order.sort_values(by='y_mean', inplace=True)
    order['ordering'] = range(1,order.shape[0]+1)
    ordering = order['ordering'].to_dict()
    for key,value in ordering:
        frame.loc[frame[feature]==key,feature+'E'] = value

for feature in qualitative:
    encode(train, feature)

# correlation matrix



#
TSNE
StandardScaler
PCA
KMeans
sns.lmplot()
patsy.dmatrices()

# 建模,从相关系数矩阵中挑选出相关性较大的变量，并删除共线性变量用来建模，对y值进行对数转换
# 可以考虑多项式回归，需要创建新的特征
linear_model.LassoCV()



