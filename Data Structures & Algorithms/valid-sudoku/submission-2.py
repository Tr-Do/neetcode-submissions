class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def helper(cell, sett):
            if cell == '.':
                return True
            if cell in sett:
                return False
            sett.add(cell)
            return True

        for i in range(9):
            seen = set()
            for j in range(9):
                if not helper(board[i][j], seen):
                    return False

        for i in range(9):
            seen = set()
            for j in range(9):
                if not helper(board[j][i], seen):
                    return False

        for i in range(0,9,3):
            for j in range(0,9,3):
                seen = set()
                for m in range(i, i+3):
                    for n in range(j, j+3):
                        if not helper(board[m][n], seen):
                            return False
        return True
