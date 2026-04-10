# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depths = []
        stack = [(root,1)]
        while stack:
            pair = stack.pop()
            node, depth = pair[0], pair[1]
            has_child = False
            if node.left:
                has_child = True
                stack.append((node.left, depth+1))
            if node.right:
                has_child = True
                stack.append((node.right, depth+1))
            if not has_child:
                depths.append(depth)
        return max(depths)
            
            