# AVL Tree aka Balanced Binary Search Trees is similar to BST but difference is tracking balance factor
# balanceFactor = height(leftSubtree) - height(rightSubtree)
# Tree is balanced if BF = -1, 0, 1
# Claim - balance tree can result in better Big-O performance of key operations
# Searching AVL Tree --> O(log N(h)), number of nodes at height
from BinarySearchTreeSolution import TreeNode, BinarySearchTree

class BalancedTree(BinarySearchTree):
    def _put(self,key,val,currentNode: TreeNode):
        """ Similar to BST, also update parent balance factor """
        if key < currentNode.key: # go Left
            if currentNode.hasLeftChild():
                self._put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val)
                self.updateBalance(currentNode.leftChild)
        else: # go right key > currentNode.key
            if currentNode.hasRightChild():
                self._put(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val)
                self.updateBalance(currentNode.rightChild)

    def updateBalance(self,node):
        """ Update balance factor of parents node. 
            1) check if node is out of balance >1 or <-1, if so rebalance and return
            2) check whether current node is left/right child and update parent balance
            3) if parent node is not zero, update balance for parent node
        """
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.rebalance(node)
            return
        
        if node.isLeftChild():
            node.parent.balanceFactor += 1
        elif node.isRightChild():
            node.parent.balanceFactor -= 1

        if node.parent.balanceFactor != 0:
            self.updateBalance(node.parent)

    def rotateLeft(self,rotRoot):
        """ Left rotation as part of rebalancing tree
        1) create new root with right child as parent
        2) realign references of parent and child 
        3) If old root is the root then set self.root, else set parent and child references
        4) if new root has left child, make it the right child of old root
        5) update balance factor of old and new root
        """
        newRoot = rotRoot.rightChild
        if newRoot.hasLeftChild():
            newRoot.leftChild.parent = rotRoot
        newRoot.parent = rotRoot.parent

        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot

        newRoot.leftChild = rotRoot
        rotRoot.parent = newRoot
        
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 + min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor, 0)
        
    def rotateRight(self,rotRoot):
        """ Symmetric to rotateLeft"""
        newRoot = rotRoot.leftChild
        if newRoot.hasRightChild():
            newRoot.leftChild.parent = rotRoot
        newRoot.parent = rotRoot.parent

        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            elif rotRoot.isRightChild():
                rotRoot.parent.rightChild = newRoot
        
        newRoot.rightChild = rotRoot
        rotRoot.parent = newRoot

        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor, 0)

    def rebalance(self,node):
        """ rebalance"""

        if node.balanceFactor < 0: #right heavy so requires left rotation
            if node.rightChild.balanceFactor > 1 : # left heavy BF for rightChild
                self.rotateRight(node.rightChild)
            self.rotateLeft(node)
        elif node.balanceFactor > 0: # left heavy so rotate right
            if node.leftChild < 0:
                self.rotateLeft(node.leftChild)
            self.rotateRight(node)
        
