def mergeTwoList(self, l1: ListNode, l2: ListNode) -> ListNode:
    prev = ListNode(0)
    cur = prev

    while l1 and l2:
        if l1.val < l2.val:
            prev.next = l1
            prev, l1 = prev.next, l1.next
        else:
            prev.next = l2
            prev, l2 = prev.next, l2.next

    if l1 or l2:
        prev.next = l1 or l2

    return cur.next