"""
Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:
Input: s = "aaabb", k = 3
Output: 3
The longest substring is "aaa", as 'a' is repeated 3 times.

Result:
TLE
"""

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0
        
        if len(s) < k:
            return 0
        
        kRepeating = {}
        
        for string in s:
            if string not in kRepeating:
                kRepeating[string] = 1
            else:
                kRepeating[string] += 1
        
        kRepeatingSet = {}
        #remove from krepeating the char not greater
        for i, v in kRepeating.items():
            if v >= k:
                kRepeatingSet[i] = v
                
        #print(kRepeatingSet)
        def validSubstring(sub):
            charSet = set(sub)
            #print(charSet)
            for ch in charSet:
                if ch not in kRepeatingSet or sub.count(ch) < k:
                    return False
            return True
        
        globalSub = ""
        # iterate through each string as starting
        for startStr in range(len(s)):
            largestSub = ""
            for endStr in range(len(s),startStr-1,-1):
                #print(s[startStr:endStr])
                if validSubstring(s[startStr:endStr]):
                    largestSub = s[startStr:endStr]
                    break
            #print(largestSub)
            if len(largestSub) > len(globalSub):
                globalSub = largestSub
        
        #print("globalSub: " + globalSub)
        return len(globalSub)