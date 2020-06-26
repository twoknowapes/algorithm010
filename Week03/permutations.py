def permute(self, nums: list[int]) -> list[list[int]]:
    if len(nums) <= 1:
        return [nums]

    res = []
    for idx, num in enumerate(nums):
        res_nums = nums[:idx] + nums[idx + 1:]
        for j in self.permute(res_nums):
            res.append([num] + j)
    return res