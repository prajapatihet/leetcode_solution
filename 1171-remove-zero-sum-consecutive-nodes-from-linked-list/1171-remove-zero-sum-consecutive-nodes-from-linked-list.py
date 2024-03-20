# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        dummy = ListNode(0)
        dummy.next=head
        sum=0
        sums={0:dummy}

        while head:
            sum+=head.val
            if sum in sums:
                prev = sums[sum]
                start = prev.next
                curr_sum = sum
                while start != head:
                    curr_sum += start.val
                    del sums[curr_sum]
                    start = start.next
                prev.next = head.next

            else:
                sums[sum]= head
            head=head.next
        
        return dummy.next
        