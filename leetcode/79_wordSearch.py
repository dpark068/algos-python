"""
Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Algorithm:
1) Simple DFS backtracking

result:
TLE
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        if not board or not word:
            return False
        
        wordInBoard = False
        visited = {}
        def validNbrs(r,c,pos,word):
            offsets = [(0,-1),(0,1),(-1,0),(1,0)]
            nbrs = []
            
            for offset in offsets:
                newR = r + offset[0]
                newC = c + offset[1]
                
                if (newR >= 0 and newR < len(board) and newC >= 0 and newC < len(board[0])) and board[newR][newC] == word[pos+1]:
                    nbrs.append((newR,newC))
            
            return nbrs
        
        def dfs(r,c,pos,word):
            nonlocal wordInBoard
            
            # if (r,c,pos) in visited:
            #     return
            #print("r: " + str(r) + " c: " + str(c))
            if pos == len(word)-1:
                if word[pos] == board[r][c]:
                    wordInBoard = True
                return
            
            if board[r][c] != word[pos]:
                return
            
            tempVal = board[r][c]
            board[r][c] = "-"
            nbrs = validNbrs(r,c,pos,word)
            #print("nbrs: " + str(nbrs))
            for nbr in nbrs:
                dfs(nbr[0],nbr[1],pos+1,word)
            
            board[r][c] = tempVal
            # visited[(r,c,pos)] = True
            
        for row in range(len(board)):
            for col in range(len(board[0])):
                if wordInBoard:
                    return wordInBoard
                if board[row][col] == word[0]:
                    #print("row: " + str(row) + " col: " + str(col))
                    dfs(row,col,0,word)
        
        #print(wordInBoard)
        return wordInBoard