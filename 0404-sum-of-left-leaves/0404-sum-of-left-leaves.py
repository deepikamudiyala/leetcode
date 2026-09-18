# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        s=deque([(root,False)])
        res=0
        while s:
            node,isleft=s.pop()
            if not node.left and not node.right and isleft:
                res=res+node.val
            if node.left:
                s.append([node.left,True])
            if node.right:
                s.append([node.right,False])
        return res