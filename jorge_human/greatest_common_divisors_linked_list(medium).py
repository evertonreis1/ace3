class listNode:

    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

class Solution:
    
    def gcd(self, val1, val2):
        gcd = 1
        for n in range(2, min(val1, val2)+1):
            if val1%n == 0 and val2%n == 0:
                gcd = n
        
        return gcd
    
    def listNodeAppend(self, list:listNode, value):
        current = list
        while current.next != None:
            current = current.next

        current.next = listNode(value)
    
    def insert_gcd_nodes(self, list:listNode):
        current = list
        while current.next:
            val1, val2 = current.val, current.next.val
            dummy = current.next
            current.next = listNode(self.gcd(val1, val2))
            current.next.next = dummy
            current = current.next.next