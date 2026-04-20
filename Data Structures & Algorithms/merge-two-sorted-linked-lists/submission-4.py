# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list_of_data = []
        curr1 = list1
        curr2 = list2
        while list1 or list2:
            if list1:
                list_of_data.append(list1.val)
                list1 = list1.next
            elif list2:
                list_of_data.append(list2.val)
                list2 = list2.next
        list_of_data.sort()
        last = curr1
        while curr1 and last.next:
            last = last.next
        if curr1:
            last.next = curr2
        else:
            curr1 = curr2
        l = ListNode()
        l.head = curr1
        curr = l.head
        for data in list_of_data:
            if curr:
                curr.val = data
                curr = curr.next
        return l.head