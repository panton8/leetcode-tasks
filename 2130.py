from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # reverse 2nd part of linked list
    def pairSum1(self, head: Optional[ListNode]) -> int:
        if not head.next.next:
            return head.val + head.next.val

        slow, fast = head.next, head.next

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        prev = None

        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        max_sum = 0

        while prev:
            max_sum = max(max_sum, prev.val + head.val)
            prev = prev.next
            head = head.next

        return max_sum

    # reverse 1st part of linked list
    def pairSum2(self, head: Optional[ListNode]) -> int:
        if not head.next.next:
            return head.val + head.next.val

        slow, fast, prev = head, head, None

        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        max_sum = 0

        while prev:
            max_sum = max(max_sum, prev.val + slow.val)
            prev = prev.next
            slow = slow.next

        return max_sum


def main():
    sol = Solution()

    head1 = ListNode(4, ListNode(2, ListNode(2, ListNode(3))))
    head2 = ListNode(5, ListNode(4, ListNode(2, ListNode(1))))
    head3 = ListNode(1, ListNode(100000))
    head4 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9, ListNode(10))))))))))

    assert sol.pairSum1(head1) == 7
    assert sol.pairSum1(head2) == 6
    assert sol.pairSum1(head3) == 100001
    assert sol.pairSum1(head4) == 11

    head1 = ListNode(4, ListNode(2, ListNode(2, ListNode(3))))
    head2 = ListNode(5, ListNode(4, ListNode(2, ListNode(1))))
    head3 = ListNode(1, ListNode(100000))
    head4 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9, ListNode(10))))))))))

    assert sol.pairSum2(head1) == 7
    assert sol.pairSum2(head2) == 6
    assert sol.pairSum2(head3) == 100001
    assert sol.pairSum2(head4) == 11


if __name__ == '__main__':
    main()
