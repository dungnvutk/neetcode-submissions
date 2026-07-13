# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
           # find the middle
        s,f = head, head
        while f and f.next:    
            prev = s                 
            s = s.next
            f = f.next.next    
        prev = s                 
        s = s.next  
        prev.next = None

        # reverse
        reverse = None
        curr = s
        while curr:
            nxt = curr.next
            curr.next = reverse
            reverse = curr
            curr = nxt
        second = reverse

        # merge
        first = head
        while second:
            l1 = first.next
            l2 = second.next

            first.next = second
            second.next = l1

            first = l1
            second = l2