from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        unique_nodes = set()

        while head:
            if head.next in unique_nodes:
                return True
            unique_nodes.add(head.next)
            head = head.next

        return False
