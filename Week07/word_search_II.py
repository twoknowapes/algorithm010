import collections
from typing import List

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
END_OF_WORD = '#'


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0]: return []
        if not words: return []

        self.res = set()

        # 构建 Trie
        root = collections.defaultdict()
        for word in words:
            node = root
            for char in word:
                node = node.setdefault(char, collections.defaultdict())
            node[END_OF_WORD] = END_OF_WORD

        self.m, self.n = len(board), len(board[0])
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] in root:
                    self._dfs(board, i, j, '', root)
        return list(self.res)

    def _dfs(self, board, i, j, cur_word, cur_dict):
        cur_word += board[i][j]
        cur_dict = cur_dict[board[i][j]]
        if END_OF_WORD in cur_dict:
            self.res.add(cur_word)
        tmp, board[i][j] = board[i][j], '@'
        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            if 0 <= x < self.m \
                    and 0 <= y < self.n \
                    and board[x][y] != '@' \
                    and board[x][y] in cur_dict:
                self._dfs(board, x, y, cur_word, cur_dict)
        board[i][j] = tmp


def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    # 构建 Trie
    trie = {}
    for word in words:
        node = trie
        for char in word:
            node = node.setdefault(char, {})
        node['#'] = True

    def search(i, j, node, pre, visited):
        if '#' in node:
            res.add(pre)
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            _i, _j = i + di, j + dj
            if -1 < _i < h \
                    and -1 < _j < w \
                    and board[_i][_j] in node \
                    and (_i, _j) not in visited:
                search(_i, _j,
                       node[board[_i][_j]],
                       pre + board[_i][_j],
                       visited | {(_i, _j)})

    res, h, w = set(), len(board), len(board[0])
    for i in range(h):
        for j in range(w):
            if board[i][j] in trie:
                search(i, j,
                       trie[board[i][j]],
                       board[i][j],
                       {(i, j)})
    return list(res)
