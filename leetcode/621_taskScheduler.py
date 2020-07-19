"""
You are given a char array representing tasks CPU need to do. It contains capital letters A to Z where each letter represents a different task. Tasks could be done without the original order of the array. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.
However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.
You need to return the least number of units of times that the CPU will take to finish all the given tasks.

Algorithm:
1) Get frequency of each letter, store in dict
2) Iterate through dict and add to maxheap
3) while loop until heap is empty
3b) loop through n+1 times and  pop maxheap onto an temp array
3c) Iterate through temp array and subtract 1 and add back into maxHeap if value is greater than zero
4) cycles is the number of tasks run (including idle), if heap is empty - return size of the temp array, else return n+1 (n+1 to account for initial job wait)

Result:
Runtime: 588 ms, faster than 51.72% of Python3 online submissions for Task Scheduler.
Memory Usage: 14.1 MB, less than 32.77% of Python3 online submissions for Task Scheduler.
"""

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        if not tasks:
            return 0
        if len(tasks) == 1:
            return 1
        
        freqDict = {}
        for task in tasks:  # get freq of jobs
            if task in freqDict:
                freqDict[task] += 1
            else:
                freqDict[task] = 1
        
        heap = []
        for i,v in freqDict.items():    # add to max heap
            heapq.heappush(heap,(-v,v))
        
        cycles = 0
        
        while heap: # loop until heap is empty
            tempItems = []
            for i in range(n+1):    # loop n+1 times (account for when n == 0)
                if heap:    # if heap, pop heap item and add to arr
                    tempItems.append(heapq.heappop(heap))
            
            for item in tempItems:  # iterate through temp arr and subtract value and add back to heap
                newVal = item[1] - 1
                if newVal > 0:
                    heapq.heappush(heap,(-newVal,newVal))
            
            if not heap:    # if heap is empty, account for LAST CYCYLE ONLY - just add number of items
                cycles += len(tempItems)
            else:   # account for all other times
                cycles += n + 1
        return cycles