class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eatgood(k: int) -> bool:
            hour = h
            for pile in piles:
                hour -= math.ceil(pile/k)
            print(k,hour)
            return hour
        l = 1
        r = max(piles)
        minh = float('inf')
        while l <= r:
            m = math.floor((l+r)/2)
            print(l,r,m)
            lo = eatgood(m)
            if lo > 0:
                minh = min(minh, m)
                r = m-1
            elif lo < 0:
                l = m+1
            else:
                minh = min(minh,m)
                r = m-1
        return minh