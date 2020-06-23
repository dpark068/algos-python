"""
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.
The successor of a node p is the node with the smallest key greater than p.val.

Algorithm:
1) if curr node is greater than p, set successor as curr node and traverse left
2) if curr node is less than p, go right
3) if curr node equals p, check if it has a right child, if so, get the right child's left most child (leaf node) as successor
4) If curr node equals p and no right child, return previously set successor node

Result:
Runtime: 76 ms, faster than 68.39% of Python3 online submissions for Inorder Successor in BST.
Memory Usage: 17.9 MB, less than 18.43% of Python3 online submissions for Inorder Successor in BST.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if root is None or p is None:
            return None
        
        succ = None
        def traverse(node):
            nonlocal succ
            if node.val == p.val:
                # if right child get left most key of that right child
                if node.right:
                    rightChild = node.right
                    while rightChild:
                        succ = rightChild
                        rightChild = rightChild.left

            elif node.val > p.val:
                succ = TreeNode(node.val)
                traverse(node.left)
            elif node.val < p.val:
                traverse(node.right)
        
        traverse(root)
        return succ