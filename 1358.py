from typing import Counter

def numberOfSubstrings(s: str) -> int:
    count = Counter()
    res = 0
    l = 0

    for r in range(len(s)):
        count[s[r]] += 1

        while (len(count) == 3):
            res += len(s) - r

            lc = s[l]
            count[lc] -= 1
            if not count[lc]: del count[lc]
            l += 1

    return res
