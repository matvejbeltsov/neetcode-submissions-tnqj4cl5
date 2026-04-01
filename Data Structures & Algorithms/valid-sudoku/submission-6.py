class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for idx_row, row in enumerate(board):
            for idx_col, elem in enumerate(row):
                if elem == '.':
                    continue

                idx_boxes = (idx_row // 3, idx_col // 3)

                if elem in rows[idx_row] or elem in cols[idx_col] or elem in boxes[idx_boxes]:
                    return False
                
                rows[idx_row].add(elem)
                cols[idx_col].add(elem)
                boxes[idx_boxes].add(elem)
        return True
