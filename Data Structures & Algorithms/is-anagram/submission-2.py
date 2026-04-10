class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        seent = {}
        for chars in s:
            if chars in seen:
                seen[chars] += 1
            else:
                seen[chars] = 1
        for chars in t:
            if chars in seent:
                seent[chars] += 1
            else:
                seent[chars] = 1
        if seen == seent:
            return True
        return False
