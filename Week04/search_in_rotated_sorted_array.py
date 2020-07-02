def search_two_points(self, nums: list[int], target: int) -> int:
    if not nums: return -1

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < nums[right]:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
    return left if nums[left] == target else -1


def search_xor(self, nums: list[int], target: int) -> int:
    if not nums: return -1

    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if (nums[0] > target) ^ (nums[0] > nums[mid]) ^ (target > nums[mid]):
            left = mid + 1
        else:
            right = mid - 1
    return left if target in nums[left:left + 1] else -1
