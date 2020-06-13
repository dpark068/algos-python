"""
A peak element is an element that is greater than its neighbors.
Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.
The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
You may imagine that nums[-1] = nums[n] = -∞.

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Result:
Runtime: 40 ms, faster than 92.30% of Python3 online submissions for Find Peak Element.
Memory Usage: 13.9 MB, less than 61.53% of Python3 online submissions for Find Peak Element.
"""


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        
        # if len of 2, return max num index in arr
        if len(nums) == 2:
            return nums.index(max(nums))
        

        done = False
        left, mid, right = 0, len(nums)//2 , len(nums) - 1
        peak = None
        while not done:

            # if right == mid , that is the peak value
            if right == mid:
                peak = mid
                done = True
                continue
            # left is peak if l > r 
            if left > right:
                peak = left
                done = True
                continue
            
            # compare mid with adjacent mid + 1, if (m < m+1), left = m+1   else: right is mid
            if mid + 1 < len(nums):
                if nums[mid] <= nums[mid+1]:
                    left = mid+1
                else:
                    right = mid
            mid = (left + right) // 2 # calculate new midpointer
        return peak