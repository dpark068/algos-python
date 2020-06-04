# BST Implementation

class TreeNode:
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.leftChild

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return self.parent is None

    def isLeaf(self):
        return self.leftChild is None and self.rightChild is None

    def hasAnyChildren(self):
        return self.leftChild or self.rightChild

    def hasBothChildren(self):
        return self.leftChild and self.rightChild

    def spliceOut(self):
        """ Realign parent and child node to reference each other"""
        if self.isLeaf():
            if self.parent:
                if self.isLeftChild():
                    self.parent.leftChild = None
                else:
                    self.parent.rightChild = None
        else:
            if self.hasAnyChildren():
                if self.hasLeftChild():
                    if self.isLeftChild():
                        self.parent.leftChild = self.leftChild
                    else:
                        self.parent.rightChild = self.leftChild
                    self.leftChild.parent = self.parent
                else:
                    if self.isLeftChild():
                        self.parent.leftChild = self.rightChild
                    else:
                        self.parent.rightChild = self.rightChild
                    self.rightChild.parent = self.parent

    def findSuccessor(self):
        """
        1) if node has right child, the smallest key in rightchild subtree is the successor
        2) if the node has no right child, if node is the left child of parent, its parent is the successor
        3) if the node has no right child, if node is right child of parent, its successor is the parents successor, excluding current node
        """
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        elif self.parent:
            if self.parent.leftChild == self:
                succ = self.parent
            elif self.parent.rightChild == self:
                self.parent.rightChild = None
                succ = self.findSuccessor(self.parent)
                self.parent.rightChild = self
        return succ
    def findMin(self):
        """ Min node is always on the left most node in BST """
        curr = self
        while curr.hasLeftChild():
            curr = self.leftChild
        return curr

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.value = value
        self.leftChild = lc
        self.rightChild = rc
        #Handle parent reference in child nodes
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self
        


class BinarySearchTree:

    def __init__(self):
        self.size = 0
        self.root = None

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self,key,val):
        if self.root:
            self_put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size += 1
    
    def _put(self,key,val,currentNode):
        """ Go left if key is smaller than current, go right if larger. Keep going until find empty spot """
        if (key < currentNode.key):
            if currentNode.hasLeftChild():
                _put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key,val, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                _put(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key,val, parent=currentNode)

    def __setitem__(self,k,v):
        """ Able to use arr['key'] = value """
        self.put(k,v)

    def get(self,key):
        """ Get Node from Tree """
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
        else:
            # Nothing in Tree
            return None

    def _get(self,key,currentNode):
        """ Go left if key is smaller than current Node and right if key is larger
            Return if key == current Node Key
            Return None if key doesnt exist
        """
        
        if key == currentNode.key:
            return currentNode
        elif key < currentNode.key:
            if currentNode.hasLeftChild():
                self._get(key, currentNode.leftChild)
            else:
                return None
        else:
            if currentNode.hasRightChild():
                self._get(key, currentNode.rightChild)
            else:
                return None

    def __getitem__(self,key):
        return self.get(key)

    def __contains__(self,key):
        if self.get(key):
            return True
        else:
            return False

    def delete(self,key):
        """ Check size to see if its not root that needs to be deleted """
        if self.size > 1:
            nodeToRemove = self.get(key)
            if nodeToRemove:
                self.remove(nodeToRemove)
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1:   #Remove root node
            if key == self.root.key:
                self.root = None
                self.size = 0
            else:
                raise KeyError('Error, key not in tree')

    def __delitem__(self,key):
        self.delete(key)
    
    def remove(self,currentNode):
        """ 
        1) Handle leaf nodes - just delete parent references
        2) Handle one child - Just promote child node to current node by swapping parent references and its own parent reference
        3) Handle two child - find a successor + splice it out then assign current node key and value
        """
        if self.isLeaf(): # has no child
            if self.parent:
                if isLeftChild():
                    self.parent.left = None
                else:
                    self.parent.right = None
        
        elif self.hasAnyChildren(): # has one child
            if self.hasLeftChild(): # left child
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                    self.leftChild.parent = self.parent
                elif self.isRightChild():
                    self.parent.rightChild = self.leftChild
                    self.rightChild.parent = self.parent
                else:
                    currentNode.replaceNodeData(
                        currentNode.leftChild.key,
                        currentNode.leftChild.payload,
                        currentNode.leftChild.leftChild,
                        currentNode.leftChild.rightChild
                    )
            else: # right child
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                    self.rightChild.parent = self.parent
                elif self.isRightChild():
                    self.parent.rightChild = self.rightChild
                    self.rightChild.parent = self.parent
                else:
                    currentNode.replaceNodeData(
                        currentNode.rightChild.key,
                        currentNode.rightChild.payload,
                        currentNode.rightChild.leftChild,
                        currentNode.rightChild.rightChild
                    )
        
        elif self.hasBothChildren(): # 2 children
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload





mytree = BinarySearchTree()
mytree[3]="red"
mytree[4]="blue"
mytree[6]="yellow"
mytree[2]="at"

print(mytree[6])
print(mytree[2])
