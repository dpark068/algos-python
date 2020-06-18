"""
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.
Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.
Note:

If there exists a solution, it is guaranteed to be unique.
Both input arrays are non-empty and have the same length.
Each element in the input arrays is a non-negative integer.

Result:
Runtime: 56 ms, faster than 60.84% of Python3 online submissions for Gas Station.
Memory Usage: 14.7 MB, less than 84.25% of Python3 online submissions for Gas Station.
"""


class SolutionOne:  # Brute force solution try all combinations   - O(n^2)
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if len(gas) == 0:
            return -1
        elif len(gas) == 1:
            if gas[0] >= cost[0]:
                return 0
            else:
                return -1
        
        # try all possible routes
        for i in range(len(gas)):
            tank = 0
            outOfGas = False
            gasRoute = gas[i:len(gas)+1] + gas[:i]  # starting point gas route
            costRoute = cost[i:len(cost)+1] + cost[:i]
            
            # start moving from station to station
            for j in range(len(gasRoute)):
                tank += gasRoute[j]
                tank -= costRoute[j]
                if tank < 0:
                    outOfGas = True
                    break
            
            if not outOfGas:
                return i
        
        return -1


# track total sum - O(n)
class SolutionTwo:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if len(gas) == 0:
            return -1
        
        if len(gas) == 1:
            return 0 if gas[0]-cost[0] >= 0 else -1
        
        # track total sum and temp sum
        total_sum, sub_sum = 0, 0
        candidate = 0
        for i in range(len(gas)):
            total_sum += gas[i] - cost[i]
            sub_sum += gas[i] - cost[i]
            
            # if sub is < 0 , you know candidate is next gas station, reset sub_sum
            if sub_sum < 0:
                if i < len(gas) - 1:
                    candidate = i+1
                    sub_sum = 0
                else:
                    return -1
            
        return candidate if total_sum >= 0 else -1