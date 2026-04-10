# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def dfs(node):
            if node:
                if node.left and node.right:
                    left, right = dfs(node.left), dfs(node.right)
                    if left == -1 or right == -1 or abs(left-right) > 1:
                        return -1
                    return max(left,right) + 1
                elif not node.left and not node.right:
                    return 1
                elif node.left:
                    left = dfs(node.left)
                    if left == -1 or left > 1:
                        return -1
                    else:
                        return left + 1
                else:
                    right = dfs(node.right)
                    if right == -1 or right > 1:
                        return -1
                    else:
                        return right + 1
        return dfs(root) != -1