# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode | None) -> int:
        q=deque([root])
        maxsum=float('-inf')
        maxlevel=1
        curr=1
        while q:
            levelsum=0
            levelsize=len(q)
            for _ in range(levelsize):
                node=q.popleft()
                levelsum+=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if levelsum>maxsum:
                maxsum=levelsum
                maxlevel=curr
            curr+=1
        return maxlevel