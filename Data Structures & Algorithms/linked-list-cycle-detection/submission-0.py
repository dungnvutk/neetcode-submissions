class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        current = head
        while current:
            if current.val is -999999:
                return True
            else:
                current.val = -999999
            if current.next is None:
                return False
            else:
                current = current.next