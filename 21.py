from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        head_of_res = result

        while list1 and list2:
            if list1.val < list2.val:
                result.next = list1
                list1 = list1.next
            else:
                result.next = list2
                list2 = list2.next
            result = result.next

        if list1:
            result.next = list1
        elif list2:
            result.next = list2

        return head_of_res.next

def main():
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]
    #Output: [1, 1, 2, 3, 4, 4]

    list1 = []
    list2 = []
    #Output: []


if __name__ == '__main__':
    main()
