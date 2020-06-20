"""
Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.
Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).
You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n). There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.

Algorithm (similar to gas station problem):
1) Candidate starts at zero. Iterate through each person.
2) If candidate knows the person, then the person must be the potential candidate since a celeb should not know anyone but themselves
3) Iterate through again and make sure no one knows the candidate, else no one is the celeb

Result:
Runtime: 1816 ms, faster than 54.90% of Python3 online submissions for Find the Celebrity.
Memory Usage: 14.1 MB, less than 6.55% of Python3 online submissions for Find the Celebrity.
"""

# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        
        if n == 0:
            return -1
        elif n == 1:
            return 1
        
        candidate = 0
        
        # loop thru each and choose candidate
        for person in range(n):
            if knows(candidate,person):
                candidate = person

        # verify no one knows the candidate
        for otherPerson in range(n):
            if candidate != otherPerson:
                if knows(candidate,otherPerson) or not knows(otherPerson, candidate):
                    return -1
            
        return candidate
