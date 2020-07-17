"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).

Algorithm:
1) Find the smallest num index in array (binary search and compare middleValue with right pointer)
2) Decide which side of the array to compare against
3) Do a regular Binary search to find value


Result:
Runtime: 48 ms, faster than 30.60% of Python3 online submissions for Search in Rotated Sorted Array.
Memory Usage: 14.2 MB, less than 8.68% of Python3 online submissions for Search in Rotated Sorted Array.
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        elif len(nums) == 1:
            if nums[0] == target:
                return 0
            return -1
        
        
        # find index of smallest num
        
        l = 0
        r = len(nums)-1
        
        while l < r:    # Binary search for smallest value
            m = (l+r) // 2
            
            if nums[m] > nums[r]:
                l = m+1
            else:
                r = m

        if l == len(nums) - 1:  # decide which side of array to do binary search on
            if nums[l] == target:
                return l
            else:
                l = 0
                r = l-1
        if l > 0:
            if target >= nums[l] and target <= nums[-1]:
                r = len(nums)
            elif target <= nums[l-1] and target >= nums[0]:
                r = l-1
                l = 0
        elif l == 0:
            l = 0
            r = len(nums) - 1
        
        while l < r:    # regular binary search
            m = (l+r) // 2
            
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m+1
            else:
                r = m-1

        if l < len(nums) and nums[l] == target:
            return l
        
        return -1
   