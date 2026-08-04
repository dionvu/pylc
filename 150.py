from typing import List
import math

def evalRPN(tokens: List[str]) -> int:
    stack = []
    ops = {"*", "/", "+", "-"}

    for tok in tokens:
        if tok not in ops:
            stack.append(int(tok))
            continue

        b = stack.pop()
        a = stack.pop()

        match tok:
            case "*": stack.append(a * b)
            case "/": stack.append(math.trunc(a / b))
            case "+": stack.append(a + b)
            case "-": stack.append(a - b)

    return stack.pop()
