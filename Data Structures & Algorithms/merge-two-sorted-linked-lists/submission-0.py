class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        listMerge = dummy
        while list1 and list2:
            if list1.val<=list2.val:
                listMerge.next = list1
                list1 = list1.next
            else:
                listMerge.next = list2
                list2 = list2.next
            listMerge = listMerge.next
        if list1:
            listMerge.next = list1
        elif list2:
            listMerge.next = list2
        return dummy.next