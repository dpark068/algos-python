"""
Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

Algorithm:
1) Iterate through string
2) if char is num - append to num string (could be more than one digit)
3) if char is letter - append to res string
4) if char is [ - append num and letter strings to num stack and letter stack ++ reset num and letter string to ""
5) if char is ] - pop num and letter strings (this will be the previous string) + multiply existing string by num and append popped letter string to front

Result:
Runtime: 32 ms, faster than 59.45% of Python3 online submissions for Decode String.
Memory Usage: 14 MB, less than 9.86% of Python3 online submissions for Decode String.
"""

class Solution:
    def decodeString(self, s: str) -> str:
        if not s:
            return ""
        
        numStack = []
        sStack = []
        
        res = ""
        num = ""
        
        def isInt(char):    # check if int
            try:
                int(char)
                return True
            except ValueError:
                return False
        
        for char in s:  # iterate through s
            
            if isInt(char):
                num = num + char
            elif char == "[":
                sStack.append(res)
                numStack.append(int(num))
                
                res = ""
                num = ""
            elif char == "]":
                multiplier = numStack.pop()
                preString = sStack.pop()
                
                res = res * multiplier
                res = preString + res
            else:
                res = res + char
        
        return res
            