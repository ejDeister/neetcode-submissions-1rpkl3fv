class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxwat = float('-inf')
        l = 0
        r = len(heights)-1
        h = heights
        while l < r:
            if h[l] < h[r]:
                less = h[l]
                l += 1
            else:
                less = h[r]
                r -= 1
            wat = (r-l+1) * less
            print(l,r,wat)
            maxwat = max(wat,maxwat)

        return maxwat