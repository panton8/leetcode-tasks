from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # T: O(n+m) M: O(n)
    def getIntersectionNode1(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodes = set()

        while headA:
            nodes.add(headA)
            headA = headA.next

        while headB:
            if headB in nodes:
                return headB
            headB = headB.next

        return None

    # T: O(n+m) M: O(1)
    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA, lenB = 0, 0
        copyA, copyB = headA, headB

        while copyA:
            lenA += 1
            copyA = copyA.next

        while copyB:
            lenB += 1
            copyB = copyB.next

        if lenA > lenB:
            for i in range(lenA-lenB):
                headA = headA.next
        elif lenB > lenA:
            for i in range(lenB-lenA):
                headB = headB.next

        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

        return None

