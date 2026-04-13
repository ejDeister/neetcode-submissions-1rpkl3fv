# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = head
        while temp and temp.next:
            temp = temp.next
            if temp.val == head.val:
                return True
            temp = temp.next
            head = head.next
        return False