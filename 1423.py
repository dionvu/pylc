from typing import List

def maxScore(cardPoints: List[int], k: int) -> int:
    wsize = len(cardPoints) - k
    score = sum(cardPoints)
    res = 0

    for i in range(len(cardPoints)):
        score -= cardPoints[i]

        if i >= wsize:
            score += cardPoints[i - wsize]

        if i >= wsize - 1: 
            res = max(score, res)

    return res
