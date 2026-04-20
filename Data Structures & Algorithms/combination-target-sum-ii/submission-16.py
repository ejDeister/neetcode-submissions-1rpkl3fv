class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        c = sorted(candidates)
        def iter(i: int, r: List[int], s: int):
            if s == target:
                res.append(r.copy())
                return
            for j in range(i,len(c)):
                if j > i and c[j] == c[j-1]:
                    continue
                if s + c[j] > target:
                    break
                
                r.append(c[j])
                iter(j+1,r,s+c[j])
                r.pop()
        
        iter(0,[],0)
        return res