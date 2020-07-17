from typing import List


def maxSubArray(self, nums: List[int]) -> int:
    dp = nums

    for i in range(1, len(nums)):
        dp[i] = nums[i] + max(0, dp[i - 1])

    return max(dp)