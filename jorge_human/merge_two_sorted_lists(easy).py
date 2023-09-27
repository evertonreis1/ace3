class Solution:    
    def mergeTwoLists(self, list1:listNode, list2:listNode):   
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val <= list2.val:
            merged = list1
            query = list2
        else:
            merged = list2
            query = list1

        current_m = merged
        while current_m.next and query:
            if query.val < current_m.next.val:
                dummy = current_m.next
                current_m.next = query
                query = query.next
                current_m.next.next = dummy
            current_m = current_m.next
        
        if query:
            current_m.next = query

        return merged