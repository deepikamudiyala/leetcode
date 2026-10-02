# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode | None) -> int:
        def depth(node):
            if not node:
                return 0
            return max(depth(node.left),depth(node.right))+1
        def summ(node,d):
            if not node:return 
            if d==depth:
                self.ans+=node.val
            summ(node.left,d+1)
            summ(node.right,d+1)
        self.ans=0
        depth=depth(root)
        summ(root,1)
        return self.ans