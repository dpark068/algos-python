"""
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

Result:
Runtime: 276 ms, faster than 84.03% of Python3 online submissions for 4Sum II.
Memory Usage: 34.5 MB, less than 88.58% of Python3 online submissions for 4Sum II.
"""

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        
        abVals = {}
        # A+ B --> store in dict num of occurences
        for a in A:
            for b in B:
                if a+b not in abVals:
                    abVals[a+b] = 1
                else:
                    abVals[a+b] += 1
        
        totalCount = 0
        
        # loop through C+D and check dict to see if val exists - add num of occurences
        for c in C:
            for d in D:
                if -(c+d) in abVals:
                    totalCount += abVals[-(c+d)]
        
        return totalCount