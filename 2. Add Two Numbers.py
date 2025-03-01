# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        lr = ListNode()
        current = lr
        d = 0
        while l1 is not None and l2 is not None:
            s = l1.val + l2.val + d
            if s > 9:
                current.next=ListNode(s%10)
                current = current.next
                d = 1
            else:
                current.next=ListNode(s)
                current = current.next
                d = 0
            l1 = l1.next
            l2 = l2.next
        while l1 is not None:
            s = l1.val + d
            if s > 9:
                current.next=ListNode(s%10)
                current = current.next
                d = 1
            else:
                d = 0
                current.next=ListNode(s)
                current = current.next
            l1 = l1.next
        while l2 is not None:
            s = l2.val + d
            if s > 9:
                current.next=ListNode(s%10)
                current = current.next
                d = 1
            else:
                d = 0
                current.next=ListNode(s)
                current = current.next
            l2 = l2.next
        if d!=0:
            current.next=ListNode(d)
            current = current.next
        return lr.next