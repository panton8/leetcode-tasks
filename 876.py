from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        middle = head
        head_len = 0

        while head:
            head = head.next
            head_len += 1

        middle_len = head_len // 2 + 1

        while middle_len != 1:
            middle = middle.next
            middle_len -= 1

        return middle