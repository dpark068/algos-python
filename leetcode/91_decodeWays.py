"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:
'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Result:
Runtime: 32 ms, faster than 75.64% of Python3 online submissions for Decode Ways.
Memory Usage: 14 MB, less than 38.58% of Python3 online submissions for Decode Ways.
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        
        dp = [0 for _ in range(len(s)+1)]
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1
        
        for pos in range(2,len(s)+1):
            singleDigit = int(s[pos-1])
            doubleDigit = int(s[pos-2:pos])

            if singleDigit >= 1:
                dp[pos] += dp[pos-1]
            
            if doubleDigit >= 10 and doubleDigit <= 26:
                dp[pos] += dp[pos-2]
        
        return dp[-1]
            
        