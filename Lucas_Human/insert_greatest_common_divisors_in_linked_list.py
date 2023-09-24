# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        listNode: ListNode = head
        while head.next is not None:
            gcd = math.gcd(head.val, head.next.val)
            temp = head.next
            head.next = ListNode(gcd, temp)
            head = temp
        return listNode
