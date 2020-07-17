"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
Note: Do not modify the linked list.

Algorithm:

1) Iterate and add nodes to stack
2) if node is already in stack - cycle detected, return Node

Result:
Runtime: 64 ms, faster than 31.78% of Python3 online submissions for Linked List Cycle II.
Memory Usage: 16.8 MB, less than 83.84% of Python3 online submissions for Linked List Cycle II.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        
        cache = {}
        
        curr = head
        while curr:
            if curr in cache:
                return curr
            elif curr not in cache:
                cache[curr] = True
                curr = curr.next
        
        return None