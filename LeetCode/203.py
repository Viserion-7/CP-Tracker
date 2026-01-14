# Leetcode 203
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        temp = ListNode(-1, head)
        pre = temp
        while pre.next:
            if pre.next.val != val:
                pre = pre.next
            else:
                pre.next = pre.next.next
        return temp.next
