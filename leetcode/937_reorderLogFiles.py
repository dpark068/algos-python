"""
You have an array of logs.  Each log is a space delimited string of words.
For each log, the first word in each log is an alphanumeric identifier.  Then, either:
Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.
Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.
Return the final order of the logs.

Algorithm:
1) seperate letter and digit arrays
2) for letter arrays - sort by letters then by the identifier using sort function
3) append num arr to end of letter arr

Result:
Runtime: 52 ms, faster than 26.29% of Python3 online submissions for Reorder Data in Log Files.
Memory Usage: 13.7 MB, less than 94.36% of Python3 online submissions for Reorder Data in Log Files.
"""

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        if not logs or len(logs) == 1:
            return logs
        
        digitLogs = []
        letterLogs = []
        
        def isInt(char):
            try:
                int(char)
                return True
            except ValueError:
                return False
        
        for log in logs:
            nextChar = False
            for char in log:
                if char == " ":
                    nextChar = True
                elif nextChar:
                    if isInt(char):
                        digitLogs.append(log)
                    else:
                        letterLogs.append(log)
                    break
        # letterLogs.sort(key=lambda x:x.split()[0])    # we can do this also since sort is stable sort
        # letterLogs.sort(key=lambda x:x.split()[1:])
        letterLogs.sort(key=lambda x:(x.split()[1:],x.split()[0]))
        return letterLogs + digitLogs
                        
