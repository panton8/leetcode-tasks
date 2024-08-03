from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # T: O(k*n)
    def rotateRight1(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        for i in range(k):
            prev, curr = head, head.next
            while curr.next:
                prev = prev.next
                curr = curr.next

            prev.next = None
            curr.next = head
            head = curr

        return head

    # T: O(len%k*n)
    def rotateRight2(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        list_len = 0

        copy_head = head

        while copy_head:
            list_len += 1
            copy_head = copy_head.next

        for i in range(k % list_len):
            prev, curr = head, head.next
            while curr.next:
                prev = prev.next
                curr = curr.next

            prev.next = None
            curr.next = head
            head = curr

        return head


def main():
    sol = Solution()

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    k = 2
    head = sol.rotateRight1(head, k)

    while head:
        print(head.val)
        head = head.next

    print('######################')

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    head = sol.rotateRight2(head, k)

    while head:
        print(head.val)
        head = head.next


if __name__ == '__main__':
    main()
