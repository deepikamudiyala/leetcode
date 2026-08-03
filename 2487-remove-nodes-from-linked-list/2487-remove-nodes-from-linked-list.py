# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rev(node):
            prev=None
            while node:
                next=node.next
                node.next=prev
                prev=node
                node=next
            return prev
        head=rev(head)
        maxi=head.val
        cur=head
        while cur and cur.next:
            if cur.next.val<maxi:
                cur.next=cur.next.next
            else:
                cur=cur.next
                maxi=cur.val
            
        return rev(head)
        