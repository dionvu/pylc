from typing import List

def longestSubarray(nums: List[int]) -> int:
    n = len(nums)
    zeros = 0
    res = 0
    l = 0

    for r in range(n):
        zeros += not nums[r]

        while zeros > 1:
            zeros -= not nums[l]
            l += 1

        res = max(r - l + 1, res)

    return res - zeros if res != n else n - 1
