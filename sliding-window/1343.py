from typing import List

def numOfSubarrays(arr: List[int], k: int, threshold: int) -> int:
    min_sum = threshold * k 
    sum = 0
    res = 0

    for i, n in enumerate(arr):
        sum += n

        if i >= k:
            sum -= arr[i - k]

        if i >= k - 1 and sum >= min_sum:
            res += 1

    return res
