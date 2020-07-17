"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Algorithm:
1) create a dp table will all 0s, dp table will hold max square possible at that cell
2) look at cells with offset [(0,-1),(-1,-1),(-1,0)] and compute min value for the three cells on dp table
3) if matrix cell is 0, continue, if its a 1, add 1 to the previous computed min value 

Result:
Runtime: 348 ms, faster than 18.99% of Python3 online submissions for Maximal Square.
Memory Usage: 14.6 MB, less than 52.98% of Python3 online submissions for Maximal Square.
"""

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        dp = [[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)] # create 0's for first row and col
        
        maxNum = 0  # max range on squares
        
        for row in range(1,len(matrix)+1):  # compute with offset since first row and col are 0s
            for col in range(1,len(matrix[0])+1):
                if matrix[row-1][col-1] == '0':
                    continue
                else:
                    dp[row][col] = min(dp[row][col-1],dp[row-1][col-1],dp[row-1][col]) + int(matrix[row-1][col-1])
                    
                    if dp[row][col] > maxNum:
                        maxNum = dp[row][col]
        
        return maxNum**2