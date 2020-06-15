def twoSum(self, nums: List[int], target: int) -> List[int]:
    d = {}
    for idx, num in enumerate(nums):
        if d.get(num) == None:
            d[target - num] = idx
        else:
            return [d.get(num), idx]
