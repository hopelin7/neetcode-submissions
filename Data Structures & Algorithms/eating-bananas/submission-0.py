class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right 
        while left <= right:
            mid = left+(right-left)// 2 
            print(left, right, mid)
            total = 0 
            for i in piles:
                total += math.ceil(float(i)/mid)
            if total > h:
                left = mid + 1
            else:
                res = mid
                right = mid - 1
        return res 


        