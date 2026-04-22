class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        res = False
        seen = set()
        def iter(i, j, s, d):
            nonlocal res
            if s == s3 and i == len(s1) and j == len(s2):
                res = True
            if d >= len(s3) or (i,j) in seen:
                return
            seen.add((i,j))
            if i < len(s1) and s3[d] == s1[i]:
                iter(i+1,j,s+s1[i],d+1)
            if j < len(s2) and s3[d] == s2[j]:
                iter(i,j+1,s+s2[j],d+1)
        
        iter(0, 0, "", 0)
        return res
