"""
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:
Input: 2.00000, 10
Output: 1024.00000

Algorithm:
1) keep multiplying value tempval by 2 until n is less than current n
2) subtract that n and repeat until n == 0

Result:
Runtime: 36 ms, faster than 27.88% of Python3 online submissions for Pow(x, n).
Memory Usage: 13.9 MB, less than 35.56% of Python3 online submissions for Pow(x, n).
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif x == 1 or x == 0:
            return x
        
        negativeSign = False
        if n < 0:
            negativeSign = True
        n = abs(n)
        finalVal = 1
        while n > 1:
            tempN = 1   # keep track of current N
            done = False    # break inner while loop if finding N
            tempVal = x
            while not done:
                if tempN * 2 > n:
                    done = True
                    break
                elif tempN * 2 <= n:
                    tempN *= 2
                    tempVal *= tempVal
            
            n -= tempN
            if negativeSign:
                finalVal *= (1/tempVal)
            else:
                finalVal *= tempVal
        
        if n == 1:
            if negativeSign:
                finalVal *= (1/x)
            else:
                finalVal *= x
        return finalVal