# 在O(n log n)的时间内使用常数级空间复杂度对链表进行排序	from Leecode


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:  # 合并排序
    def merge_sort_list(self, alist: list):
        if len(alist) > 1:
            mid = len(alist) // 2
            left = alist[:mid]
            right = alist[mid:]
            self.merge_sort_list(left)
            self.merge_sort_list(right)

            i, j, k = 0, 0, 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    alist[k] = left[i]
                    i += 1
                else:
                    alist[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                alist[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                alist[k] = right[j]
                j += 1
                k += 1

    def merge_sort(self, head: ListNode):
        if not head or not head.next:
            return head

        # 快慢指针寻找链表中间点；是整个代码的关键
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        fast = slow
        slow = slow.next
        fast.next = None

        left = self.merge_sort(head)
        right = self.merge_sort(slow)

        new_head = ListNode(0)
        cur = new_head
        while left and right:
            if left.val < right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
        if left:
            cur.next = left
        if right:
            cur.next = right
        return new_head.next

    #   给出一组区间，请合并所有重叠的区间
    @staticmethod
    def merge(intervals: list):
        if not intervals:
            return intervals
        pre, cur, n = 0, 1, len(intervals)
        while cur < n:
            if intervals[pre].end < intervals[cur].start:
                pre += 1
                intervals[pre] = intervals[cur]
            else:
                intervals[pre].end = max(intervals[pre].end, intervals[cur].end)
            cur += 1
        return intervals[:pre + 1]

    @staticmethod
    def search_range(A: list, target):
        first = 0
        last = len(A) - 1

        if len(A) == 0:
            return [-1, -1]
        #         向左夹逼
        while first <= last:
            mid = (first + last) // 2
            if A[mid] < target:
                first = mid + 1
            else:
                last = mid - 1
        #         向右进行夹逼
        first_2 = 0
        last_2 = len(A) - 1
        while first_2 <= last_2:
            mid = (first_2 + last_2) // 2
            if A[mid] <= target:
                first_2 = mid + 1
            else:
                last_2 = mid - 1

        if first <= last_2:
            return [first, last_2]
        return [-1, -1]


if __name__ == '__main__':
    alist = [3, 5, 1, 2, 6, 7, 4, 9, 6]
    Solution().merge_sort_list(alist)
    print(alist)

    node1 = ListNode(8)
    node2 = ListNode(5)
    node3 = ListNode(4)
    node1.next = node2
    node2.next = node3

    node = Solution().merge_sort(node1)
    cur = node
    while cur:
        print(cur.val)
        cur = cur.next

    interval_1 = Interval(1, 4)
    interval_2 = Interval(2, 5)
    interval_3 = Interval(7, 9)
    interval_4 = Interval(10, 15)
    intervals = [interval_1, interval_2, interval_3, interval_4]
    res = Solution().merge(intervals)
    for index in res:
        print(index.start, index.end, '\n')

    list_test = [5, 8, 8, 8, 99, 99]
    target = 8
    res = Solution.search_range(list_test, target)
    print(res)
