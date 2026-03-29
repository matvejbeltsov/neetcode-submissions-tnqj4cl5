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

        l = 0
        r = len(row) - 1

        while l <= r:
            mid = (l + r) // 2

            if row[mid] > target:
                r = mid - 1
            elif row[mid] < target:
                l = mid + 1
            else:
                return True
        return False