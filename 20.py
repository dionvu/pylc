def isValid(s: str) -> bool:
    matching = {')': '(', '}': '{', ']': '['}
    stack = []

    for c in s:
        if c in matching:
            if not stack or stack.pop() != matching[c]:
                return False
        else:
            stack.append(c)


    return not stack
