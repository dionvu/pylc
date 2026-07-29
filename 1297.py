from typing import Counter

def maxFreq(s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
    occur = Counter()

    for i in range(len(s) - minSize + 1):
        substr = s[i: i + minSize]

        if len(set(substr)) <= maxLetters:
            occur[substr] += 1

    return max(occur.values()) if len(occur) else 0
