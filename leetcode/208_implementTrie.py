"""
Implement a trie with insert, search, and startsWith methods.

Result:
Runtime: 132 ms, faster than 91.14% of Python3 online submissions for Implement Trie (Prefix Tree).
Memory Usage: 27.2 MB, less than 73.57% of Python3 online submissions for Implement Trie (Prefix Tree).
"""

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trieDict = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """ 
        
        pointer = self.trieDict  # trick is to use pointers to reference a sub dict within a dict
        for char in word:
            if char not in pointer:
                pointer[char] = {}
            pointer = pointer[char]
        
        pointer["-"] = True # indicates the end of a word
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        pointer = self.trieDict
        for char in word:
            if char not in pointer:
                return False
            else:
                pointer = pointer[char]
        
        if "-" in pointer: 
            return True #determines if word in a subword or actual word
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        pointer = self.trieDict
        for char in prefix:
            if char not in pointer:
                return False
            else:
                pointer = pointer[char]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)