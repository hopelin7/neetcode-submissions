class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sort = sorted(nums)
        curr_max = 1 
        maxi = 1 
        curr_val = sort[0]
        for i in range(1,len(nums)):
            if sort[i] == curr_val:
                continue
            if sort[i-1] + 1  == sort[i]:
                curr_max += 1 
                curr_val = sort[i]
            else:
                curr_max = 1
                sort[i]
            maxi = max(maxi, curr_max)

        return maxi




        

        