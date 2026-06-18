class Solution:
    def getArea(self, height, width):
        return height * width
    def maxArea(self, heights: List[int]) -> int:
        maxi = 0
        left, right = 0, len(heights) - 1
        while left < right:
            height = min(heights[left], heights[right])
            area = self.getArea(height, right - left)
            maxi = max(maxi, area)
            if heights[left] > heights[right]:
                right -=1 
            else:
                left +=1 
        return maxi 
