# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    root=None
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        prev=None
        lenght=0
        while curr:
            lenght+=1
            curr=curr.next
        if n==lenght:
            return head.next
        
        pos=lenght-n
        curr=head

        for _ in range(pos):
            prev=curr
            curr=curr.next

        prev.next=curr.next

        return head

        