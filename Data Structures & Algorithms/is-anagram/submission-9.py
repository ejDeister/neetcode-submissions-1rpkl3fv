class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            seenS = {}
            seenT = {}
            for i in range(len(s)):
                if s[i] in seenS:
                    seenS[s[i]] += 1
                else:
                    seenS[s[i]] = 1
                if t[i] in seenT:
                    seenT[t[i]] += 1
                else:
                    seenT[t[i]] = 1
            if seenT == seenS:
                return True
            return False