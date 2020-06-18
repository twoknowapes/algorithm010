def removeDuplicates(self, nums: list[int]) -> int:
    if not nums: return 0

    idx, temp = 0, 1
    while idx < len(nums) -1:
        if nums[idx] == nums[temp]:
            nums.pop(idx)
        else:
            idx, temp = idx + 1, temp + 1
        return len(nums)
