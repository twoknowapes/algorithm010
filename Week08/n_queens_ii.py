from typing import List


def totalNQueen(self, n: int) -> List[List[str]]:
    if n < 1:
        return []

    self.count = 0
    self.DFS(n, 0, 0, 0, 0)
    return self.count


def DFS(self, n, row, cols, pie, na):
    # recursion terminator
    if row >= n:
        self.count += 1
        return

    # 得到当前所有的空位
    bits = (~(cols | pie | na)) & ((1 << n) - 1)
    while bits:
        # 取到最低位的 1
        p = bits & -bits
        # 表示在 p 位置上放入皇后
        bits &= bits - 1
        self.DFS(n, row + 1, cols | p, (pie | p) << 1, (na | p) >> 1)
