class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def findGCD(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def insertGreatestCommonDivisors(self, head):
        if not head:
            return head
        
        current = head
        while current and current.next:
            gcd_value = self.findGCD(current.val, current.next.val)
            new_node = ListNode(gcd_value)
            new_node.next = current.next
            current.next = new_node
            current = current.next.next
        
        return head
