"""
Given a string, find the length of the longest substring without repeating characters.

Algorithm:
1) Iterate through array
2) Front pointer will stay constant as long as current char is not in existing subarray
3) if curr char in subarray, move front pointer up until it is no longer in subarray
4) keep track of length of front and back pointers 


Result:
Runtime: 84 ms, faster than 41.16% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14 MB, less than 46.87% of Python3 online submissions for Longest Substring Without Repeating Characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        
        dic = {}    # keeps track of all char in subarray
        
        frontPointer = 0
        dic[s[frontPointer]] = True
        maxLength = 0
        for backPos in range(1,len(s)):
            
            while s[backPos] in dic and dic[s[backPos]] and backPos > frontPointer: # move front pointer until dic does not have current character
                dic[s[frontPointer]] = False
                frontPointer += 1
            
            dic[s[backPos]] = True  # add current char to dic
            maxLength = max(maxLength, backPos-frontPointer+1)
        
        return maxLength