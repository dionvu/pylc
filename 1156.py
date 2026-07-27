from typing import Counter

def maxRepOpt1(text: str) -> int:
    freq = Counter(text)
    res = 0

    for target in freq:
        nontargets = 0
        l = 0

        for r in range(len(text)):
            nontargets += text[r] != target

            while (nontargets > 1):
                nontargets -= text[l] != target
                l += 1

            wsize = r - l + 1
            if (not nontargets):
                res = max(wsize, res)
                continue

            res = max(wsize if freq[target] > wsize - 1 else wsize - 1, res)

    return res


class Solution:
    def maxRepOpt1(self, text: str) -> int:
        freq = Counter(text)
        res = 0

        for target in freq:
            nontargets = 0
            l = 0

            for r in range(len(text)):
                nontargets += text[r] != target

                while (nontargets > 1):
                    nontargets -= text[l] != target
                    l += 1

                wsize = r - l + 1
                if (not nontargets):
                    res = max(wsize, res)
                    continue

                res = max(wsize if freq[target] > wsize - 1 else wsize - 1, res)

        return res


