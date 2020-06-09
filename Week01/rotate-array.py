def rotate(self, nums: List[int], k: int) -> None:
    if not nums and k <= 0:
        return

    n = len(nums)
    k = k % n

    def swap(lidx, ridx):
        while lidx < ridx:
            nums[lidx], nums[ridx] = nums[ridx], nums[lidx]
            lidx = lidx + 1
            ridx = ridx - 1 

    swap(0, n - k - 1)
    swap(n - k, n - 1)
    swap(0, n - 1)