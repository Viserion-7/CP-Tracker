# Leetcode 2
class Solution:
	def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
		temp = ListNode()
		carry, curr = 0, temp
		while l1 or l2 or carry:
			
			total = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
			carry= total//10
			val = total % 10
			
			curr.next = ListNode(val)
			curr = curr.next
			l1 = l1.next if l1 else None
			l2 = l2.next if l2 else None
		return temp.next
