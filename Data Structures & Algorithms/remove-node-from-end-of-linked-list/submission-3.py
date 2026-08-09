# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        current = head
        length = 0
        while current:
            length += 1
            current = current.next
        remove_index = length - n

        if remove_index == 0:
            return head.next

        current = head
        
        while current:
            remove_index -= 1
            if remove_index == 0:
                temp = current.next.next
                current.next = temp
                break
            current = current.next
            
        return head