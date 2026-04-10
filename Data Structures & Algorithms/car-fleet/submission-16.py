class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # (10 - 4) / 2 = 3
        # (10 - 1) / 3 = 3
        # 1

        # (10 - 7) / 1 = 3
        # (10 - 4) / 2 = 3
        # (10 - 1) / 2 = 5
        # (10 - 0) / 1 = 10

        # is there a fleet ahead of you that will arrive after or at the same time as you?
            # if so, you are a part of the fleet


        pair = [[p,s] for p,s in zip(position,speed)]

        fts = []
        for p,s in sorted(pair)[::-1]:
            time = (target-p)/s
            if len(fts) == 0 or (len(fts) >= 1 and not time <= fts[-1]):
                fts.append(time)
        return len(fts)











