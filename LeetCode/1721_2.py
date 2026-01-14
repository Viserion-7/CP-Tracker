class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        first= head
        for i in range(k-1):
            first=first.next
        slow=head
        fast=head

        for i in range(k):
            fast=fast.next
        while fast!=None:
            slow=slow.next
            fast=fast.next
        second=slow
        first.val, second.val = second.val, first.val
        
        return head
