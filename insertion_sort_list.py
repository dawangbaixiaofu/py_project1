class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertion_sort_list(self, head: ListNode):
        if not head or not head.next:
            return head

        sort_linked_node = ListNode(-1)
        cur = head
        while cur:
            p = sort_linked_node
            next_cur = cur.next

            while p.next and p.next.val < cur.val:
                p = p.next

            cur.next = p.next
            p.next = cur
            cur = next_cur
        return sort_linked_node.next


if __name__ == "__main__":
    node1 = ListNode(8)
    node2 = ListNode(5)
    node3 = ListNode(4)
    node1.next = node2
    node2.next = node3
    sort_linked_node = Solution().insertion_sort_list(node1)

    while sort_linked_node:
        print(sort_linked_node.val)
        sort_linked_node = sort_linked_node.next
