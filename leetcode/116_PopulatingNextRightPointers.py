"""
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.

Result:
Runtime: 76 ms, faster than 27.96% of Python3 online submissions for Populating Next Right Pointers in Each Node.
Memory Usage: 15.4 MB, less than 44.24% of Python3 online submissions for Populating Next Right Pointers in Each Node.

Algorithm:
DS - Queue

1) Store level of node and node in stack
2) have a current pointer that points to the curr pointer in stack
3) If currPointerLevel and node popped from Queue are different, a) assign curr.next = None b) curr = newNode c) increase curr level
4) add left and right child of node popped from queue
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return root
        
        if root.left is None and root.right is None:
            return root
        
        stack = [(0,root)]
        curr = root
        currLevel = 0
        #will be doing BFS search
        while len(stack) != 0:
            node = stack.pop(0)
            
            # check if level is the same
            if currLevel < node[0]:
                # nevel level - end current pointer, assign node as new curr and increase level
                curr.next = None
                curr = node[1]
                currLevel += 1
            else:
                # else assign as next and set current to new Node
                curr.next = node[1]
                curr = curr.next
            
            #add the left and right child
            if node[1].left:
                stack.append((node[0] + 1,node[1].left))
            if node[1].right:
                stack.append((node[0] + 1,node[1].right))
        
        return root