"""
There are a total of n courses you have to take, labeled from 0 to n-1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.
There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Algorithm:
1) use topological sorting - for a given node explore all child nodes and until one is leaf node, then add it to stack
2) return stack

Result:
Runtime: 592 ms, faster than 5.01% of Python3 online submissions for Course Schedule II.
Memory Usage: 17.1 MB, less than 13.45% of Python3 online submissions for Course Schedule II.
"""

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 0:
            return []
        if len(prerequisites) == 0:
            return [x for x in range(numCourses)]
        
        # add edges to dict
        edges = {}
        for prereq in prerequisites:
            if prereq[0] not in edges:
                edges[prereq[0]] = [prereq[1]]
            else:
                edges[prereq[0]].append(prereq[1])
        
        visited = []
        stack = []
        cycle = False
        
        def dfs(course, visited, stack):
            nonlocal cycle
            if cycle:   # if it has cycle no need to explorer further
                return
            if course in visited and course not in stack:   # is cycle if already visited node that is not in stack (revisited)
                cycle = True
            
            if course in visited:      # means it has already been explorered so go back
                return
            
            visited.append(course)  # Add to visit arr
            if course not in edges:
                stack.append(course)
                return
            
            for preCourse in edges[course]:
                dfs(preCourse,visited,stack)
            
            stack.append(course)
            
        for course in range(numCourses):
            if cycle:
                break
            dfs(course,visited,stack)
        
        if cycle:
            return []
        return stack