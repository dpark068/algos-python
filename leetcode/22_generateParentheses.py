"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Result:
Runtime: 32 ms, faster than 79.39% of Python3 online submissions for Generate Parentheses.
Memory Usage: 14.2 MB, less than 18.43% of Python3 online submissions for Generate Parentheses.
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        elif n == 1:
            return ["()"]
        
        
        #make parenthesis
        def parenthesis(currP, result):
            currOpen = currP.count("(")
            currClose = currP.count(")")
            # base case
            if currOpen == n and currClose == n:
                result.append(currP)
                return
            
            # recurse with open and closing brackets w conditions
            if currOpen < n:  # if num of opening bracket is less than n, add opening bracket
                parenthesis(currP + "(",result)
            
            if currClose < currOpen:  # we can close bracket as long as the number of closing bracket is less than opening bracket
                parenthesis(currP + ")",result)
            return result
        
        result = parenthesis("",[])
        return result