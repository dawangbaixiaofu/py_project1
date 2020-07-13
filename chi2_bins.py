import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

def Chi2Box(df,variable,flag,bins=10,confidenceVal=3.841,sample=None):
    """
    卡方分箱代码实现
    :param df: dataframe,包含两列，一列是variable，一列是flag
    :param variable: 分箱的变量
    :param flag: 分箱的因变量
    :param bins: 分箱个数上限
    :param confidenceVal: 置信值
    :param sample: 抽样百分比；样本过多是否进行抽样，提高分箱效率
    :return:
    """
    if sample is not None:
        df = df.sample(sample)
    else:
        pass

    # 对数据进行格式化处理
    total_num = df[flag].groupby(df[variable]).count()
    total_num = pd.DataFrame({'total_num': total_num})  #之所以转化为数据框是为了获取索引，增加为新的一列
    negative_num = df[flag].groupby(df[variable]).sum()
    negative_num = pd.DataFrame({'negative_num':negative_num})
    regroup = pd.merge(total_num,negative_num,left_index=True,right_index=True,how='inner')
    regroup['positive_num'] = regroup['total_num']-regroup['negative_num']
    regroup.reset_index(inplace=True)

    #转化为np.array数据形式，好进行数据的处理
    np_regroup = np.array(regroup)
    print('数据已经格式化处理，开始进行数据的预处理！')

    # 处理连续没有正样本或负样本的区间，并进行区间的合并（以免卡方值计算报错）
    i = 0
    while(i<=np_regroup.shape[0]-2):
        if((np_regroup[i,2]==0 and np_regroup[i+1,2]==0) or (np_regroup[i,3]==0 and np_regroup[i+1,3]==0)):
            np_regroup[i,2]+=np_regroup[i+1,2]
            np_regroup[i,3]+= np_regroup[i+1,3]
            np_regroup[i,0]=np_regroup[i+1,0]
            np_regroup[i,1] += np_regroup[i+1, 1]
            np_regroup = np.delete(np_regroup,i+1,axis=0)
            i = i-1
        i = i+1
    print("数据合并完毕，开始计算卡方值")
    # 对相邻的两个区间计算卡方值
    chi_table = np.array([])    # 创建一个数组保存相邻两个区间的卡方值
    for i in np.arange(np_regroup.shape[0]-1):
        observed = np.array([[np_regroup[i,2], np_regroup[i,3]], [np_regroup[i+1, 2],np_regroup[i+1, 3]]])
        chi = chi2_contingency(observed)[0]
        chi_table = np.append(chi_table, chi)
    print('已完成数据初处理，正在进行卡方分箱核心操作')

    # 把卡方值最小的两个区间进行合并（卡方分箱核心）
    while(1):
        if(len(chi_table) <= bins-1 and min(chi_table)>confidenceVal):
            break
        chi_min_index = np.argwhere(chi_table == min(chi_table))[0] # 找到卡方值最小的索引位置
        np_regroup[chi_min_index, 2] += np_regroup[chi_min_index+1, 2]
        np_regroup[chi_min_index, 3] += np_regroup[chi_min_index+1, 3]
        np_regroup[chi_min_index, 1] += np_regroup[chi_min_index+1, 1]
        np_regroup[chi_min_index, 0] = np_regroup[chi_min_index+1, 0]
        np_regroup = np.delete(np_regroup, chi_min_index+1, axis=0)

        # 计算合并后的卡方值
        if chi_min_index == np_regroup.shape[0]-1:
            observed = np.array([[np_regroup[chi_min_index-1, 2], np_regroup[chi_min_index-1, 3]], [np_regroup[chi_min_index, 2], np_regroup[chi_min_index, 3]]])
            chi_table[chi_min_index-1] = chi2_contingency(observed)[0]
            chi_table = np.delete(chi_table,chi_min_index,axis=0)
        elif chi_min_index == 0:
            observed = np.array([[np_regroup[chi_min_index, 2], np_regroup[chi_min_index, 3]], [np_regroup[chi_min_index+1, 2], np_regroup[chi_min_index+1, 3]]])
            chi_table[chi_min_index] = chi2_contingency(observed)[0]
            chi_table = np.delete(chi_table,chi_min_index+1,axis=0)
        else:
            observed1 = np.array([[np_regroup[chi_min_index-1, 2],np_regroup[chi_min_index-1, 3]],[np_regroup[chi_min_index, 2],np_regroup[chi_min_index, 3]]])
            observed2 = np.array([[np_regroup[chi_min_index, 2], np_regroup[chi_min_index, 3]], [np_regroup[chi_min_index+1, 2], np_regroup[chi_min_index+1, 3]]])
            chi_table[chi_min_index-1] = chi2_contingency(observed1)[0]
            chi_table[chi_min_index] = chi2_contingency(observed2)[0]
            chi_table = np.delete(chi_table, chi_min_index+1, axis=0)

    print("已完成卡方分箱核心操作，正在保存结果")
    # 保存生成的结果
    result_data = pd.DataFrame()
    list_temp = []
    result_data['variable'] = [variable]*np_regroup.shape[0]
    for i in np.arange(np_regroup.shape[0]):
        if i == 0:
            x = '0'+','+str(np_regroup[i,0])
        else:
            x = str(np_regroup[i-1, 0])+','+str(np_regroup[i, 0])
        list_temp.append(x)

    result_data['interval'] = list_temp
    result_data['flag_1'] = np_regroup[:, 2]
    result_data['flag_0'] = np_regroup[:, 3]
    return result_data,chi_table

if __name__ == '__main__':

    data = pd.read_csv('./dataProcessed.csv')
    # data = pd.DataFrame({'age':[18,19,21,20,25,33,30,70],'label':[1,0,1,1,0,1,0,1]})
    result_box,chi2 = Chi2Box(df=data,variable='age',flag='label',bins=4)
    print(result_box,chi2)