"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:
Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 

Algorithm:
1) Create dp table to track longest sequence at a certain position in arr
2) * compare with current pointer whether value is greater than current value, if it is + 1 or its own value (whichever is greater)
3) return max value in arr

Algorithm2: patience sorting method
1) Create array of stacks and append each num from left to right
2) For longest increasing Subsequence, just need to look at num of stacks in arr

Result:
Runtime: 1192 ms, faster than 44.63% of Python3 online submissions for Longest Increasing Subsequence.
Memory Usage: 14.1 MB, less than 34.15% of Python3 online submissions for Longest Increasing Subsequence.
"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        dp = [1] * (len(nums))

        for curr in range(1,len(nums)):
            
            for subset in range(curr):
                if nums[curr] > nums[subset]:

        return max(dp)