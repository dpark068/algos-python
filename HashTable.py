# Hash Table - collection of items stored in a way to find them later easily
# Hashing - build data structure that can be searched in O(1)

def hash(astring, tablesize):
    """ takes a string and a table size and returns the hash value in the range from 0 to tablesize-1 """

class HashTable:

    def __init__(self, size=11):
        self.slots = [None] * size
        self.data = [None] * size
        self.size = size

    def put(self,key,data):
        """ Find available slot to put data in
        1) calculate hash pos
        2) if pos is empty - put value into position
        3) if pos filled, check if the value in the slot is the same. If it is, change value
        4) If key is different, keep rehashing until hash key is none or key is not the same
        5) If slot is none, add key and val to empty slot
        6) If key is same, change value
        """
        hashPos = self.hashfunction(key,self.size)

        if self.slots[hashPos] is None:
            self.slots[hashPos] = key
            self.data[hashPos] = data
        else:
            if self.slots[hashPos] == key:
                self.data[hashPos] = data
            else:
                rehashPos = self.rehash(hashPos,self.size)
                while self.slots[rehashPos] is not None and self.slots[rehashPos] != key:
                    rehashPos = self.rehash(rehashPos, self.size)
                
                if self.slots[rehashPos] is None:
                    self.slots[rehashPos] = key
                    self.data[rehashPos] = data
                elif self.slots[rehash] == key:
                    self.data[rehashPos] = data
        
    def hashfunction(self,key,size):
        """ Function to find hash position, will go with simple hashing"""
        return key%size

    def rehash(self,oldhash,size):
        """ hash the old hash -> (oldHash + skip) % tableSize"""
        return (oldhash + 1) & self.size

    def get(self,key):
        """ 
        1) Compute hash and check if key is equal
        2) if not keep rehashing until hitting empty slot or key is the same
        3) make sure you dont loop continuously
        """
        hashPos = self.hash(key,self.size)

        if self.slots[hashPos] == key:
            return self.data[hashPos]
        else:
            rehashPos = self.rehash(hashPos, self.size)
            while self.slots[rehashPos] != None and self.slots[rehashPos] != key:
                rehashPos = self.rehash(rehashPos, self.size)
                if rehashPos == hashPos:
                    return None
            if self.slots[rehashPos] == key:
                return self.data[rehashPos]
            elif self.slots[rehashPos] is None:
                return None
            



    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        return self.put(key,data)
