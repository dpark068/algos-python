"""
Given a binary tree, flatten it to a linked list in-place.

Algorithm:
1) Use recursion - flatten left and flatten right subtree
2) set currNode.right equal to flattenLeft
3) set flattenedRight tree to end of the flattened left subtree
4) set currNode.left as None

Result:
Runtime: 64 ms, faster than 10.71% of Python3 online submissions for Flatten Binary Tree to Linked List.
Memory Usage: 14.5 MB, less than 69.42% of Python3 online submissions for Flatten Binary Tree to Linked List.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        if not root:    # no root case
            return
        
        
        def flattenSubtree(node):   # will flatten left and right
            if not node.left and not node.right:     # leaf
                return node
            
            
            if node.left:   # if left subtree, will flatten Left and set it to right
                flatLeftTree = flattenSubtree(node.left)
                if node.right:  # if right subtree, flatten right and set currNode.right as flattenLeftTree
                    originalRight = flattenSubtree(node.right)
                    
                    node.right = flatLeftTree
                    curr = node.right
                    while curr.right:   # will iterate to end of flattened left subtree
                        curr = curr.right
                    curr.right = originalRight  # set flattenedRight at end of flattened left
                else:   # if no right, just set flattenedLeft as right
                    node.right = flatLeftTree
            else:   # if no left, just flatten right subtree
                if node.right:
                    flattenSubtree(node.right)
                
            
            node.left = None    # delete left subtree
            return node
        
        return flattenSubtree(root)