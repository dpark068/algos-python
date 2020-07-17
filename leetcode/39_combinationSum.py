"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
The same repeated number may be chosen from candidates unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Algorithm:
1) use backtracking and keep looping through until value is greater or equal to target

Result:
Runtime: 1224 ms, faster than 5.10% of Python3 online submissions for Combination Sum.
Memory Usage: 13.7 MB, less than 90.29% of Python3 online submissions for Combination Sum.
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates or not target:
            return []
        
        totalSums = []
        totalSumsDict = {}
        def dfs(currSum, currNums, totalSums):
            if currSum > target:
                return
            elif currSum == target:
                tempNum = currNums[:]
                tempNum.sort()
                if tuple(tempNum) not in totalSumsDict:
                    totalSums.append(tempNum)
                    totalSumsDict[tuple(tempNum)] = True
                return
            
            for i in range(len(candidates)):
                currSum += candidates[i]
                currNums.append(candidates[i])
                dfs(currSum, currNums, totalSums)
                
                currSum -= candidates[i]
                currNums.pop()
        
        
        
        dfs(0, [],totalSums)
        return totalSums
