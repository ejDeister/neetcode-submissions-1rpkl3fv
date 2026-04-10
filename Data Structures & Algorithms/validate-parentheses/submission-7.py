class Solution:
    def isValid(self, s: str) -> bool:
        lefts = []
        parenL = { '(': 0, '[': 1, '{': 2}
        parenR = { ')': 0, ']': 1, '}': 2}
        for char in s:
            if char in parenL:
                lefts.append(char)
            elif char in parenR:
                if not lefts:
                    return False
                left = lefts.pop()
                if parenL.get(left) != parenR.get(char):
                    return False
        
        return not lefts