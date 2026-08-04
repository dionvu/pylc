from typing import Counter

def balancedString(s: str) -> int:
    freq = Counter(s)
    k = len(s) // 4
    over = sum(v - k for v in freq.values() if v > k)
    res = len(s)
    l = 0

    if not over: return 0

    for r in range(len(s)):
        c = s[r]
        over -= freq[c] > k
        freq[c] -= 1

        while over == 0:
            res = min(r - l + 1, res)
            cl = s[l]

            freq[cl] += 1
            over += freq[cl] > k
            l += 1

    return res
