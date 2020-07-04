"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null. Return a deep copy of the list.
The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.

Algorithm:
1) Add duplicates to LL ->  a->a'->b->b'->c->c'
2) Iterate thru LL and get the copy random pointers via a->a.rand.next, then set when you go to next curr Pointer
3) Iterate thru LL and remove the original copy


Result:
Runtime: 56 ms, faster than 10.88% of Python3 online submissions for Copy List with Random Pointer.
Memory Usage: 14.5 MB, less than 32.87% of Python3 online submissions for Copy List with Random Pointer.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        if not head:
            return head
        
        # create extended LL        
        curr = head
        
        while curr:
            tempNext = curr.next
            curr.next = Node(curr.val,tempNext)
            curr = curr.next.next   # go to next non deep copy val
        
        curr = head
        
        # set random pointers
        while curr:
            copyRand = None
            if curr.random:
                copyRand = curr.random.next
            curr = curr.next    # go to copy
            curr.random = copyRand
            curr = curr.next
        
        head = head.next    # start with copy
        curr = head
        
        # remove original copy
        while curr:
            if curr.next:
                curr.next = curr.next.next
            else:
                curr.next = None
            curr = curr.next
        
        return head
