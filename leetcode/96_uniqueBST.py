"""
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Algorithm:
1) Iterate n times
1b) within each iteration, iterate from 1 - current n (mimcs selecting the first number) 
2) Use dp table to cache - number of unique BSTs for a given n
3) when calculating larger n's - can leverage previous computed dp table
4) when selecting a number, will use the numbers that go to left and right subtree (BST - behavior)
5) use prior sum to determine number of sub BSTs possible

Result:
Runtime: 28 ms, faster than 74.86% of Python3 online submissions for Unique Binary Search Trees.
Memory Usage: 14 MB, less than 12.39% of Python3 online submissions for Unique Binary Search Trees.
"""

class Solution:
    def numTrees(self, n: int) -> int:
        if n == 1:
            return 1
        
        dp = [0,1]

        for i in range(2,n+1):  # iterate n times

            dp.append(0)    # start with value as 0
            for j in range(1,i+1):  # iterate from 1 -> i (mimics selecting first digit)
                leftNumCount = j-1  # number of left nums
                rightNumCount = i-j # num of right nums
                
                if leftNumCount < 1:    # ensure for empty string its a 1 
                    leftNumCount = 1
                if rightNumCount < 1:
                    rightNumCount = 1
                    
                dp[i] += dp[leftNumCount] * dp[rightNumCount]   # add for each j iteration, multiply left and right possibilities
        
        return dp[-1]
                
            