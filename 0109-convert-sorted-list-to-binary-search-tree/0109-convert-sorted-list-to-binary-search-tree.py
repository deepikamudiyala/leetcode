# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode | None) -> TreeNode | None:
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        def bst(low,high):
            if low>high:
                return None
            mid=(low+high)//2
            node=TreeNode(arr[mid])
            node.left=bst(low,mid-1)
            node.right=bst(mid+1,high)
            return node
        return bst(0,len(arr)-1)