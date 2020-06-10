"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Result:
Runtime: 96 ms, faster than 85.67% of Python3 online submissions for Valid Sudoku.
Memory Usage: 13.8 MB, less than 70.39% of Python3 online submissions for Valid Sudoku.
"""

class Solution:
    def isValidSudoku(self, board):
        
        rows = {0: [], 1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]}
        cols = {0: [], 1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]}
        
        # checks each row and col
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] != ".":
                    if board[row][col] in rows[row] or board[row][col] in cols[col]:
                        return False
                    else:
                        rows[row].append(board[row][col])
                        cols[col].append(board[row][col])

        midSqs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        midPoints = [(1,1),(1,4),(1,7),(4,1),(4,4),(4,7),(7,1),(7,4),(7,7)]
        
        # check midsquares
        for midPoint in midPoints:
            nums = [board[midPoint[0]][midPoint[1]]]
            for midSq in midSqs:
                newX = midSq[0] + midPoint[0]
                newY = midSq[1] + midPoint[1]
                if board[newX][newY] != ".":
                    if board[newX][newY] in nums:
                        return False
                    else:
                        nums.append(board[newX][newY])
        
        return True


test = [
    ["9",".",".","6",".",".",".",".","."],
    [".",".",".",".","6",".",".",".","."],
    [".",".",".",".",".","1",".","3","."],
    [".",".",".",".",".",".",".",".","8"],
    [".",".",".",".",".","8",".",".","."],
    [".",".",".","4",".",".","2",".","."],
    [".",".",".",".",".",".",".",".","1"],
    ["6",".",".",".","1",".",".",".","."],
    [".",".",".",".",".",".",".",".","."]
]

s = Solution()
print(s.isValidSudoku(test))