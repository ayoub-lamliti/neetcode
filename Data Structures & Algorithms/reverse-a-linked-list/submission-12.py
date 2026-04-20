# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        list_data = []
        while curr:
            list_data.append(curr.val)
            curr = curr.next
        curr = head
        for data in list_data[::-1]:
            curr.val = data
            curr = curr.next
        return head