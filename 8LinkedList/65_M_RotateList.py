# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        l = 0
        cur = head
        while cur:
            l += 1
            cur = cur.next
        if k % l == 0:
            return head
        k = k % l
        tempNode = head
        for _ in range(l - k - 1):
            tempNode = tempNode.next
        answer = tempNode.next
        tempNode.next = None

        return answer

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
r = Solution().rotateRight(head, 2)
