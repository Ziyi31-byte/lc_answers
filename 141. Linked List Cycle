# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next: return False
        idx=0
        while head:
            head.idx=idx
            idx+=1
            head=head.next
            if hasattr(head, "idx"): return True
        return False
