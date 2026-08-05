class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        for i in range(len(prices)):
            maxi = max(maxi, max(prices[i:]) - prices[i])

        return maxi