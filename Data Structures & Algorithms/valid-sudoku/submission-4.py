class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dict_row = defaultdict(set)
        dict_col = defaultdict(set)
        dict_box = defaultdict(set)

        for idx_row, row in enumerate(board):
            for idx_col, el in enumerate(row):
                if el == '.':
                    continue

                idx_boxes = (idx_row // 3, idx_col // 3)

                if el in dict_row[idx_row] or el in dict_col[idx_col] or el in dict_box[idx_boxes]:
                    return False

                dict_row[idx_row].add(el)
                dict_col[idx_col].add(el)
                dict_box[idx_boxes].add(el)

        return True
        
        