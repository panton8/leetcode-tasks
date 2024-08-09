# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        res = list1
        tail = None

        while list1:
            a -= 1

            if a == 0:
                node = list1

                while b != 0:
                    list1 = list1.next
                    b -= 1

                tail = list1.next
                node.next = list2

            list1 = list1.next
            b -= 1

        cur = res
        while cur.next:
            cur = cur.next

        cur.next = tail

        return res


def main():
    sol = Solution()

    # Input: list1 = [10, 1, 13, 6, 9, 5], a = 3, b = 4, list2 = [1000000, 1000001, 1000002]
    # Output: [10, 1, 13, 1000000, 1000001, 1000002, 5]
    list1 = ListNode(10,  ListNode(1, ListNode(13, ListNode(6, ListNode(9, ListNode(5 ))))))
    list2 = ListNode(100000, ListNode(1000001, ListNode(1000002)))
    a = 3
    b = 4

    head = sol.mergeInBetween(list1, a, b, list2)

    while head:
        print(head.val)
        head = head.next


if __name__ == '__main__':
    main()
