"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
The order of output does not matter.

Algorithm:
1) Create desired Dict with all values we want
2) Create dict with count of values that are relevant
3) When iterating through string s, remove the character that exceeds length of p from end
4) If match, than add index and continue

Result:
Runtime: 272 ms, faster than 27.96% of Python3 online submissions for Find All Anagrams in a String.
Memory Usage: 14.6 MB, less than 98.40% of Python3 online submissions for Find All Anagrams in a String.
"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not s or not p:
            return []
        
        allAnagrams = []
        currAnagram = {}
        desiredAnagram = {}
        
        for i in range(len(p)): # create desired anagram counts
            if p[i] not in desiredAnagram:
                desiredAnagram[p[i]] = 1
                currAnagram[p[i]] = 0
            else:
                desiredAnagram[p[i]] += 1
        
        for i in range(len(s)): # iterate through s and keep track of characters at certain array
            
            if s[i] not in desiredAnagram:
                if i >= len(p) and s[i-len(p)] in desiredAnagram:
                    currAnagram[s[i-len(p)]] -= 1
                    continue
            
            if i >= len(p) and s[i-len(p)] in desiredAnagram:
                currAnagram[s[i-len(p)]] -= 1
            
            if s[i] in desiredAnagram:
                currAnagram[s[i]] += 1
            
            validAnagram = True
            for index, value in currAnagram.items():
                if currAnagram[index] != desiredAnagram[index]:
                    validAnagram = False
                    break
            
            if validAnagram:
                allAnagrams.append(i-len(p)+1)
        
        return allAnagrams
            