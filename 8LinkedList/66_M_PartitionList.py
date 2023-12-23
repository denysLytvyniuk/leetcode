# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # Create two dummy nodes for partitioned list
        before_head = ListNode(0)
        before = before_head
        after_head = ListNode(0)
        after = after_head

        # Traverse the original list and add each node to either
        # the before partition or after partition
        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next

        # End the after partition list
        after.next = None
        # Combine the before and after partitions
        before.next = after_head.next
        return before_head.next
