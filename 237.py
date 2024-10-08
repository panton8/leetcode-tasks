# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node.next and node.next.next:
            node.val = node.next.val
            node = node.next

        node.val = node.next.val
        node.next = None


def main():
    sol = Solution()
    head = ListNode(4)
    head.next = ListNode(5)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(9)

    sol.deleteNode(head.next)

    while head:
        print(head.val)
        head = head.next


if __name__ == '__main__':
    main()