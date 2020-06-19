"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Algorithm:
1) create visited flag table (white, gray, black)
2) add edges to dictionary (list of prereq per course)
3) Iterate through each course and dfs
4) If already visited (-1), then you know its cyclic (return False)
5) if not visited mark it gray

Result: 
Runtime: 120 ms, faster than 35.51% of Python3 online submissions for Course Schedule.
Memory Usage: 17.2 MB, less than 12.47% of Python3 online submissions for Course Schedule.
"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        visited = [0] * numCourses
        
        prereqDict = {}
        
        # add edges to dict
        for prereq in prerequisites:
            if prereq[0] not in prereqDict:
                prereqDict[prereq[0]] = [prereq[1]]
            else:
                prereqDict[prereq[0]].append(prereq[1])
        
        canFinish = True
        
        def dfs(course):
            nonlocal canFinish
            
            if not canFinish:
                return
            if visited[course] == -1:
                canFinish = False
                return
            
            visited[course] = -1
            
            #look at prereq
            if course in prereqDict:
                for pre in prereqDict[course]:
                    dfs(pre)
            
            visited[course] = 1
        
        
        for course in range(numCourses):
            if not canFinish:
                return False
            if visited[course] == 1:
                continue
            elif visited[course] == -1:
                return False
            else:
                dfs(course)
        
        return canFinish
                