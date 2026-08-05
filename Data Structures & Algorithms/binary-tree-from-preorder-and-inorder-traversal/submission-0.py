# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderIndex = {}

        for i, num in enumerate(inorder):
            inorderIndex[num] = i

        def build(preLeft, preRight, inLeft, inRight):
            if preLeft > preRight:
                return None

            rootValue = preorder[preLeft]
            root = TreeNode(rootValue)

            mid = inorderIndex[rootValue]

            leftSize = mid - inLeft

            root.left = build(
                preLeft + 1,
                preLeft + leftSize,
                inLeft,
                mid - 1
            )

            root.right = build(
                preLeft + leftSize + 1,
                preRight,
                mid + 1,
                inRight
            )

            return root
        
        return build(
            0,
            len(preorder) - 1,
            0,
            len(inorder) - 1
        )