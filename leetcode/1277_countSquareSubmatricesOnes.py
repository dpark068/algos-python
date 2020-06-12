"""
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

Solution:
Use memoization
1) The left most col and upmost row is set to itself
2) look through dp table and notice that the value depends on the prior 3 cells (offsets)
3) will grab the lowest value + 1 for that cell unless there is a zero - value == 1

Runtime: 916 ms, faster than 33.34% of Python3 online submissions for Count Square Submatrices with All Ones.
Memory Usage: 15.9 MB, less than 56.70% of Python3 online submissions for Count Square Submatrices with All Ones.
"""

class Solution:
    def countSquares(self, matrix):
        if len(matrix) == 0:
            return 0
        
        dp = [ [0] * len(matrix[0]) for _ in range(len(matrix))]
        
        total = 0

        # set the 0th row to itself
        for i in range(len(matrix[0])):
            dp[0][i] = matrix[0][i]
            total += matrix[0][i]
         
        print(total) 
        # set the 0th col to itself
        for i in range(1,len(matrix)):
            dp[i][0] = matrix[i][0]
            total += matrix[i][0]
        
        # look at dp table and figure out what value is
        def sameNumPre(r,c):
            offsets = [(0,-1),(-1,0),(-1,-1)]
            
            nbrs = []
            minVal = None
            for offset in offsets:
                newR = r + offset[0]
                newC = c + offset[1]
                
                if newR >= 0 and newR < len(matrix) and newC >=0 and newC < len(matrix[0]):
                    nbrs.append(dp[newR][newC])
                    if not minVal and dp[newR][newC] > 0:
                        minVal = dp[newR][newC]
                    if minVal and dp[newR][newC] < minVal:
                        minVal = dp[newR][newC]
            if 0 in nbrs:
                return 1
            else:
                return minVal + 1
        
        for row in range(1,len(matrix)):
            for col in range(1,len(matrix[0])):
                if matrix[row][col] == 1:
                    val = sameNumPre(row,col)
                    total += val
                    dp[row][col] = val
                else:
                    dp[row][col] = 0
        
        return total


s = Solution()
# matrix =[
#   [0,1,1,1],
#   [1,1,1,1],
#   [0,1,1,1]
# ]
matrix = [[1,0,1],[1,1,0],[1,1,0]]
print(s.countSquares(matrix))