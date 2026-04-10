class Solution:
    def isValid(self, s: str) -> bool:
        opentoclose = {
            '(': ')',
            '{': '}',
            '[': ']',
        }
        closetoopen = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        stack = []

        for c in s:
            if c in opentoclose:
                stack.append(c)
            elif c in closetoopen:
                if len(stack) == 0:
                    return False
                o = stack.pop()
                if closetoopen[c] != o:
                    return False
        if len(stack) == 0:
            return True
        return False