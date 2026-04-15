class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t = temperatures
        s = [0]
        res = [0] *len(t)
        # i = len(t)-2
        # while i >= 0:
        for i in range(len(t)):
            while s and t[s[-1]] < t[i]:
                r = s.pop()
                res[r] = i-r
            s.append(i)
        return res
            