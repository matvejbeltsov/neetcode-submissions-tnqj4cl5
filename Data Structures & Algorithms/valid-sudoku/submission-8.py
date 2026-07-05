class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        set_row = defaultdict(set)
        set_col = defaultdict(set)
        set_boxes = defaultdict(set)

        for idx_row, row in enumerate(board):
            for idx_col, elem in enumerate(row):
                if elem == '.':
                    continue
                
                idx_boxes = (idx_row // 3, idx_col // 3)

                if elem in set_row[idx_row] or elem in set_col[idx_col] or elem in set_boxes[idx_boxes]:
                    return False
                
                set_row[idx_row].add(elem)
                set_col[idx_col].add(elem)
                set_boxes[idx_boxes].add(elem)
        return True