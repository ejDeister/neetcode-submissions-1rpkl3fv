class Solution:
    import re
    def isPalindrome(self, s: str) -> bool:
        s = "".join(s.split(" "))
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()

        if len(s) == 1:
            return True

        ls = len(s)//2
        
        l = ls-1
        r = ls if ls%2 == 0 else ls+1
        if len(s) % 2 == 0:
            print('even')
            l, r = len(s)//2-1, len(s)//2
        else:
            l, r = len(s)//2-1, len(s)//2+1

        return s[l::-1] == s[r:len(s)]
        # while r < len(s):
        #     print(s[l], s[r])
        #     if s[l] != s[r]:
        #         return False
        #     l -= 1
        #     r += 1
        # return True