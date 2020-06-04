# Binary Heaps - ordered collection of nodes in an array
# root will always be min
# root, left = 2n, right = 2n + 1

class BinaryHeap():
    def __init__(self):
        self.aList = [0]
        self.size = 0
    
    def insert(self, item):
        self.aList.append(item)
        self.size += 1
        self.percup(self.size)
    
    def percup(self, i):
        """ swap last value upward if value is larger than the node above """
        while i // 2 > 0:
            if self.aList[i] < self.aList[i // 2]:
                self.aList[i], self.aList[i // 2] = self.aList[i // 2], self.aList[i]
            i = i // 2

    def delMin(self):
        """Delete minimum value at root """
        print(self.aList[1])
        self.aList[1] = self.aList[self.size]
        self.size -= 1
        self.aList.pop()
        # Get last item and move it to front of arr and percdown
        self.percdown(1)
    
    def percdown(self, i):
        # swap with minimum value

        while i * 2 <= self.size:
            if self.aList[i] > self.aList[self.checkMin(i)]:
                self.aList[i], self.aList[self.checkMin(i)] = self.aList[self.checkMin(i)], self.aList[i]

            i = self.checkMin(i)
    def checkMin(self, i):
        # Return child position with lower value
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.aList[i * 2] < self.aList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1
    
    def buildHeap(self, aList):
        """ Build heap -> O(n) """
        self.size = len(aList)
        # Any nodes past the halfway point will be leaves and therefore have no children.
        i = self.size // 2
        self.aList = [0] + aList

        while i > 0:
            self.percdown(i)
            i = i-1


# Test BinaryHeap
heap = BinaryHeap()
heap.buildHeap([9,5,6,2,3])

heap.delMin()
heap.delMin()
heap.delMin()
heap.delMin()
heap.delMin()





        