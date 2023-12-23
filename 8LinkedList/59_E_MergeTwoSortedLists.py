# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        nums = []
        while list2 is not None or list1 is not None:
            if list1 is not None:
                nums.append(list1.val)
                list1 = list1.next
            if list2 is not None:
                nums.append(list2.val)
                list2 = list2.next
        if not nums:
            return None
        nums = sorted(nums, reverse=True)
        ln = ListNode(nums[-1], None)
        curr = ln

        for i in range(len(nums) - 2, -1, -1):
            new_node = ListNode(nums[i], None)
            curr.next = new_node
            curr = curr.next

        return ln


class Solution2:
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2

        if list1 or list2:
            cur.next = list1 if list1 else list2

        return dummy.next


print(Solution().mergeTwoLists(None, ListNode()).val)
