class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0 
        charSet = set(s)

        for char in charSet:
            l, count = 0, 0 
            maxi = 0 
            for r in range(len(s)):
                if s[r] == char:
                    count += 1
                while r - l + 1 - count > k:
                    if s[l] == char:
                        count -= 1 
                    l += 1  
                maxi = max(maxi, r-l + 1)
            res = max(res, maxi)
        return res

        