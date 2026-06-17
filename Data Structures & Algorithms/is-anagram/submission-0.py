class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1, s2 = dict(), dict()
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            char1, char2 = s[i], t[i]
            s1[char1] = s1.get(char1, 0 ) + 1
            s2[char2] = s2.get(char2, 0) + 1
        return s1 == s2


        