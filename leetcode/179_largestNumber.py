"""
Given a list of non negative integers, arrange them such that they form the largest number.

Algorithm:
1) Selection sort to compare vals

Result:
Runtime: 244 ms, faster than 5.25% of Python3 online submissions for Largest Number.
Memory Usage: 13.8 MB, less than 63.92% of Python3 online submissions for Largest Number.
"""

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        if len(nums) == 0:
            return ""
        elif len(nums) == 1:
            return str(nums[0])
        
        
        # selection sort
        finalNum = ""
        
        for startPos in range(len(nums)-1,-1,-1):
            for pos in range(1,startPos+1):
                numPos = str(nums[pos])
                preNumPos = str(nums[pos-1])
                numPre = int(numPos + preNumPos)
                preNum = int(preNumPos + numPos)
                if preNum > numPre:
                    nums[pos-1],nums[pos] = nums[pos], nums[pos-1]
        
        if nums[-1] == 0:
            return '0'
        return ''.join(str(x) for x in nums[::-1])