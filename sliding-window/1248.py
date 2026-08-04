from typing import List

def numberOfSubarrays(nums: List[int], k: int) -> int:
    odds = 0
    res = 0
    l = 0

    for r in range(len(nums)):
        odds += nums[r] % 2

        while odds > k:
            odds -= nums[l] % 2
            l += 1

        if odds == k:
            i = l

            while i < r and nums[i] % 2 == 0:
                i += 1

            res += i - l + 1


    return res
