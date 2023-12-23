# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        values = {}
        while cur:
            if  cur.val in values:
                values[cur.val] += 1
            else:
                values[cur.val] = 1
            cur = cur.next
        l = []
        for value in values:
            if values[value] == 1:
                l.append(value)
        cur = head
        while cur.next:
            if cur.next.val not in l:
                cur.next = cur.next.next
            else:
                cur = cur.next

        if head.val not in l:
            return head.next
        return head


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(3)
head.next.next.next.next.next = ListNode(4)
head.next.next.next.next.next.next = ListNode(5)
r = Solution().deleteDuplicates(head)
print("23")