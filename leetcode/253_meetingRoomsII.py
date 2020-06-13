"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
Example 1:  Input: [[0, 30],[5, 10],[15, 20]]    Output: 2

Result:
Runtime: 76 ms, faster than 86.96% of Python3 online submissions for Meeting Rooms II.
Memory Usage: 17.1 MB, less than 33.22% of Python3 online submissions for Meeting Rooms II.
"""

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        elif len(intervals) == 1:
            return 1
        
        #sort arr by start time   O(n log n)
        intervals.sort(key=itemgetter(0))
        
        heap = []
        numOfRooms = 0
        
        # loop through intervals O(n)
        for interval in intervals:
            if len(heap) == 0: # if heap is empty add ending time of interval
                numOfRooms += 1
                heapq.heappush(heap,interval[1])   # O(log n)
            else:
                if heap[0] <= interval[0]:      # if start time of interval is greater or equal to min end time in heap, pop smallest from heap and add interval end time
                    heapq.heappushpop(heap,interval[1])
                else:   # if times are coinciding, requires another room
                    numOfRooms += 1
                    heapq.heappush(heap,interval[1])
        
        return numOfRooms