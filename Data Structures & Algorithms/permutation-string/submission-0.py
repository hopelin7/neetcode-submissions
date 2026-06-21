class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1> n2:
            return False 
        need=  [0] * 10000
        have = [0] * 10000
        for i in s1:
            need[ord(i)] += 1
        
        left = 0
        for r in range(n2):
            have[ord(s2[r])] += 1
            if r >= n1:
                have[ord(s2[left])] -= 1
                left += 1
            if need == have:
                return True 
        return False


    