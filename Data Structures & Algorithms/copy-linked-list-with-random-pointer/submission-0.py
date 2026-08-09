"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        

        hash_copy = {None: None}

        current = head

        while current:
            copy = Node(current.val)
            hash_copy[current] =  copy
            current = current.next
        current = head
        while current:
            copy = hash_copy[current]
            copy.next = hash_copy[current.next]
            copy.random = hash_copy[current.random]
            current = current.next
        return hash_copy[head]
