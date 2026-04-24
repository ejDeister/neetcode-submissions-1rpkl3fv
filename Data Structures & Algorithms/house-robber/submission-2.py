from functools import lru_cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache(None)
        def helper(i):
            if i >= len(nums):
                return 0
            return max(nums[i]+helper(i+2),nums[i]+helper(i+3))

        return max(helper(0),helper(1))
