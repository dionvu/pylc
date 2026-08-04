def maxVowels(s: str, k: int) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    res = 0

    for i in range(len(s)):
        count += s[i] in vowels

        if i >= k:
            count -= s[i - k] in vowels

        if i >= k - 1:
            res = max(count, res)

    return res
