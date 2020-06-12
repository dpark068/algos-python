"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Result:
Runtime: 28 ms, faster than 75.93% of Python3 online submissions for Letter Combinations of a Phone Number.
Memory Usage: 13.8 MB, less than 73.43% of Python3 online submissions for Letter Combinations of a Phone Number.
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        # mapping of num to letters
        letterMap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        # create array of input str
        digitStack = list(digits)

        #reverse the array so we can pop from end with first value
        digitStack = digitStack[::-1]
        result = []

        #use stacks to figure out how to iterate
        while len(digitStack) != 0:
            digit = digitStack.pop()
            tempChars = letterMap[digit]
            
            # first character just add each seperately
            if len(result) == 0:
                for i in range(len(tempChars)):
                    char = tempChars[i]
                    result.append(char)
            
            elif len(result) > 0: # 2nd char onwards
                tempResult = result[:]
                result = []

                #loop through each char in array and append new char
                for i in range(len(tempChars)):
                    tempArr = [x + tempChars[i] for x in tempResult]
                    result.extend(tempArr)
        return result

