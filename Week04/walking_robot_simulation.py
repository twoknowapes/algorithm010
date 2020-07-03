from typing import List


def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    # 判断下一步是否是障碍点
    obstance_set = set(map(tuple, obstacles))
    x = y = di = ans = 0
    for cmd in commands:
        if cmd == -2:
            di = (di - 1) % 4
        elif cmd == -1:
            di = (di + 1) % 4
        else:
            for k in range(cmd):
                if (x + dx[di], y + dy[di]) not in obstance_set:
                    x += dx[di]
                    y += dy[di]
                    ans = max(ans, x * x + y * y)
    return ans
