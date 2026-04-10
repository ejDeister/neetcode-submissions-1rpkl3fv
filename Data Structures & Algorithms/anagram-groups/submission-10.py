class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        seenI = 0
        ans = []
        for word in strs:
            sortedW = ''.join(sorted(word))
            if sortedW in seen:
                print('HI')
                ans[seen[sortedW]] += [word]
            else:
                ans.append([word])
                seen[sortedW] = seenI
                seenI += 1

        return ans