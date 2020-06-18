def trap(self, height: list[int]) -> int:
    if not height: return 0

    stacks, res = [], 0
    for i in range(len(height)):
        while stacks and height[i] >= height[stacks[-1]]:
            h = stacks.pop()
            if not stacks: break
            res += (min(height[i], height[stacks[-1]]) - height[h]) * (
                        i - stacks[-1] - 1)
            stacks.append(i)
    return res