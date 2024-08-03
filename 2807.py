from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head

        first, second = head, head.next

        while second:
            new_val = self.find_gcd(first.val, second.val)
            first.next = ListNode(new_val)
            first.next.next = second

            first = second
            second = second.next

        return head

    def find_gcd(self, num1, num2):
        while num2:
            num1, num2 = num2, num1 % num2
        return num1


def main():
    sol = Solution()

    head = ListNode(18, ListNode(6, ListNode(10, ListNode(3))))

    head = sol.insertGreatestCommonDivisors(head)

    while head:
        print(head.val)
        head = head.next


if __name__ == '__main__':
    main()


