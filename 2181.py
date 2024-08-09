from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # with new List
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        range_sum = 0
        final_list = ListNode()
        res = final_list
        head = head.next

        while head:
            if head.val == 0:
                final_list.next = ListNode(range_sum)
                final_list = final_list.next
                range_sum = 0
            else:
                range_sum += head.val
            head = head.next

        return res.next


def main():
    sol = Solution()

    # [0,3,1,0,4,5,2,0]
    head = ListNode(0,  ListNode(3, ListNode(1, ListNode(0, ListNode(4, ListNode(5, ListNode(2 ,ListNode())))))))

    head = sol.mergeNodes(head)

    while head:
        print(head.val)
        head = head.next


if __name__ == '__main__':
    main()
