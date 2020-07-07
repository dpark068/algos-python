"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

Algorithm:
1) DFS + memoization - cache indexes visited
2) Explorer all choices

Algo2:
1) Iterate reverse and see if position can reach the lastIndex
2) if so, set last index as the current pos
3) if not continue, checking to see if there is a larger value in arr that can reach the current lastIndex

Result:
Runtime: 140 ms, faster than 14.02% of Python3 online submissions for Jump Game.
Memory Usage: 15.9 MB, less than 39.34% of Python3 online submissions for Jump Game.
"""

class Solution:     # TLE
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        if len(nums) == 1:
            return True
        
        found =False
        lastIndex = len(nums) - 1
        cache = {}
        
        def dfs(index):
            nonlocal found
            if index in cache or found:
                return
            if index == lastIndex:
                found = True
                return
            elif index > lastIndex:
                cache[index] = found
                return
            for i in range(nums[index],0,-1):
                if index+i not in cache:
                    dfs(index+i)
            
            cache[index] = found
            
        for startNum in range(nums[0],0,-1):
            if found:
                return found
            dfs(startNum)
        return found


class Solution2:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        if len(nums) == 1:
            return True
        
        lastIndex = len(nums) - 1
        
        for pos in range(len(nums)-2,-1,-1):
            if pos + nums[pos] >= lastIndex:
                lastIndex = pos

        return lastIndex == 0