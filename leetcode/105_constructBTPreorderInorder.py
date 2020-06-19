"""
Given preorder and inorder traversal of a tree, construct the binary tree. You may assume that duplicates do not exist in the tree.

For example, given
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

Result:
Runtime: 216 ms, faster than 33.37% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
Memory Usage: 88.9 MB, less than 5.01% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        
        
        def setTree(preArr, inArr):
            
            if len(preArr) == 0 or len(inArr) == 0:
                return None
        
            #base case - if single node then set it and return
            # if len(preArr) == 1 and len(inArr) == 1:
            #     return TreeNode(val=preArr[0])
            
            # set first node in pre, split into left then right right nodes
            currVal = preArr[0]
            currNode = TreeNode(val=currVal)
            
            inArrIndex = inArr.index(currVal)
            
            leftInArr = inArr[:inArrIndex]
            rightInArr = inArr[inArrIndex+1: ]
            
            # to find leftPreArr and rightPreArr

            leftPreArr = preArr[1: inArrIndex+1]
            rightPreArr = preArr[inArrIndex+1: ]
            
            print(currVal)
            print(inArrIndex)
            print(leftInArr)
            print(rightInArr)
            print(leftPreArr)
            print(rightPreArr)
            print("")
            
            currNode.left = setTree(leftPreArr,leftInArr)
            currNode.right = setTree(rightPreArr, rightInArr)
            
            return currNode
        
        root = setTree(preorder, inorder)
        return root