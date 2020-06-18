def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    if not strs: return []

    d = {}
    for i in sorted(strs):
        key = tuple(sorted(i))
        # 如果 key 不存在则返回 []
        d[key] = d.get(key, []) + [i]
    return list(d.values())
