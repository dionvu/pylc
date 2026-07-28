def equalSubstring(s: str, t: str, maxCost: int) -> int:
    cost = 0
    res = 0
    l = 0

    for r in range(len(s)):
        cost += abs(ord(s[r]) - ord(t[r]))

        while cost > maxCost:
            cost -= abs(ord(s[l]) - ord(t[l]))
            l += 1

        res = max(r - l + 1, res)

    return res
