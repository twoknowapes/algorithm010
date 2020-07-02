def mySqrt_two_points(self, x: int) -> int:
    if x < 0: return -1

    left, right = 0, x
    while left <= right:
        mid = left + (right - left) // 2
        if mid ** 2 == x:
            return mid
        elif mid ** 2 < x:
            left = mid + 1
        else:
            right = mid - 1
    return right


def mySqrt_newton(self, x: int) -> int:
    r = x
    while r * r > x:
        r = (r + x / r) / 2
    return r
