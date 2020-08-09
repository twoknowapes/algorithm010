def strStr(self, haystack: str, needle: str) -> int:
    if haystack is None or len(haystack) < len(needle):
        return -1
    if needle is None:
        return 0

    i, j, partial_match_table = 0, 0, self.partial_match_table(needle)
    while i < len(haystack) and j < len(needle):
        if haystack[i] == needle[j] or j == -1:
            i += 1
            j += 1
        else:
            j = partial_match_table[j]
    if j == len(needle):
        return i - len(needle)
    else:
        return -1


def partial_match_table(self, p: str):
    k, i, partial_match_table = -1, 0, [-1] * len(p)
    while i < len(p) - 1:
        if k == -1 or p[i] == p[k]:
            k += 1
            i += 1
            if p[i] == p[k]:
                partial_match_table[i] = partial_match_table[k]
            else:
                partial_match_table[i] = k
        else:
            k = partial_match_table[k]
    return partial_match_table
