# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        return not root or self.sym(root.left,root.right)
    def sym(self,l,r):
            if not l or not r :return l==r
            if l.val!=r.val:
                return False
            return self.sym(l.left,r.right) and self.sym(l.right,r.left)