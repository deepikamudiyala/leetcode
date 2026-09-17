# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode | None) -> int:
        q=deque([root])
        fmin=root.val
        smin=float('inf')
        if not root.left:
            return -1
        while q:
            node=q.popleft()
            if node.left:
                q.append(node.left)
                q.append(node.right)
                if node.left.val>fmin:
                    smin=min(smin,node.left.val)
                if node.right.val>fmin:
                    smin=min(smin,node.right.val)
        return -1 if smin==float('inf') else smin