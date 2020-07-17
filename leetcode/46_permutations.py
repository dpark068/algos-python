"""
Given a collection of distinct integers, return all possible permutations.

Algorithm:
1) dfs backtracking

Result:
Runtime: 44 ms, faster than 51.85% of Python3 online submissions for Permutations.
Memory Usage: 13.8 MB, less than 87.38% of Python3 online submissions for Permutations.
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        elif len(nums) == 1:
            return [[nums[0]]]
        
        result = []
        arr = nums[:]
        
        def dfs(arr,output,result):
            
            if not arr:
                result.append(output[:])
            
            for i in range(len(arr)):
                tempNum = arr.pop(i)
                output.append(tempNum)
                
                dfs(arr,output,result)
                
                output.pop()
                arr.insert(i,tempNum)
        
        dfs(arr,[],result)
        return result
            