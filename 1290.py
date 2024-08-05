# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        head_copy = head
        list_len = 0

        while head_copy:
            list_len += 1
            head_copy = head_copy.next

        decimal_value = 0
        while head:
            if head.val == 1:
                decimal_value += pow(2, list_len-1)
            list_len -= 1
            head = head.next

        return decimal_value
