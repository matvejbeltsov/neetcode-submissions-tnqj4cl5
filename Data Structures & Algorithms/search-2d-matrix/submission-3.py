class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_top = 0
        row_bottom = len(matrix) - 1

        while row_top <= row_bottom:
            mid = (row_bottom + row_top) // 2

            row = matrix[mid]

            if row[0] > target:
                row_bottom = mid - 1
            elif row[-1] < target:
                row_top = mid + 1
            else:
                break
        else:
            return False
        
        left = 0
        right = len(row) - 1

        while left <= right:
            midd = (left + right) // 2

            if row[midd] == target:
                return True
            elif row[midd] > target:
                right = midd - 1
            else:
                left = midd + 1
        return False