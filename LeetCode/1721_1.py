# Leetcode 1721
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        fast = head
        for _ in range(k - 1):
            fast = fast.next
        p = fast
        slow = head
        while fast.next:
            slow, fast = slow.next, fast.next
        q = slow
        p.val, q.val = q.val, p.val
        return head
