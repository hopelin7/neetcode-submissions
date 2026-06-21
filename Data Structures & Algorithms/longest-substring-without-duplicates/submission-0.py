class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #  to track seen characters put it in a set 
        seen = set()
        maxi = 0 
        left = 0 
        for i in range(len(s)):
            if s[i] in seen:
                # do smth 
                while s[i] in seen:
                    seen.remove(s[left])
                    left += 1 
            
            seen.add(s[i])
            maxi = max(maxi, len(seen))
        return maxi 
        