# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(node):
            nonlocal diameter
            
            if node is None:
                return 0

            lefth = dfs(node.left)
            righth = dfs(node.right)

            diameter = max(diameter, lefth + righth)

            return max(lefth, righth) + 1

        dfs(root)
        return diameter