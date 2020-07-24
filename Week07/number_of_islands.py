import collections
from typing import List


def numIslands(self, grid: List[List[str]]) -> int:
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            # 发现陆地
            if grid[row][col] == '1':
                count += 1
                # 记录该陆地已访问过
                grid[row][col] = '0'
                land_positions = collections.deque()
                land_positions.append([row, col])
                while len(land_positions) > 0:
                    x, y = land_positions.popleft()
                    # 进行四个方法扩张
                    for new_x, new_y in [[x, y + 1],
                                         [x, y - 1],
                                         [x + 1, y],
                                         [x - 1, y]]:
                        # 判断有效性
                        if 0 <= new_x < len(grid) \
                                and 0 <= new_y < len(grid[0]) \
                                and grid[new_x][new_y] == '1':
                            grid[new_x][new_y] = '0'
                            land_positions.append([new_x, new_y])
    return count
