# Leetcode 141
class Solution:
	def hasCycle(self, head: ListNode) -> bool:
		slow = head
		fast = head

		if head is None:
			return False

		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next

			if slow == fast:
				return True

		return False
