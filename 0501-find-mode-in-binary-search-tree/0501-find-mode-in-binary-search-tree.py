# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode | None) -> list[int]:
        if not root:return []
        a=[]
        q=deque([root])
        while q:
            node=q.popleft()
            a.append(node.val)
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
        count=Counter(a)
        maxfreq=max(count.values())
        return [val for val,freq in count.items() if freq==maxfreq]