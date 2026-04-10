class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxwat = float('-inf')
        l = 0
        r = len(heights)-1
        while l < r:
            if heights[l] < heights[r]:
                less = heights[l]
                l += 1
            else:
                less = heights[r]
                r -= 1
            wat = (r-l+1) * less
            maxwat = max(wat,maxwat)

        return maxwat