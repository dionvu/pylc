from typing import List

def maxSatisfied(customers: List[int], grumpy: List[int], minutes: int) -> int:
    base = sum(n for i, n in enumerate(customers) if not grumpy[i])
    max_add = 0
    add = 0

    for i in range(len(grumpy)):
        if (grumpy[i]): add += customers[i]

        if (i >= minutes and grumpy[i - minutes]): 
            add -= customers[i - minutes]

        max_add = max(add, max_add)

    return base + max_add
