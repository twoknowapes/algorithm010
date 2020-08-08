def strStr(self, haystack: str, needle: str) -> int:
    d = 256
    q = 9997
    n = len(haystack)
    m = len(needle)
    h = pow(d, m - 1) % q
    p = 0
    t = 0
    if m > n:
        return -1
    # preprocessing
    for i in range(m):
        p = (d * p + ord(needle[i])) % q
        t = (d * t + ord(haystack[i])) % q
    # note the +1
    for s in range(n - m + 1):
        # check character by character
        if p == t:
            match = True
            for i in range(m):
                if needle[i] != haystack[s + i]:
                    match = False
                    break
            if match:
                return s
        if s < n - m:
            t = (t - h * ord(haystack[s])) % q
            t = (t * d + ord(haystack[s + m])) % q
            t = (t + q) % q
    return -1
