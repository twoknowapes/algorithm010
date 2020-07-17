from typing import List


def minimumTotal(self, triangle: List[List[int]]) -> int:
    if not triangle:
        return 0

    dp = [0] * (len(triangle) + 1)

    for row in triangle[::-1]:
        for i in range(len(row)):
            dp[i] = min(dp[i], dp[i - 1]) + row[i]

    return dp[0]
