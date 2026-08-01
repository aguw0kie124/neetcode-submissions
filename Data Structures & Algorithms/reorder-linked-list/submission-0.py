# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        # find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse secnod half
        second = slow.next
        slow.next = None
        prev = None

        while second:
            t = second.next # temporary store of rest of list
            second.next = prev # reverse to point to previous vlaue
            prev = second # previous move up 1
            second = t # second move up one to previosu temp
        
        first = head
        second = prev

        while second:
            t1, t2 = first.next, second.next

            first.next = second
            second.next = t1

            first, second = t1, t2



        
