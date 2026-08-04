def simplifyPath(path: str) -> str:
    dirs = [dir for dir in path.split("/") if dir]
    stack = []

    for dir in dirs:
        if dir == "..":
            if stack: 
                stack.pop()
        elif dir != ".":
            stack.append(dir)

    return "/" + "/".join(stack)
