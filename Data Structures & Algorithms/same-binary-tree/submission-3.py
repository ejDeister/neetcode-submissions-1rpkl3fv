# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            if p.val != q.val:
                return False
            if p.left and q.left:
                return self.isSameTree(p.left, q.left)
            elif (not p.left) ^ (not q.left):
                return False
            if p.right and q.right:
                return self.isSameTree(p.right,q.right)
            elif (not p.right) ^ (not q.right):
                return False
            if not p.left and not p.right and not q.left and not q.right:
                return True
            
        elif not q and not p:
            return True
        else:
            return False