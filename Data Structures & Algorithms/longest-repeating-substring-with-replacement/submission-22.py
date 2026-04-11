class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freqs = {'': 0}
        maxfreq = 0
        maxlength = 0
        for r, c in enumerate(s):
            freqs[c] = 1 + freqs.get(c, 0)
            maxfreq = max(maxfreq, freqs[c])

            while r-l+1 - maxfreq > k:
                freqs[s[l]] -= 1
                l += 1
        
            maxlength = max(maxlength, r-l+1)
        
        return maxlength