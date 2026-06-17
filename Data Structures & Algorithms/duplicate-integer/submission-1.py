class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h1 = set()
        for i in nums:
            if i in h1:
                return True 
            h1.add(i)
        return False

        