class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxl = 0
        l = 0
        seen = {}
        for r, c in enumerate(s):
            if c in seen:
                l = max(l,seen[c]+1)
            seen[c] = r
            maxl = max(maxl,r-l+1)
        return maxl