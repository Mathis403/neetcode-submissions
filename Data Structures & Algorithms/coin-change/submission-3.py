class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def minCoinrec(amount:int) -> int:
            
            if amount == 0 :
                return 0

            if amount in memo.keys():
                return memo[amount]
            
        
            

            res = 1e9

            for c in coins:
                if amount - c >= 0:
                    res = min(res, 1 + minCoinrec(amount - c))
            memo[amount] = res
            return res

        minCoins = minCoinrec(amount)
        return -1 if minCoins >= 1e9 else minCoins