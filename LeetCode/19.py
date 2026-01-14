# Leetcode 19
class Solution:
	def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
		dummy = ListNode(next=head)
		fast = slow = dummy
		for _ in range(n):
			fast = fast.next
		while fast.next:
			slow, fast = slow.next, fast.next
		slow.next = slow.next.next
		return dummy.next

