"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:
Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.

Result:
Runtime: 4504 ms, faster than 44.58% of Python3 online submissions for Perfect Squares.
Memory Usage: 14.1 MB, less than 45.78% of Python3 online submissions for Perfect Squares.
"""

class Solution:
    def numSquares(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        
        # generate all squares
        squares = []
        i = 1
        squareVal = 1
        while squareVal <= n:
            squares.append(squareVal)
            i += 1
            squareVal = i**2
        
        # create dp table
        dp = [math.inf] * (n+1)
        dp[0] = 0
        
        #loop through each dp cell and determine lowest possible squares num for that number
        for i in range(1,n+1):
            
            # loop through squares arr
            for square in squares:
                if i < square:
                    break
                
                dp[i] = min(dp[i], dp[i-square]+1)
                
        return dp[-1]
        