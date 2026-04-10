# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = []
        def dfs(node, level):
            nonlocal q
            if node:
                if len(q) < level:
                    q.append([])
                q[level-1].append(node.val)
                dfs(node.left,level+1)
                dfs(node.right,level+1)
        dfs(root,1)
        return q
        