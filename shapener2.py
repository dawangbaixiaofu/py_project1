# 给出含有n个整数的数组s，找出s中和加起来的和最接近给定的目标值的三个整数。返回这三个整数的和。你可以假设每个输入都只有唯一解。
# 1.排序2.定基（第一个数为外循环，临近数为第二个数，链表最后一个数是第三个数）
# 3.在固定第一个数的前提下，根据三个数的和是否与target进行比较，如果大于target，
# 那么第三个数后退一步，如果小于target那么第二个前进一步，如果等于target结束。
# 每次内部循环要记录最小gap=abs(sum-target)

# @param num int整型一维数组
# @param target int整型
# @return int整型
#


class Solution:
    def threeSumClosest(self, num: list, target):
        num.sort()
        length = len(num)
        first = 0
        init_sum = num[0] + num[1] + num[length - 1]
        while first <= length - 3:
            second = first + 1
            third = length - 1
            while second < third:
                sum = num[first] + num[second] + num[third]
                gap = sum - target
                if gap > 0:
                    third -= 1
                elif gap < 0:
                    second += 1
                else:
                    return sum

                if abs(gap) < abs(init_sum - target):
                    init_sum = sum
            first += 1
        return init_sum

    def max_area(self, height: list):
        length = len(height)
        first = 0
        last = length - 1
        if length < 2:
            return 0
        area = min(height[first], height[last]) * (last - first)
        while first < last:
            if first < last:
                area = max(height[first] * (last - first), area)
                first += 1
            else:
                area = max(height[last] * (last - first), area)
                last -= 1
        return area

    def binary_search(self, num: list, target):
        if len(num) < 1:
            return False
        mid = len(num) // 2
        if num[mid] == target:
            return True
        if num[mid] < target:
            return self.binary_search(num[mid + 1:], target)
        else:
            return self.binary_search(num[:mid], target)


if __name__ == "__main__":
    test_list = [1, 5, 2, 3, 6, 78]
    target = 19
    res = Solution().threeSumClosest(test_list, target)
    print(res)
    test = [1, 5, 2, 3, 6, 78]
    res = Solution().max_area(test)
    print(res)
    test_bs = [1]
    res = Solution().binary_search(test_bs, 8)
    print(res)
