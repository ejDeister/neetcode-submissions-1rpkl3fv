class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # {} to track chains (ends point to each other)
        # Five cases:
        # 1 - No matches
            # Add to set
        # 2 - Double match
            # start/end point to each other
        # 3 - Start match
            # Update start
        # 4 - End match
            # Update end
        # 5 - Duplicate
            # Nothing 
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
                print(num, longest, 1, 'single')
            elif num - 1 in chains and num + 1 in chains:
                start = chains[num-1]
                end = chains[num+1]
                chains[start] = end
                chains[end] = start
                print(num, longest, end-start, 'double')
                longest = max(longest, end-start)
            elif num - 1 in chains:
                start = chains[num-1]
                chains[start] = num
                chains[num] = start
                print(num, longest, num-start, 'end+')
                longest = max(longest, num-start)
            elif num + 1 in chains:
                end = chains[num+1]
                chains[end] = num
                chains[num] = end
                print(num, longest, end-num, 'start+')
                longest = max(longest, end-num)
        return longest+1
                