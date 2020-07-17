"""
Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

Example:
Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]

Algorithm:
1) Append to front and back (lower-1) & upper+1
2) Iterate and compare differences

Result:
Runtime: 32 ms, faster than 54.12% of Python3 online submissions for Missing Ranges.
Memory Usage: 13.9 MB, less than 42.11% of Python3 online submissions for Missing Ranges.
"""

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        
        nums.insert(0,lower-1)
        nums.append(upper+1)
        
        missingRangeArr = []
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 1:
                continue
            elif nums[i+1] - nums[i] > 1:
                if nums[i+1] - nums[i] == 2:
                    missingRangeArr.append(str(nums[i]+1))
                else:
                    missingRangeArr.append(str(nums[i]+1)+"->"+str(nums[i+1]-1))
        return missingRangeArr