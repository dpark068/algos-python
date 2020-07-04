"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].

Algorithm:
1) binary search
2) if target == midpoint, expand left and right pointers to find range of nums
3) if target < midpoint val, go left for smaller vals
4) if target > midpoint val, go right to see larger values


Result:
Runtime: 92 ms, faster than 46.46% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
Memory Usage: 14.9 MB, less than 97.64% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        
        if len(nums) == 1:  # handle single num use case
            if nums[0] == target:
                return [0,0]
            else:
                return [-1,-1]
        
        if target > nums[-1]:   # if target is greater than entire list
            return [-1,-1]
        
        done = False
        leftIndex = rightIndex = -1
        left = 0
        right = len(nums)-1
        
        
        while left < right: #Binary search
            midPoint = (right+left) // 2
            
            if nums[midPoint] == target:    
                leftIndex = rightIndex = midPoint
                tempLeftMid = tempRightMid = midPoint
                
                while leftIndex > left and nums[tempLeftMid-1] == target:
                    leftIndex -= 1
                    tempLeftMid -= 1                   
                while rightIndex < right and nums[tempRightMid+1] == target:
                    rightIndex += 1
                    tempRightMid += 1
                return [leftIndex,rightIndex]
            elif nums[midPoint] < target:   # go right if num is less than target
                left = midPoint + 1
            elif nums[midPoint] > target:    # go left if num is greater than target
                right = midPoint - 1
        
        # handle case where left == right and target is at that value
        if left >= 0 and left < len(nums) and nums[left] == target:
            return [left,left]
        elif right >= 0 and right < len(nums) and nums[right] == target:
            return [right,right]
        return [leftIndex,rightIndex]