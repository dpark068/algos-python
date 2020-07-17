"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

Algorithm:
1) Use dp table to keep track of the minimum sum to a certain position
2) First row and first col, set the value as the sum of prior path to the position
3) For all other cells, the value is the determined by the min sum of [(row,col-1) and (row-1,col)] + arr[row][col]
4) The value at end of table is the min sum

Result:
Runtime: 96 ms, faster than 93.70% of Python3 online submissions for Minimum Path Sum.
Memory Usage: 15.2 MB, less than 79.53% of Python3 online submissions for Minimum Path Sum.
"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0
        
        dp = [[None]*len(grid[0]) for _ in grid]
        
        dp[0][0] = grid[0][0]
        
        for col in range(1,len(grid[0])):
            dp[0][col] = dp[0][col-1] + grid[0][col]
        
        for row in range(1,len(grid)):
            dp[row][0] = dp[row-1][0] + grid[row][0]
        
        for row in range(1,len(grid)):
            for col in range(1,len(grid[0])):
                dp[row][col] = min(dp[row][col-1],dp[row-1][col])+ +grid[row][col]
        
        return dp[-1][-1]