# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        def get_length(head):
            # Функция для получения длины связанного списка
            length = 0
            current = head
            while current:
                length += 1
                current = current.next
            return length

        # Получаем длину списка
        length = get_length(head)

        # Если список пуст или недостаточно нод для удаления, возвращаем исходную голову
        if not head or n > length:
            return head

        # Вычисляем номер ноды для удаления от начала списка
        node_from_start_to_delete = length - n + 1

        # Если нужно удалить голову списка, просто перенаправляем голову на следующий элемент
        if node_from_start_to_delete == 1:
            head = head.next
            return head

        # Ищем предыдущий элемент перед удаляемой нодой
        prev_node = head
        for _ in range(node_from_start_to_delete - 2):
            if not prev_node.next:  # Если достигли конца списка раньше, чем нашли ноду, выходим
                return head
            prev_node = prev_node.next

        # Если нашли предыдущую ноду, то перенаправляем её ссылку на следующий элемент после удаляемой
        if prev_node.next:
            prev_node.next = prev_node.next.next

        return head


