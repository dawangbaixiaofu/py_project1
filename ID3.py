# 决策树代码实现过程
"""
熵的计算，给出数据集进行计算并返回
对数据集进行切分，返回切分后的数据集
选择最优的切分特征
叶子结点标签不唯一处理--票多为胜
创建决策树
预测函数
进行测试
"""
from math import log
import numpy as np


class ID3:
    def __int__(self, dataset):
        self.dataset = dataset[1:]
        self.labels = dataset[0]

    def calc_entropy(self,dataset):
        entropy = 1
        label_counts = {}
        for row in dataset:
            current_label = row[-1]
            if current_label not in label_counts.keys():
                label_counts[current_label] = 0
            else:
                label_counts[current_label] += 1

        total_rows = len(dataset)
        for key in label_counts:
            p = label_counts[key]/total_rows
            entropy -= p*log(p,2)
        return entropy

    def split_category_dataset(self,dataset,axis,value):
        ret_dataset = []
        for row in dataset:
            if row[axis] == value:
                reduce_vec = row[:axis]
                reduce_vec.extend(row[axis+1:])
                ret_dataset.append(reduce_vec)
        return ret_dataset

    def split_continuous_dataset(self, dataset, axis, value, direction: int=0):
        """
        对连续性特征使用二分法进行切分数据集
        :param dataset:
        :param axis:
        :param value:
        :param direction: 0表示按照>value进行切分，1表示按照<=value进行切分
        :return:
        """
        ret_dataset = []
        for row in dataset:
            if direction == 0:
                if row[axis] > value:
                    reduce_vec = row[:axis]
                    reduce_vec.extend(row[axis+1:])
                    ret_dataset.append(reduce_vec)
            else:
                if row[axis] <= value:
                    reduce_vec = row[:axis]
                    reduce_vec.extend(row[axis+1:])
                    ret_dataset.append(reduce_vec)
        return ret_dataset

    def choose_best_feature(self, dataset):
        best_feature = -1
        feature_num = dataset.shape[1]-1
        root_entropy = self.calc_entropy(dataset=dataset)
        best_info_gain = 0
        best_split_dict = {}

        for axis in range(feature_num):
            feature_list = sorted(dataset[:, axis])
            # 判断数组某一列数据类型是否是数值型，数值型number:包括int float bool complex
            if type(feature_list[0]).__name__.startswith('float')  or type(feature_list[0]).__name__.startswith('int'):
                split_list = []
                for i in range(len(feature_list)-1):
                    split_point = (feature_list[i]+feature_list[i+1])/2
                    split_list.append(split_point)

                for point in split_list:
                    sub_entropy = 0
                    split_dataset0 = self.split_continuous_dataset(dataset=dataset,axis=axis,value=point,direction=0)
                    w_right = len(split_dataset0)/dataset.shape[0]
                    sub_entropy += w_right*self.calc_entropy(dataset=split_dataset0)

                    split_dataset1 = self.split_continuous_dataset(dataset=dataset,axis=axis,value=point,direction=1)
                    w_left = len(split_dataset1)/len(dataset)
                    sub_entropy += w_left*self.calc_entropy(dataset=split_dataset1)

                    if root_entropy - sub_entropy > best_info_gain:
                        best_info_gain = root_entropy - sub_entropy
                        best_split_point = point
                        best_feature = axis
                best_split_dict[axis] = best_split_point
            else:
                feature_elements = set(feature_list)
                for value in feature_elements:
                    sub_entropy = 0
                    split_dataset = self.split_category_dataset(dataset=dataset,axis=axis,value=value)
                    w = len(split_dataset)/len(dataset)
                    sub_entropy += w*self.calc_entropy(dataset=split_dataset)
                if root_entropy - sub_entropy > best_info_gain:
                    best_feature = axis
        # 若当前节点的最佳划分特征为连续特征，则将其对应的取值进行二值化处理，即与best_split_point进行对比，小于等于的赋值1，大于的为0
        if type(dataset[0][best_feature]).__name__ == 'float' or type(dataset[0][best_feature]).__name__ == 'int':
            best_split_value = best_split_dict[best_feature]
            for i in range(len(dataset.shape[0])):
                if dataset[i][best_feature] <= best_split_value:
                    dataset[i][best_feature] = 1
                else:
                    dataset[i][best_feature] = 0

        return best_feature

    def majority_count(self, dataset):
        label_count = {}
        for row in dataset:
            label = row[-1]
            if label not in label_count.keys():
                label_count[label] = 0
            label_count[label] += 1
        return max(label_count)

    # todo:成员变量最为成员函数的默认参数，不可以实现
    def fit(self,dataset=self.dataset,labels=self.labels):
        class_label = [example[-1] for example in dataset]
        # np.ndarray has no attribute 'count' but list object has this attribute
        if class_label.count(class_label[0]) == len(class_label):
            return class_label[0]
        if len(dataset[0]) == 1:
            return self.majority_count(dataset=dataset)

        best_feature_index = self.choose_best_feature(dataset=dataset)
        best_feature = labels[best_feature_index]
        my_tree = {best_feature: {}}
        # 字典对象可以接收基本数据类型
        del labels[best_feature_index]

        feature_values = [example[best_feature_index] for example in dataset]
        unique_value = set(feature_values)

        for value in unique_value:
            sub_dataset = self.split_category_dataset(dataset=dataset,axis=best_feature_index,value=value)
            my_tree[best_feature][value] = self.fit(sub_dataset,labels)

        return my_tree