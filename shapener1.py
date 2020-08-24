#
#
# @param A int整型一维数组
# @param B int整型一维数组
# @return double浮点型
#


class Solution:
    @staticmethod
    def find_kth(A: list, B: list, k: int):
        m = len(A)
        n = len(B)
        if m > n:
            return Solution.find_kth(B, A, k)
        if m == 0:
            return B[k - 1]
        if k == 1:
            test = min(A[0], B[0])
            return test

        p_a = min(k // 2, m)
        p_b = k - p_a
        if A[p_a - 1] < B[p_b - 1]:
            return Solution.find_kth(A[p_a:], B, k - p_a)   # 8-19号 代码错误原因：此处必须有return
        elif A[p_a - 1] > B[p_b - 1]:
            return Solution.find_kth(A, B[p_b:], k - p_b)   # 8-19号 代码错误原因：此处必须有return
        else:
            return A[p_a - 1]

    def findMedianSortedArrays(self, A, B):
        # write code here
        m = len(A)
        n = len(B)
        total = m + n
        if total % 2 == 0:
            test_1 = Solution.find_kth(A, B, total // 2)
            test_2 = Solution.find_kth(A, B, total // 2 + 1)
            return (test_1 + test_2) / 2
        else:
            return Solution.find_kth(A, B, total // 2 + 1)


if __name__ == '__main__':
    A = [1, 4, 6, 7, 8, 9, 10]
    B = [3, 4, 5, 6, 7, 8, 9]
    A1 = [1, 4]
    B1 = [3]
    res = Solution().findMedianSortedArrays(A, B)
    print(res)
