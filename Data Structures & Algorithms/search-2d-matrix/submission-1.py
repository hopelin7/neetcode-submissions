class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        left, right = 0, row * col - 1
        while left <= right:
            mid = math.ceil((left+right)//2)
            row_num = mid // col 
            col_num = mid % col 
            if matrix[row_num][col_num] > target:
                right -=1 
            elif matrix[row_num][col_num] < target:
                left += 1
            else: return True 
        return False 
        