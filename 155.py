class MinStack:
    def __init__(self):
        self.monodec = []
        self.stack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.monodec or value <= self.monodec[-1]: 
            self.monodec.append(value)

    def pop(self) -> None:
        if self.stack.pop() == self.monodec[-1]:
            self.monodec.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.monodec[-1]
