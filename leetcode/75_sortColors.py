"""
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
Note: You are not suppose to use the library's sort function for this problem.

Example:
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Result:
selectionSort (SolutionOne): 
Runtime: 40 ms, faster than 20.06% of Python3 online submissions for Sort Colors.
Memory Usage: 14 MB, less than 6.25% of Python3 online submissions for Sort Colors.

DutchFlagAlgo (SolutionTwo):
Runtime: 28 ms, faster than 92.46% of Python3 online submissions for Sort Colors.
Memory Usage: 13.9 MB, less than 38.23% of Python3 online submissions for Sort Colors.
"""

class SolutionOne:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        
        curr = 1
        
        while curr < len(nums):
            stop = False
            temp = curr
            while stop != True and temp > 0:
                if nums[temp] < nums[temp-1]:
                    #swap
                    nums[temp], nums[temp-1] = nums[temp-1], nums[temp]
                    temp -= 1
                else:
                    stop = True
            
            curr += 1

class SolutionTwo:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if len(nums) <= 1:
            return nums
        
        p0 = curr = 0
        p2 = len(nums) - 1
        
        while curr <= p2:
            
            #if currVal = 0, swap p0 and curr and increment both
            if nums[curr] == 0:
                nums[p0],nums[curr] = nums[curr], nums[p0]
                curr += 1
                p0 += 1
            # currVal = 1, increment curr
            elif nums[curr] == 1:
                curr += 1
            # currVal = 2, swap curr and p2 then decrement p2
            else:
                nums[p2],nums[curr] = nums[curr], nums[p2]
                p2 -= 1
            