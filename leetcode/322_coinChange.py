"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that 
you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Algorithm:
1) sort coins in descending order ( will prioritize large coins in search)
2) DFS algorithm to determine what num of coins will be for given choice
3) Use memoization to cache for a given amount what the numofcoins needed was to avoid recalculating

Result:
Runtime: 1744 ms, faster than 35.73% of Python3 online submissions for Coin Change.
Memory Usage: 39.9 MB, less than 5.64% of Python3 online submissions for Coin Change.
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        if amount == 0:
            return 0
        
        dp = {}
        coins.sort(reverse=True)
        
        def dfs(amount, coins): # return coins
            nonlocal dp
            if amount in dp:        # memoize
                return dp[amount]
            if amount in coins:
                return 1
            elif amount < coins[-1]: # smallest coin
                return -1
            
            numOfCoins = []
            for coin in coins: # loop through each decision we make to choose a coin (descending order)               
                tempNumCoins = dfs(amount-coin,coins)
                if tempNumCoins != -1:
                    numOfCoins.append(tempNumCoins)
            
            if len(numOfCoins) == 0:    # if there is no decision to make for amount return -1
                dp[amount] = -1
                return -1
            
            dp[amount] = 1 + min(numOfCoins)    # cache value for amount
            return 1 + min(numOfCoins)  # return value
            
        
        totalCoins = dfs(amount, coins)
        return totalCoins