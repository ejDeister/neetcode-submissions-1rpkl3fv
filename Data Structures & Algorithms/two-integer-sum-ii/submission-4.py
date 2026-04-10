class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        n = numbers
        while l < r:
            if n[l]+n[r] < target:
                l += 1
            elif n[l]+n[r] > target:
                r -= 1
            else:
                return [l+1,r+1]