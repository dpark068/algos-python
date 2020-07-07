"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
The cache is initialized with a positive capacity.
Follow up:
Could you do both operations in O(1) time complexity?

Algorithm:
1) use ordered dictionary, always place recent add/requested items to end of dict
2) if reached capacity, popitem in beginning of dict (least recently used)
3) if not, add item to dict and increment current capacity

Result:
Runtime: 176 ms, faster than 96.47% of Python3 online submissions for LRU Cache.
Memory Usage: 22.9 MB, less than 86.82% of Python3 online submissions for LRU Cache.
"""

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.currCapacity = 0
        self.cache = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
        elif self.currCapacity == self.capacity:
            self.cache.popitem(last=False)
            self.cache[key] = value
        else:
            self.cache[key] = value
            self.currCapacity += 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)