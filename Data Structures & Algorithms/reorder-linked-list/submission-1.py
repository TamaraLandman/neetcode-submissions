# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
       
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        
        second = slow.next

        # Reverse second half of the list
        prev = slow.next = None
        while second: 
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        
        first, second = head, prev
        while second:
            f1, f2 = first.next, second.next
            first.next = second
            second.next = f1
            first, second = f1, f2
        
         




