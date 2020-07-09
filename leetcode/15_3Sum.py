"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Note:
The solution set must not contain duplicate triplets.

Algorithm:
1) Sort array and iterate through array once
2) At each interation, have two pointers left and right, if val of left+right > currVal, move right pointer to left, else move left pointer to right
3) Difficulty is duplicates, keep iterating until value is different than curent one

Result:
Runtime: 1556 ms, faster than 25.94% of Python3 online submissions for 3Sum.
Memory Usage: 17.3 MB, less than 42.42% of Python3 online submissions for 3Sum.
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3:
            return []
        
        nums.sort() # must sort array first!
        threeSum = []
        
        for anchor in range(len(nums)-2):   # iterate through array
            if anchor >= 1 and nums[anchor] == nums[anchor-1]:
                continue
            first = anchor+1
            last = len(nums) - 1
            targetVal = nums[anchor] * -1   # want a + b == targetVal
            while first < last: # two pointers and compare left and right
                tempVal = nums[first] + nums[last]
                
                if tempVal == targetVal:    # append if values are equal
                    threeSum.append([nums[anchor],nums[first],nums[last]])
                    
                    firstVal = nums[first]
                    first += 1
                    while first < last and nums[first] == firstVal:
                        first += 1

                    secondVal = nums[last]
                    last -= 1
                    while last > first and nums[last] == secondVal:
                        last -= 1
                elif tempVal < targetVal:
                    firstVal = nums[first]
                    first += 1
                    while first < last and nums[first] == firstVal:
                        first += 1
                elif tempVal > targetVal:
                    secondVal = nums[last]
                    last -= 1
                    while last > first and nums[last] == secondVal:
                        last -= 1
            
        return threeSum