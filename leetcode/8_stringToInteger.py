"""
Implement atoi which converts a string to an integer.
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
If no valid conversion could be performed, a zero value is returned.

Note:
Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.

Result:
Runtime: 40 ms, faster than 31.31% of Python3 online submissions for String to Integer (atoi).
Memory Usage: 13.6 MB, less than 98.61% of Python3 online submissions for String to Integer (atoi).
"""

class Solution:
    def myAtoi(self, str: str) -> int:
        
        if not str:
            return 0
        
        sign = False
        readSign = False
        finalNum = ""
        useSign = True
        
        def isInt(sNum):
            try:
                s = int(sNum)
                return True
            except ValueError:
                return False
        
        if len(str) == 1:
            if isInt(str):
                return int(str)
            else:
                return 0
        
        for s in str:
            if finalNum == "" and readSign and not isInt(s):
                return 0
            if finalNum == "" and s == " ":
                continue
            
            
            
            if finalNum == "" and s == "-":  # check for sign
                if readSign:
                    return 0
                sign = True
                readSign = True
                continue
            if finalNum == "" and s == "+":
                if readSign:
                    return 0
                readSign = True
                continue
            if finalNum == "" and readSign and s in "+-":
                return 0
            if finalNum == "" and s not in "+-":
                if not isInt(s):    #if first val is not a integer return 0
                    return 0
                else:
                    finalNum = s
                    continue
            
            if len(finalNum) > 0:
                if isInt(s):
                    finalNum = finalNum + s
                else:
                    break
                
        if not isInt(finalNum):
            return 0

        
        finalNum = int(finalNum)
        if sign and useSign:
            finalNum *= -1
        
        if finalNum == 2147483648:
            return 2147483647
        
        if finalNum > 2147483648:
            finalNum = 2147483647
        if finalNum < -2147483648:
            finalNum = -2147483648
        return finalNum