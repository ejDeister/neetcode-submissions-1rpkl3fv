class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def iter(i: int, r: List[int]):
            nonlocal res
            nonlocal nums
            if i == len(nums)-1:
                res.append(r)
                res.append([*r,nums[i]])
            else:
                iter(i+1, r)
                iter(i+1, [*r,nums[i]])
        iter(0,[])
        return res