
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        dic={None:None}
        cur=head
        while cur:
            dic[cur]=Node(cur.val)
            cur=cur.next
        cur=head
        while cur:
            copy=dic[cur]
            copy.next=dic[cur.next]
            copy.random=dic[cur.random]
            cur=cur.next
        return dic[head]

