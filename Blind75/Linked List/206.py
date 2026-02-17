# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev # 2-3-4 -> 2-1-none | 3-4 -> 3-2-1-none
            prev = curr # 2-1-none | 3-2-1-none
            curr = temp
        return prev

