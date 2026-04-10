class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        if not strs:
            return res

        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            sLen = ""
            while s[i] != "#":
                sLen += s[i]
                i += 1
            i += 1
            sLen = int(sLen)
            strs.append(s[i:i+sLen])
            i += sLen
        return strs