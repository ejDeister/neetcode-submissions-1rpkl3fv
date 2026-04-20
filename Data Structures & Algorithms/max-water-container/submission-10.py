class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxwat = float('-inf')
        l = 0
        r = len(heights)-1
        while l < r:
            less = min(heights[l],heights[r])
            maxwat = max(maxwat,less*(r-l))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxwat
            