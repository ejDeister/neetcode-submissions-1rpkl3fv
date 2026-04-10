# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        size = 0
        while temp:
            temp = temp.next
            size += 1
        temp = head
        i = 0
        if size-n == 0:
            head = head.next
            return head
        while i < size-n-1:
            temp = temp.next
            i += 1
        if i == size-n:
            temp = None
        else:
            if temp.next and temp.next.next:
                temp.next = temp.next.next
            else:
                temp.next = None
        return head