# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode | None) -> list[int]:
        if not root:return[]
        res=[]
        q=deque([root])
        while q:
            size=len(q)
            maxx=float('-inf')
            for _ in range(size):
                node=q.popleft()
                maxx=max(maxx,node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(maxx)
        return res