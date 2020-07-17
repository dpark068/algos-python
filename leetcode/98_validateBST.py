"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Algorithm:
1) validate leftsubtree by setting parent node as the upperbound and passing lowerbound from parent node
2) validate rightsubtree by setting parent node as the lowerbound and passing upperbound from parent node
3) if node is between upper and lowerbound, then its valid

Result:
Runtime: 52 ms, faster than 39.59% of Python3 online submissions for Validate Binary Search Tree.
Memory Usage: 16.3 MB, less than 27.85% of Python3 online submissions for Validate Binary Search Tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        if not root:
            return True
        if root and not root.left and not root.right:
            return True
        
        def validate(node,lowerBound,upperBound):
            if not node:
                return True

            if not node.val > lowerBound or not node.val < upperBound:
                return False
            
            validLeft = validate(node.left,lowerBound,node.val)
            validRight = validate(node.right,node.val,upperBound)
            
            if validLeft and validRight:
                return True
            else:
                return False
        
        return validate(root,-inf,inf)
