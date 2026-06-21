class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        maxi = 0 
        while left < right and right <= len(prices) - 1:
            if prices[right] < prices[left]:
                # set left to right since we found a lower val lower always better 
                left = right 
                right += 1 
            else:
                diff = prices[right] - prices[left]
                maxi = max(diff, maxi)
                right += 1 
        return maxi 


        