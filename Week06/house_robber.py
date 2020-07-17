from typing import List


def rob(self, nums: List[int]) -> int:
    if not nums: return 0

    dp = [0 for _ in range(len(nums))]

    if len(dp) >= 1:
        dp[0] = nums[0]
    if len(dp) >= 2:
        dp[1] = max(nums[1], dp[0])

    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

    return dp[-1]