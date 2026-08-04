from typing import List

def longestOnes(nums: List[int], k: int) -> int:
    zeros, res, l = 0, 0, 0

    for r in range(len(nums)):
        zeros += not nums[r]

        while zeros > k:
            zeros -= not nums[l]
            l += 1

        res = max(r - l + 1, res)

    return res
