# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        left=self.depth(root.left)
        right=self.depth(root.right)
        if right==left:
            return pow(2,left)+self.countNodes(root.right)
        else:
            return pow(2,right)+self.countNodes(root.left)
    def depth(self,root):
        if not root:
            return 0
        return 1+self.depth(root.left)