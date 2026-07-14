class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashmap = {}
        while head:
            if head.next in hashmap.values():
                return True
            hashmap[head]=head.next
            head = head.next
        return False