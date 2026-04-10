class MinStack:

    def __init__(self):
        self.arr = []
        self.minarr = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        if len(self.minarr) == 0:
            self.minarr.append(val)
        elif val <= self.minarr[-1]:
            self.minarr.append(val)

    def pop(self) -> None:
        if self.arr[-1] == self.minarr[-1]:
            self.minarr.pop()
        self.arr.pop()
        

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.minarr[-1]
