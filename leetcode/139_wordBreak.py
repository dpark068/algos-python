"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:
The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Algorithm:
1) Loop through different lengths of substrings (1-> len of string)
2) in loop, iterate through the different start values, i.e. leetcode and subset == 2: le, ee, et, tc, co, ....
3) if substring is not in word dict, add dividers in between each char and see if they exist as sub sub strings
4) if they exist, set it to True on DP table
5) Set as False if neither criteria matches
6) return top right most value in DP table dp[0][len(s)-1]

Result:
Runtime: 316 ms, faster than 5.18% of Python3 online submissions for Word Break.
Memory Usage: 13.8 MB, less than 89.93% of Python3 online submissions for Word Break.
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return False
        
        dp = [[None] * len(s) for _ in range(len(s))]
        
        for subset in range(1,len(s)+1): #length of substring
            for col in range(len(s)): # loop through each substring with this length in the original string
                endCol = col + subset  #start == col, end == endCol
                
                if endCol > len(s):
                    break

                if s[col:endCol] in wordDict: # if word in dict, set it as True
                    dp[col][endCol-1] = True
                    continue
                    
                
                for divider in range(1,len(s[col:endCol])):
                    #s[col:divider] check with dp[col][divider-1] and s[divider:endCol] checks with dp[divider][endCol-1]:
                    if dp[col][divider-1] and dp[divider][endCol-1]:
                        dp[col][endCol-1] = True
                        break
                if dp[col][endCol-1] is None:
                    dp[col][endCol-1] = False
        return dp[0][-1]
