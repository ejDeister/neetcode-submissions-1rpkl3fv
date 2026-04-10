class Solution:
    def trap(self, height: List[int]) -> int:
        # 7
        # -1 +6
        # -2 
        #
        # -2 +3
        # -1
        # 
        # -1
        l = 0
        r = len(height)-1
        h = height
        while h[l] == 0:
            l += 1
            if l == len(height):
                return 0
        while h[r] == 0:
            r -= 1
            if r == -1:
                return 0
        maxwat = 0
        maxh = 0
        while l < r:
            if h[l] <= h[r]:
                maxwat -= min(h[l],maxh)
                if h[l] > maxh:
                    maxwat += (r-l-1)*(h[l]-maxh)
                    maxh = h[l]
                l += 1
            else:
                maxwat -= min(h[r],maxh)
                if h[r] > maxh:
                    maxwat += (r-l-1)*(h[r]-maxh)
                    maxh = h[r]
                r -= 1

        return maxwat