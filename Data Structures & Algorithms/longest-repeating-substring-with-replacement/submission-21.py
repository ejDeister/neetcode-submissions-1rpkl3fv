class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freqs = {'': 0}
        maxfreq = 0
        maxlength = 0
        for r, c in enumerate(s):
            if c not in freqs:
                freqs[c] = 0
            freqs[c] += 1
            maxfreq = max(maxfreq, freqs[c])                

            while r-l+1 - maxfreq > k:
                freqs[s[l]] -= 1
                l += 1
        
            maxlength = max(maxlength, r-l+1)
        
        return maxlength