class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, rows*cols - 1
        while l <= r:
            m = l + ((r-l)//2)
            mid_row, mid_col = m // cols, m % cols
            if matrix[mid_row][mid_col] < target:
                l = m + 1
            elif matrix[mid_row][mid_col] > target:
                r = m - 1
            else:
                return True
        return False