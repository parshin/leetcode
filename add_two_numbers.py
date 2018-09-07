# Definition for singly-linked list.
class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

    def get_val(self):
        return self.val

    def set_val(self, val):
        self.val = val

    def get_next(self):
        return self.next

    def set_next(self, data):
        self.next = data


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def add_node(self, val):
        new_node = Node(val, self.head)
        self.head = new_node

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.val)
            cur = cur.get_next()


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        tmp = LinkedList(0)
        cur = tmp
        car = 0

        while l1 or l2:
            val = car
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            car, val = divmod(val, 10)
            cur.next = Node(val)
            cur = cur.next

        if car == 1:
            cur.next = Node(1)

        return tmp.next


l1 = LinkedList()
l1.add_node(2)
l1.add_node(4)
l1.add_node(3)

l1.print_list()

l2 = LinkedList()
l2.add_node(5)
l2.add_node(6)
l2.add_node(4)

l2.print_list()

solution = Solution()
l3 = solution.addTwoNumbers(l1, l2)
l3.print_list()
