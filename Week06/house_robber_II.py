from typing import List


def rob(self, nums: List[int]) -> int:
    if not nums:
        return 0

    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])
    if len(nums) == 3:
        return max(nums[0], nums[1], nums[2])

    return max(self._rob(nums[0:len(nums) - 1]), self._rob(nums[1:]))


def _rob(self, nums: List[int]) -> int:
    if not nums: return 0

    dp = [0 for _ in range(len(nums))]

    if len(dp) >= 1:
        dp[0] = nums[0]
    if len(dp) >= 2:
        dp[1] = max(nums[1], dp[0])

    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

    return dp[-1]