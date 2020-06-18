def twoSum(self, nums: list[int], target: int) -> list[int]:
    temp = {}
    for idx in range(len(nums)):
        if (target - nums[idx]) in temp:
            return [idx, temp[target - nums[idx]]]
        else:
            temp[nums[idx]] = idx


def twoSumByHash(self, nums: list[int], target: int) -> list[int]:
    d = {}
    for idx, num in enumerate(nums):
        if d.get(num) == None:
            d[target - num] = idx
        else:
            return [d.get(num), idx]
