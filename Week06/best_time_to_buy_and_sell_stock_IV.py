from typing import List


def maxProfit(self, K: int, prices: List[int]) -> int:
    if len(prices) <= 1:
        return 0

    if K >= len(prices) // 2:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit

    dp = [[[None, None] for _ in range(K + 1)] for _ in range(len(prices))]
    for i in range(len(prices)):
        dp[i][0][0] = 0
        dp[i][0][1] = -float('inf')
    for k in range(1, K + 1):
        dp[0][0][k] = 0
        dp[0][1][k] = -prices[0]
    for i in range(1, len(prices)):
        for k in range(1, K + 1):
            dp[i][0][k] = max(dp[i - 1][0][k], dp[i - 1][1][k] + prices[i])
            dp[i][1][k] = max(dp[i - 1][1][k], dp[i - 1][0][k - 1] - prices[i])
        return dp[len(prices) - 1][k][0]
