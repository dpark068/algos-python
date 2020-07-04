"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:
Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.

Algorithm:
1) Keep ading operands to stack until a operator exists
2) secondNum is first popped and firstNum is the next popped
3) Compute using operator and return back into stack
4) At end, should have one num, return that num

Result:
Runtime: 84 ms, faster than 30.68% of Python3 online submissions for Evaluate Reverse Polish Notation.
Memory Usage: 14.2 MB, less than 26.76% of Python3 online submissions for Evaluate Reverse Polish Notation.
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0
        
        operands = []
        
        def isInt(ch):  # check to see if its an int
            try:
                t = int(ch)
                return True
            except ValueError:
                return False
        
        def compute(firstNum,secondNum, operator):
            if operator == "+":
                return firstNum + secondNum
            elif operator == "-":
                return firstNum - secondNum
            elif operator == "/":
                if abs(firstNum) < abs(secondNum):
                    return 0
                elif ((firstNum < 0 and secondNum >= 0) or (secondNum < 0 and firstNum >= 0)) and firstNum % secondNum != 0 :   
                    # for cases where its a negative quotient and there is a remainder - we want to truncate to zero (python specific will to lower num not zero)
                    return (firstNum // secondNum) + 1
                return firstNum // secondNum
            elif operator == "*":
                return firstNum * secondNum
        
        
        for char in tokens:
            if isInt(char):
                operands.append(int(char))
                continue
            else:   #it is operator
                secondNum = operands.pop()
                firstNum = operands.pop()
                operands.append(compute(firstNum,secondNum,char))
        
        return operands.pop()