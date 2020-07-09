"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.

Algorithm:
1) Loop through all edges and dfs and set all neighbors to "-"
2) Loop through again and set "-" to 'O' and 'O' to 'X'

Result:
Runtime: 236 ms, faster than 14.32% of Python3 online submissions for Surrounded Regions.
Memory Usage: 15.8 MB, less than 26.28% of Python3 online submissions for Surrounded Regions.
"""

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        if not board or len(board) <= 2: return
        
        def dfs(r,c):
            
            board[r][c] = "-"
            
            validNbrs = []
            offsets = [(0,-1),(0,1),(-1,0),(1,0)]
            for offset in offsets:
                newR = r + offset[0]
                newC = c + offset[1]
                
                if newR >= 0 and newR < len(board) and newC >= 0 and newC < len(board[0]) and board[newR][newC] == 'O':
                    validNbrs.append((newR,newC))
            
            for nbr in validNbrs:
                dfs(nbr[0],nbr[1])
            
        
        # change all edge O's to -'s
        
        for pos in range(len(board[0])): # top row
            if board[0][pos] == 'O':
                dfs(0,pos)
        
        for pos in range(len(board)):   # right col
            if board[pos][len(board[0])-1] == 'O':
                dfs(pos,len(board[0])-1)
        
        for pos in range(len(board[0])): # bottom row
            if board[len(board)-1][pos] == 'O':
                dfs(len(board)-1,pos)
        
        for pos in range(len(board)): # left col
            if board[pos][0] == 'O':
                dfs(pos,0)
        
        # iterate through and swap all '-' to 'O' and 'O' to 'X'
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == '-':
                    board[row][col] = 'O'
        