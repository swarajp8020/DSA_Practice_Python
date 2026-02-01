class Solution:
    def maxProfit(self, prices):
        min_prices = float('inf')
        max_profit = 0
        for p in prices:
            min_prices = min(min_prices, p)
            max_profit = max(max_profit, p - min_prices)
        return max_profit
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([7,1,5,3,6,4]))
