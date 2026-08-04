from typing import List

def trap(height: List[int]) -> int:
    n = len(height)
    max_h_l = [0] * n
    max_h_r = [0] * n

    l_max, r_max = 0, 0
    for l in range(n):
        r = -l - 1
        max_h_l[l] = l_max
        max_h_r[r] = r_max
        l_max = max(height[l], l_max)
        r_max = max(height[r], r_max)


    total = 0
    for i, h in enumerate(height):
        pot = min(max_h_l[i], max_h_r[i])
        total += max(pot - h, 0)

    return total
