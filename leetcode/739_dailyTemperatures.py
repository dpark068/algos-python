"""
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.
For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].
Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].

Algorithm:
1) Iterate backward through the tempreatures (starting from last day)
2) Keep a stack of all previous tempreatures
3) at each iteration, keep popping the stack until the tempreature in stack is greater than current temp.
4) If stack is empty - assign 0
5) if last item in stack is greater, subtract index of that item with current index item - append to result
6) append curr temp into stack
7) At end reverse the result arr (since we are analyzing backwards)

Result:
Runtime: 552 ms, faster than 45.86% of Python3 online submissions for Daily Temperatures.
Memory Usage: 17.8 MB, less than 18.47% of Python3 online submissions for Daily Temperatures.
"""

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if not T:
            return []
        
        stack = [(len(T)-1,T[-1])]
        result = [0]
        for i in range(len(T)-2,-1,-1): # iterate backwards
            while stack and stack[-1][1] <= T[i]:   # pop until last item in stack is greater than current temp
                stack.pop()
            if stack and stack[-1][1] > T[i]:   # append result
                result.append(stack[-1][0]-i)
            elif not stack: # append 0 if stack is empty
                result.append(0)
            
            stack.append((i,T[i]))
            
        return result[::-1]