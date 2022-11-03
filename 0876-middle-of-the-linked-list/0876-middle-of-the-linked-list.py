# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return_val = head 
        list_val = [head.val]
        head = head.next
        while head != None:
            list_val.append(head.val)
            head = head.next
        if len(list_val) % 2 ==0:
            middel = (len(list_val) //2) + 1
        else: 
            middel = (len(list_val) //2) + 1
            
        for i in range(middel-1):
            return_val = return_val.next
        
        return return_val
            
        