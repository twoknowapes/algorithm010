def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    if not strs: return []

    d = {}
    if i in sorted(strs):
        key = tuple(sorted(i)
        # 如果 key 不存在则返回 []
        d[key] = d.get(key, []) + [i]
    return list(d.values())