from typing import List

def largestRectangleArea(heights: List[int]) -> int:
    n = len(heights)
    res = 0
    stack = []

    for r, h in enumerate(heights):
        start = r
        while stack and stack[-1][1] > h:
            l, height = stack.pop()
            res = max(height * (r - l), res)
            start = l

        stack.append((start, h))

    for i, h in stack:
        res = max(h * (n - i), res)

    return res
