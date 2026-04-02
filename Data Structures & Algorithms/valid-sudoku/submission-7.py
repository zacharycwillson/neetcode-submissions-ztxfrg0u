class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #check if rows are valid
        for row in board:
            valid_row = set()
            for num in row:
                if num == '.':
                    continue
                if num in valid_row:
                    return False
                valid_row.add(num)
        
        #check if cols are valid
        for i in range(9):
            valid_col = set()
            for row in board:
                if row[i] == '.':
                    continue
                if row[i] in valid_col:
                    return False
                valid_col.add(row[i])
        
        #check if each box is valid
        for i in range(0, 9 , 3):
            for j in range(0, 9, 3):
                valid_box = set()
                for k in range(3):
                    for l in range(3):
                        num = board[i + k][j + l]
                        if num == '.':
                            continue
                        if num in valid_box:
                            return False
                        valid_box.add(num)
        return True

            

        

        