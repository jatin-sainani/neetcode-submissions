# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

#         mergedListNode = dummy = ListNode()
#         while(list1 and list2):
#             if list1.val<list2.val:
#                 dummy.next = list1
#                 list1=list1.next
#             else:
#                 dummy.next = list2
#                 list2=list2.next
#             dummy = dummy.next

#         if list1 == None and list2:
#             dummy.next = list2
#         else:
#             dummy.next = list1


#         return mergedListNode.next




class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:


        dummy = ListNode()
        current = dummy


        while list1 and list2:
            print(list1.val)
            print(list2.val)
            print('__')

            if list1.val<=list2.val:
                current.next = list1
                list1=list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
            print(current.val)
        
        if list1:
            current.next = list1

        if list2:
            current.next = list2
        
        return dummy.next

            
























