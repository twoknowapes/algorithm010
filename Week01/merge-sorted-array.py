def mergeSorted(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    while n:
        if m == 0:
            nums1[n - 1] = nums2[n - 1]
            n = n - 1
            continue

        if nums1[m - 1] < nums2[n - 1]:
            nums1[m + n - 1] = nums2[n - 1]
            n = n - 1
        else:
            nums2[m + n - 1] = nums1[m - 1]
            m = m - 1