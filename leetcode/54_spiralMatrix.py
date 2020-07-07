"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Algorithm:
1) Have 4 for loops that checks each side with a corresponding pointer reference on each side
2) set the proper boundaries top,right,bottom,left
3) keep checking if len of arr matches size of matrix

Result:
Runtime: 32 ms, faster than 51.20% of Python3 online submissions for Spiral Matrix.
Memory Usage: 13.6 MB, less than 96.79% of Python3 online submissions for Spiral Matrix.
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        if not matrix: return []
        elif len(matrix) == 1: return matrix[0]
        
        arr = []
        totalNum = len(matrix) * len(matrix[0])
        
        topRow = 0
        bottomRow = len(matrix) - 1
        leftCol = 0
        rightCol = len(matrix[0]) - 1
        
        count = 0
        while len(arr) != totalNum:
            
            # top row
            for topRowPos in range(leftCol,rightCol+1):
                arr.append(matrix[topRow][topRowPos])
            
            topRow += 1
            if len(arr) == totalNum:
                break
            
            # right Col
            for rightColPos in range(topRow,bottomRow+1):
                arr.append(matrix[rightColPos][rightCol])
            rightCol -= 1
            if len(arr) == totalNum:
                break
            
            # bottom Row reverse
            for bottomRowPos in range(rightCol,leftCol-1,-1):
                arr.append(matrix[bottomRow][bottomRowPos])
            bottomRow -= 1
            if len(arr) == totalNum:
                break
            
            #leftCol upwards
            for leftColPos in range(bottomRow,topRow-1,-1):
                arr.append(matrix[leftColPos][leftCol])
            leftCol += 1
            if len(arr) == totalNum:
                break

        return arr
            
                
                