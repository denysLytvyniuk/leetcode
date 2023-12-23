# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        cur = head
        values = []
        while cur:
            values.append(cur.val)
            cur = cur.next
        new_values = values[:left - 1] + values[left - 1:right][::-1]
        if right < len(values):
            new_values += values[right:]

        ln = ListNode(int(new_values[0]), None)
        curr = ln

        for i in range(1, len(new_values)):
            new_node = ListNode(new_values[i], None)
            curr.next = new_node
            curr = curr.next

        return ln

