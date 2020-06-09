class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0

#         Brute force solution
#         numOfPaths = 0
#         def traverse(col, row):
#             nonlocal numOfPaths
            
#             if col > m-1 or row > n-1:
#                 return
#             elif col == m-1 and row == n-1:
#                 numOfPaths += 1
#                 return
            
#             if col + 1 < m:
#                 traverse(col+1,row)
#             if row + 1 < n:
#                 traverse(col,row+1)
            
#         traverse(0,0)
#         return numOfPaths


        dp = [[1] * m for _ in range(n)]
        
        for row in range(1,n):
            for col in range(1,m):
                dp[row][col] = dp[row-1][col] + dp[row][col-1]

        return dp[-1][-1]