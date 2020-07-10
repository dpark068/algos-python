"""
You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, 
which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, 
to produce a multilevel data structure, as shown in the example below.
Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.

Algorithm:
1) Iterate through LL and check for child
2) if child, 
    a) set the current Node next val to child 
    b) set child node prev val to curr node
    c) Keep a pointer on original next node
3) Similarly iterate through the child level LL and check for additional childs
4) Recursion should return the last node
5) Set recurse returned last node next Val to original node next val
6) Set original node next val prev value to recursed last node val

Result:
Runtime: 40 ms, faster than 51.85% of Python3 online submissions for Flatten a Multilevel Doubly Linked List.
Memory Usage: 14.4 MB, less than 51.45% of Python3 online submissions for Flatten a Multilevel Doubly Linked List.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        
        if not head or (not head.next and not head.child):
            return head
        
        curr = head
            
        def childRecurse(node): # recurse into child node and repeat
            """ Similar to function below for iterating through LL except return the last Node (not Null) """
            curr = node
            
            while curr:
                if not curr.child:
                    if not curr.next:
                        lastNode = curr
                    curr = curr.next
                else:
                    originalNext = curr.next
                    curr.next = curr.child
                    curr.next.prev = curr
                    lastChildNode = childRecurse(curr.child)
                    if originalNext:
                        lastChildNode.next = originalNext
                        lastChildNode.next.prev = lastChildNode
                    else:
                        lastNode = lastChildNode
                    curr.child = None
                    curr = originalNext

            return lastNode
            
        while curr: # iterate through level 0 LL
            if not curr.child:  # if no child keep iterating
                curr = curr.next
            else:   # if child, keep pointers referenced to current, next and child
                originalNext = curr.next
                curr.next = curr.child
                curr.next.prev = curr
                lastChildNode = childRecurse(curr.child)    # returned node is the last node in child
                if originalNext:    # if there is a next node, set lastChildNode next as original next
                    lastChildNode.next = originalNext
                    lastChildNode.next.prev = lastChildNode
                curr.child = None   # erase child reference to current node
                curr = originalNext # set curr pointer to original next
            
        curr = head
        
        # if youd like to see what are the references at end
        # while curr:
        #     print("currVal: " + str(curr.val))
        #     print("currNextVal: " + str(curr.next.val) if curr.next else "no next")
        #     print("currPrevVal: " + str(curr.prev.val) if curr.prev else "no prev")
        #     print("currChild: " + str(curr.child))
        #     print("")
        #     curr = curr.next

        return head
        
        