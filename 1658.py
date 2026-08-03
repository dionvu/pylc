from typing import List

def minOperations(nums: List[int], x: int) -> int:
    outside = sum(nums)
    res = -1
    l = 0

    for r in range(len(nums)):
        outside -= nums[r]

        while l <= r and outside < x:
            outside += nums[l]
            l += 1

        if outside == x:
            res = max(r - l + 1, res) 

    return len(nums) - res if res != -1 else -1
