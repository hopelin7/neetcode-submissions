class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h1 = dict()
        for i in range(len(nums)):
            if target - nums[i] in h1:
                return [h1.get(target - nums[i]), i]
            h1[nums[i]] = i 
        