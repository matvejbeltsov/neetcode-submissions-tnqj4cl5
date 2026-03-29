class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for idx_row, row in enumerate(board):
            for idx_col, el in enumerate(row):

                if el == '.':
                    continue
                
                idx_boxes = (idx_row // 3, idx_col // 3)

                if el in rows[idx_row] or el in cols[idx_col] or el in boxes[idx_boxes]:
                    return False


                rows[idx_row].add(el)
                cols[idx_col].add(el)
                boxes[idx_boxes].add(el)
        
        return True