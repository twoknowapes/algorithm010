def twoSum(self, nums: List[int], target: int) -> List[int]:
    temp = {}
    for idx in range(len(nums)):
        if (target - nums[idx]) in temp:
            return [idx, temp[target - nums[idx]]]
        else:
            temp[nums[idx]] = idx
