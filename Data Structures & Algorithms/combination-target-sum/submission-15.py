class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def iter(i: int, r: List[int], s: int):
            nonlocal res
            nonlocal nums
            if i == len(nums):
                return
            if s + nums[i] == target:
                res.append([*r,nums[i]])
            if s + nums[i] <= target:
                iter(i,[*r,nums[i]],s+nums[i])
            iter(i+1,r,s)
        iter(0,[],0)
        return res