class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        chains = {}
        longest = 0
        for num in nums:
            #ignore dupes
            if num in chains:
                continue

            if num - 1 not in chains and num + 1 not in chains:
                chains[num] = num
            elif num - 1 in chains and num + 1 in chains:
                start = chains[num-1]
                end = chains[num+1]
                chains[start] = end
                chains[end] = start
                longest = max(longest, end-start)
            elif num - 1 in chains:
                start = chains[num-1]
                chains[start] = num
                chains[num] = start
                longest = max(longest, num-start)
            elif num + 1 in chains:
                end = chains[num+1]
                chains[end] = num
                chains[num] = end
                longest = max(longest, end-num)
        return longest+1
                