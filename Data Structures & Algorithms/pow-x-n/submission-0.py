class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        result = x
        for i in range(1,abs(n)):
            result *= x
        print(result)
        if n < 0:
            result = 1 / result
        return result
         