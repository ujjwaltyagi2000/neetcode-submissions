class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # incorrect board
        # board =[["1","2",".",".","3",".","1",".","."],
        #         ["4",".",".","5",".",".",".",".","."],
        #         [".","9","1",".",".",".",".",".","3"],
        #         ["1",".",".",".","6",".",".",".","4"],
        #         [".",".",".","8",".","3",".",".","5"],
        #         ["7",".",".",".","2",".",".",".","6"],
        #         [".",".",".",".",".",".","2",".","."],
        #         [".",".",".","4","1","9",".",".","8"],
        #         [".",".",".",".","8",".",".","7","9"]]

        # # check rows
        # for i in range(0,9):
        #     row_hash = {}
        #     for j in range(0,9):
        #         elem = board[i][j]
        #         print(f"row = {i} | column = {j} | elem = {elem}")
        #         if elem != "." and elem not in row_hash:
        #             row_hash[elem] = 1
        #         elif elem in row_hash:
        #             print(f"Repeated element {elem} found in row: {i}")
        #             # return False
        
        # # check column 
        # for i in range(0,9):
        #     col_hash = {}
        #     for j in range(0,9):
        #         elem = board[j][i]
        #         print(f"column = {i} | row = {j} | elem = {elem}")
        #         if elem != "." and elem not in col_hash:
        #             col_hash[elem] = 1
        #         elif elem in col_hash:
        #             print(f"Repeated element {elem} found in col: {i}")
        #             # return False
        
        # check row and column
        for i in range(0,9):
            col_hash = {}
            row_hash = {}
            for j in range(0,9):
                row_elem = board[i][j]
                col_elem = board[j][i]
                print(f"column = {i} | row = {j} | row_elem = {row_elem}")
                if row_elem != "." and row_elem not in row_hash:
                    row_hash[row_elem] = 1
                elif row_elem in row_hash:
                    print(f"Repeated element {row_elem} found in row: {i}")
                    return False
                
                print(f"column = {j} | row = {i} | col_elem = {col_elem}")
                if col_elem != "." and col_elem not in col_hash:
                    col_hash[col_elem] = 1
                elif col_elem in col_hash:
                    print(f"Repeated element {col_elem} found in col: {i}")
                    return False
        
        # check boxes
        boxes = {}
        for i in range(0,9):
            for j in range(0,9):
                
                elem = board[i][j]
                box_key = (i//3, j//3)
                if box_key not in boxes and elem != ".":
                    boxes[box_key] = {}
                    boxes[box_key][elem] = 1
                elif box_key in boxes:
                    if elem != "." and elem not in boxes[box_key]:
                        boxes[box_key][elem] = 1

                    elif elem in boxes[box_key]:
                        print(f"Repeated element {elem} at row = {i} col = {j} found in box: {box_key}")            
                        return False
                        # boxes[box_key][elem] = 1

        # print(boxes)

        return True
                
