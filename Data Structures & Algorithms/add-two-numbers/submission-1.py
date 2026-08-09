# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        current_1 = l1
        n = 0
        l1_sum = 0
        while current_1:
            l1_sum += current_1.val*10**n
            current_1 = current_1.next
            n += 1
        current_2 = l2
        n = 0
        l2_sum = 0
        while current_2:
            l2_sum += current_2.val * 10**n
            current_2 = current_2.next
            n += 1
        nodeSum = l1_sum + l2_sum
        dummy = ListNode()
        if nodeSum == 0:
            return dummy
        tail = dummy
        while nodeSum > 0:
            NodeValue = nodeSum % 10
            nodeSum = nodeSum//10
            tail.next = ListNode(NodeValue)
            tail = tail.next
        
        return dummy.next


