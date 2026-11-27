class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
#         for i in range(9):
#             seen_row = set()
#             seen_col = set()
#             seen_box = set()
#             for j in range(9):
#                 row_cell = board[i][j]
#                 if row_cell != ".":
#                     if row_cell in seen_row:
#                         return False
#                     seen_row.add(row_cell)

#                 col_cell = board[j][i]
#                 if col_cell != ".":
#                     if col_cell in seen_col:
#                         return False
#                     seen_col.add(col_cell)

#                 box_row = 3 * (i // 3) + (j // 3)
#                 box_col = 3 * (i % 3) + (j % 3)
#                 box_cell = board[box_row][box_col]
#                 if box_cell != ".":
#                     if box_cell in seen_box:
#                         return False
#                     seen_box.add(box_cell)

#         return True

        seen = set()
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                
                row_tag = ("row", r, val)
                col_tag = ("col", c, val)
                box_tag = ("box", r // 3, c // 3, val)
                
                if row_tag in seen or col_tag in seen or box_tag in seen:
                    return False
                
                seen.add(row_tag)
                seen.add(col_tag)
                seen.add(box_tag)
                
        return True
