# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        cur = head
        values = []
        while cur:
            values.append(cur.val)
            cur = cur.next

        new_values = []
        for j in range((len(values) // k) + 1):
            if j == (len(values) // k):
                new_values += values[j * k:]
            else:
                new_values += values[j * k:(j + 1) * k][::-1]
        ln = ListNode(int(new_values[0]), None)
        curr = ln

        for i in range(1, len(new_values)):
            new_node = ListNode(new_values[i], None)
            curr.next = new_node
            curr = curr.next

        return ln
