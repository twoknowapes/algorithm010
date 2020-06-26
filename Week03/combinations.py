def combine(self, n: int, k: int) -> list[list[int]]:
    if n <= 0 or k <= 0 or k > n:
        return []

    res = []
    self.__dfs(1, k, n, [], res)
    return res


def __dfs(self, start, k, n, pre, res):
    if len(pre) == k:
        res.append(pre[:])
        return

    for i in range(start, n - (k - len(pre)) + 2):
        pre.append(i)
        self.__dfs(i + 1, k, n, pre, res)
        pre.pop()