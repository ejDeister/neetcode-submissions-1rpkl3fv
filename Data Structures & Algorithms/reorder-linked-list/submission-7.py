# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        halfway = slow.next
        slow.next = None
        snd = None
        while halfway:
            print(halfway.val)
            tmp = snd
            snd = halfway
            halfway = halfway.next
            snd.next = tmp
        
        fst = head
        while snd:
            tmp = fst.next
            tmp2 = snd.next
            fst.next = snd
            snd.next = tmp
            fst = tmp
            snd = tmp2
        
