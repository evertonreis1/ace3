class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

class Solution:
    def insertGreatestCommonDivisors(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        curr = head
        while curr and curr.next:
            new_node = ListNode(gcd(curr.val, curr.next.val))
            new_node.next = curr.next
            curr.next = new_node
            prev = new_node
            curr = curr.next.next
        return dummy.next

