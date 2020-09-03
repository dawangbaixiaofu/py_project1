#
# 
# @param num int整型一维数组 
# @return int整型
# 找出一位数组中最长的连续子数组长度


class Solution:
    def longestConsecutive(self, num: list):
        # write code here
        set1 = set(num)
        length = 0
        for i in num:
            if i in set1:
                set1.remove(i)
                total = 1
                left = i - 1
                right = i + 1
                while left in set1:
                    set1.remove(left)
                    total += 1
                    left -= 1
                while right in set1:
                    set1.remove(right)
                    total += 1
                    right += 1
                length = max(length, total)
        return length


if __name__ == '__main__':
    test = [1, 2, 3, 4, 66, 4, 3, 2, 1, 4, 5, 6, 0]
    res = Solution().longestConsecutive(test)
    print(res)
