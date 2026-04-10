class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        ops = set(['*','+','-','/'])
        for t in tokens:
            if t not in ops:
                nums.append(int(t))
            else:
                two = nums.pop()
                one = nums.pop()
                if t == '+':
                    nums.append(one+two)
                elif t == '-':
                    nums.append(one-two)
                elif t == '*':
                    nums.append(one*two)
                elif t == '/':
                    nums.append(math.trunc(one/two))
                print(one,t,two, '=',nums[-1])
        return nums.pop()