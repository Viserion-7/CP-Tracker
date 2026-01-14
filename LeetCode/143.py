
class Solution:
    def reorderList(self, head: ListNode) -> None:

        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        cur = slow.next
        slow.next = None

        pre = None
        while cur:
            nxt = cur.next
            cur.next = pre
            pre, cur = cur, nxt
        cur = head

        while pre:
            nxt = pre.next
            pre.next = cur.next
            cur.next = pre
            cur, pre = pre.next, nxt