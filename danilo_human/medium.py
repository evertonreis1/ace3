class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def euclidean_algorithm(a, b):
            while b:
                a, b = b, a % b
            return a

        curr_node = head
        while (next_node := curr_node.next):
            mmc = euclidean_algorithm(curr_node.val, next_node.val)
            curr_node.next = ListNode(mmc, next_node)
            curr_node = next_node
        
        return head