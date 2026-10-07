# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def traverse(original, cloned):
            if original:
                traverse(original.left, cloned.left)
                if original == target:
                    self.ans = cloned
                traverse(original.right, cloned.right)
                

        traverse(original, cloned)
        return self.ans