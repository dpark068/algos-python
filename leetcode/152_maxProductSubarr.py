"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Algorithm:
1) keep track of min and max values at each iteration (accounts for negative vals)
2) Max product subarr is basically comparing current max val with global max

Result:
Runtime: 116 ms, faster than 6.28% of Python3 online submissions for Maximum Product Subarray.
Memory Usage: 13.8 MB, less than 94.38% of Python3 online submissions for Maximum Product Subarray.
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        
        
        globalMaxProduct = minProduct = maxProduct = nums[0]
        
        for i in range(1,len(nums)):
            preMaxProduct = maxProduct
            preMinProduct = minProduct
            
            minProduct = min(nums[i],preMaxProduct*nums[i],preMinProduct*nums[i])
            maxProduct = max(nums[i],preMaxProduct*nums[i],preMinProduct*nums[i])
            
            globalMaxProduct = max(globalMaxProduct,maxProduct)
        
        return globalMaxProduct
        