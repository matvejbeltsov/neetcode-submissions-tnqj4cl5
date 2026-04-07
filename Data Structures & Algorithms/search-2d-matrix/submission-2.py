class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_top = 0
        row_bottom = len(matrix) - 1

        while row_top <= row_bottom:
            row_mid = (row_top + row_bottom) // 2

            row = matrix[row_mid]
            
            if row[0] > target:
                row_bottom = row_mid - 1
            elif row[-1] < target:
                row_top = row_mid + 1
            else:
                break
        else:
            return False
        
        left = 0
        right = len(row) - 1

        while left <= right:
            mid = (left + right) // 2

            if row[mid] == target:
                return True
            elif row[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False