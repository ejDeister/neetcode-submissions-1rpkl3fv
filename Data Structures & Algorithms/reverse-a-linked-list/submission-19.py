# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # res = None
        # while head is not None:
        #     res = ListNode(head.val,res)
        #     head = head.next
        # return res

        res = None
        while head is not None:
            tmp = res
            res = head
            head = head.next
            res.next = tmp
            print(res.val)
            if res.next:
                print(res.next.val)
            print('=')
        return res




