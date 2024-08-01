# Definition for singly-linked list.
from copy import copy
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome1(self, head: Optional[ListNode]) -> bool:
        vals = []

        while head:
            vals.append(head.val)
            head = head.next

        return vals == vals[::-1]

    def isPalindrome2(self, head: Optional[ListNode]) -> bool:
        end, middle = head, head

        while end and end.next:
            end = end.next.next
            middle = middle.next

        prev, curr = None, middle

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        left, right = head, prev

        while right:
            if right.val != left.val:
                return False
            left = left.next
            right = right.next

        return True


def main():
    head1 = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    head2 = ListNode(1)
    head3 = ListNode(1, ListNode(2, ListNode(2, ListNode(3, ListNode(5)))))
    sol = Solution()

    assert sol.isPalindrome1(head1) is True
    assert sol.isPalindrome1(head2) is True
    assert sol.isPalindrome1(head3) is False
    assert sol.isPalindrome2(head1) is True
    assert sol.isPalindrome2(head2) is True
    assert sol.isPalindrome1(head3) is False


if __name__ == '__main__':
    main()
