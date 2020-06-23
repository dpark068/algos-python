"""
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:
Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

Algorithm:
1) Loop through each item in array
2) Will cache first and second values looping through
3) Set first item in arr as first value, if next value is less than or equal to current first value, first value will equal current value
4) If curr value is > first value, but less than or equal to existing second value, set it as second value
5) If curr value is greater than first or second, then it is a triplet increasing subsequence

why does it work? take example 5,4,2,1,3,7, we dont care about 5,4 but only care about lowest number before potential second value, 
criteria will be 2 or 1 since 5,4 are greater than 3 so it cannot be first value. Apply for second value.

Result:
Runtime: 52 ms, faster than 86.52% of Python3 online submissions for Increasing Triplet Subsequence.
Memory Usage: 14.6 MB, less than 42.03% of Python3 online submissions for Increasing Triplet Subsequence.
"""

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        first = nums[0]
        second = None
        for i in range(1,len(nums)):
            if nums[i] <= first:
                first = nums[i]
            elif nums[i] > first and second is None:
                second = nums[i]
            elif nums[i] > first and nums[i] <= second:
                second = nums[i]
            elif nums[i] > second:
                return True
        
        return False