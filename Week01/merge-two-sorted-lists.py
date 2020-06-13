def mergeTwoList(self, l1: ListNode, l2: ListNode) -> ListNode:
    if not l1 or not l2: return l2 or l1

    if l1.val < l2.val:
        l1.next = self.mergeTwoList(l1.next, l2)
        return l1
    else:
        l2.next = self.mergeTwoList(l2.next, l1)
        return l2