# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        length_list = 0
        current = head
        while current:
            length_list += 1
            current = current.next
        middle_length = math.floor(length_list/2)
        node2 = ListNode()
        current = head
        while current:
            if middle_length == 0:
                node2 = current.next
                current.next = None
                break
            current = current.next
            middle_length -= 1
        prev = None
        while node2:
            temp = node2.next
            node2.next = prev
            prev = node2
            node2 = temp
        current = head
        second = prev

        while second:
            temp_current = current.next
            temp_second = second.next

            current.next = second
            second.next = temp_current

            current = temp_current
            second = temp_second





            