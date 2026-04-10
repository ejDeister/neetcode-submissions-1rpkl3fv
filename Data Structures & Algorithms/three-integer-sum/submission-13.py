class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        trips = []
        for i, inum in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            tnum = nums[i+1:]
            tar = 0-inum
            l = 0
            r = len(tnum)-1
            while l < r:
                if tnum[l] + tnum[r] > tar:
                    r -= 1
                elif tnum[l] + tnum[r] < tar:
                    l += 1
                else:
                    trips.append([inum,tnum[l],tnum[r]])
                    l += 1
                    r -= 1
                    while l < r and tnum[l] == tnum[l-1]:
                        l += 1
        return trips