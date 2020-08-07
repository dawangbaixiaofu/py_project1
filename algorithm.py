# 顺序查找
def sequential_search(alist,item):
    find = False
    pos = 0
    while pos < len(alist) and not find:
        if alist[pos] == item:
            find = True
        else:
            pos += 1
    return find

# 二分查找适合用于有序列表进行查找复杂度为log2(n)


def binary_search1(alist,item):
    first = 0
    last = len(alist)-1
    find = False
    while first<last and not find:
        midpoint = (first+last)//2
        if alist[midpoint] == item:
            find = True
        else:
            if alist[midpoint]<item:
                first = midpoint+1
            else:
                last = midpoint-1
    return find

# 递归算法实现
def binary_search(alist, item):
    if len(alist) == 0:
        return False
    midpoint = len(alist)//2
    if alist[midpoint] == item:
        return True
    else:
        if alist[midpoint] < item:
            return binary_search(alist[midpoint+1:], item)
        else:
            return binary_search(alist[:midpoint], item)


def bubble_sort(alist):     # 冒泡法进行排序
    for passnum in range(len(alist)-1,0,-1):  #range(7,0,-1) 是左闭右开(7,6,5,...,1)
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


def short_bubble_sort(alist):
    passnum = len(alist)-1
    exchange = True
    while passnum > 0 and exchange:
        exchange = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                exchange = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        passnum -= 1


def selection_sort(alist):
    for slot in range(len(alist)-1,0,-1):
        position_of_max = 0
        for i in range(1,slot+1):
            if alist[position_of_max] < alist[i]:
                position_of_max = i
        temp = alist[position_of_max]
        alist[position_of_max] = alist[slot]
        alist[slot] = temp


def insert_sort(alist):
    for index in range(1, len(alist)):
        position = index
        current_value = alist[index]
        while position > 0 and current_value < alist[position-1]:
            alist[position] = alist[position-1]
            position -= 1
        alist[position] = current_value


def gap_insert_sort(start_point, alist, gap):
    for index in range(start_point+gap, len(alist), gap):
        current_value = alist[index]
        position = index
        while position >= gap and current_value < alist[position-gap]:
            alist[position] = alist[position-gap]
            position -= gap
        alist[position] = current_value


def shell_sort(alist):      #希尔排序
    sub_list_count = len(alist)//2
    while sub_list_count > 0:
        for start_point in range(sub_list_count):
            gap_insert_sort(start_point, alist, sub_list_count)
        sub_list_count = sub_list_count // 2


def merge_sort(alist):      #递归实现合并排序
    # print("spliting", alist)
    if len(alist) > 1:
        mid = len(alist)//2
        left_half = alist[:mid]
        right_half = alist[mid:]
        #为什么以下代码要写在if下面，不能写在if外面；原因：left_half right_half 是局部变量，必须写在if这个局部范围内
        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                alist[k] = left_half[i]
                i += 1
            else:
                alist[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            alist[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            alist[k] = right_half[j]
            j += 1
            k += 1
    # print("merge", alist)


# 递归实现快速排序
def partition(alist, first, last):
    pivot_value = alist[first]
    left_mark = first + 1
    right_mark = last
    done = False

    while not done:
        while left_mark <= right_mark and alist[left_mark] < pivot_value:
            left_mark += 1
        while left_mark <= right_mark and alist[right_mark] > pivot_value:
            right_mark -= 1
        if left_mark > right_mark:
            done = True
        else:
            temp = alist[left_mark]
            alist[left_mark] = alist[right_mark]
            alist[right_mark] = temp

    temp = alist[right_mark]
    alist[right_mark] = alist[first]
    alist[first] = temp

    return right_mark



def quick_sort_helper(alist, first, last):
    if first < last:
        split_point = partition(alist,first,last)
        quick_sort_helper(alist,first,split_point-1)
        quick_sort_helper(alist,split_point+1,last)


def quick_sort(alist):
    quick_sort_helper(alist,0,len(alist)-1)


if __name__ == '__main__':
    test_list = [2, 3, 4, 9, 8]
    test_list2 = [2, 3, 4, 5, 6, 7, 8, 1]
    test_list3 = [2,3,4,5,1,2,4,6,7,8,89,2]
    test_list4 = [2, 3, 4, 5, 1, 2, 4, 6, 7, 8, 89, 2]
    test_list5 = [21, 33, 46, 55, 1, 89, 2]
    item = 9
    print(sequential_search(test_list, item))
    bubble_sort(test_list)
    print(test_list)
    short_bubble_sort(test_list2)
    selection_sort(test_list2)
    insert_sort(test_list3)
    print(test_list2)
    print(test_list3)

    test_shell_sort = [54,26,32,17,77,88]
    shell_sort(test_shell_sort)
    print(test_shell_sort)
    merge_sort(test_list4)
    print(test_list4)

    quick_sort(test_list5)
    print(test_list5)