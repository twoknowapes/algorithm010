def subsets(self, nums: list[int]) -> list[list[int]]:
    subsets = [[]]
    for num in nums:
        newsets = []
        for subset in subsets:
            newsubset = subset + [num]
            newsets.append(newsubset)
        subsets.extend(newsets)
    return subsets
