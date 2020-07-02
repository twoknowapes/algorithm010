def findContentChildren(self, g: list[int], s: list[int]) -> int:
    if not g or not s: return 0

    g.sort()
    s.sort()
    child = cookie = 0
    while child < len(g) and cookie < len(s):
        if g[child] <= s[cookie]:
            child += 1
        cookie += 1
    return child
