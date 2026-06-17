class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h1 = dict()
        for i in nums:
            h1[i] = h1.get(i, 0) + 1 
        for i in h1.values(): 
            if i > 1:
                return True 
        return False

        