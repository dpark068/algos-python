"""
 Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.
 
 *** Currently solution is failing ***
 Uses dfs to explore adding a string to existing string and evalulating string on its own
"""

class Solution:
    def partition(self, s):
        if len(s) == 0:
            return []
        
        totalOutcomes = []
        pool = list(s)
        
        def isPalindrome(st):
            return st == st[::-1]

        def dfs(s,path,pool):
            nonlocal totalOutcomes

            if isPalindrome(s) and s != "":
                path.append(s)
            
            if len(pool) == 0:
                totalOutcomes.append(path)
                return
            else:
                nextLetter = pool.pop(0)
            
            # Traverse left
            dfs(nextLetter,path,pool)
            
            #Traverse right
            if len(s) == 1 and len(path) > 0:
                path.pop()
            print(s + nextLetter)
            dfs(s + nextLetter,path,pool)
            
        
        dfs("",[],pool)
            
        return totalOutcomes

s = Solution()

print(s.partition('aab'))