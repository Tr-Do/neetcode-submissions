class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            freq = {}
            for j in i:
                if j != '.':
                    if j in freq:
                        if freq[j] >= 1:
                            return False
                        else:
                            freq[j] += 1
                    else:
                        freq[j] = 1
        for i in range(9):
            freq = {}
            for j in range(9):
                val = board[j][i]
                if val != '.':
                    if val in freq:
                        if freq[val] >= 1:
                            return False
                        else:
                            freq[val] += 1
                    else:
                        freq[val] = 1
        for box_row in range(0,9,3):
            for box_col in range(0,9,3):
                freq = {}
                for i in range(box_row, box_row+3):
                    for j in range(box_col, box_col+3):
                        val = board[i][j]
                        if val != '.':
                            if val in freq:
                                if freq[val] >= 1:
                                    return False
                                else:
                                    freq[val] += 1
                            else:
                                freq[val] = 1
        return True