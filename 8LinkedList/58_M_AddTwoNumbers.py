# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = str(l1.val)
        num2 = str(l2.val)
        first = l1.next
        second = l2.next

        while first is not None:
            num1 = str(first.val) + num1  # Reverse the order of digits
            first = first.next

        while second is not None:
            num2 = str(second.val) + num2  # Reverse the order of digits
            second = second.next

        res = str(int(num1) + int(num2))
        ln = ListNode(int(res[-1]), None)
        curr = ln

        for i in range(len(res)-2, -1, -1):
            new_node = ListNode(int(res[i]), None)
            curr.next = new_node
            curr = curr.next

        return ln


print(Solution().addTwoNumbers(l1=[2, 4, 3], l2=[5, 6, 4]))
print(Solution().addTwoNumbers(l1=[0], l2=[0]))
print(Solution().addTwoNumbers(l1=[9, 9, 9, 9, 9, 9, 9], l2=[9, 9, 9, 9]))
