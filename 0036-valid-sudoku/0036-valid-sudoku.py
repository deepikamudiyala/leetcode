class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        seen = []

        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c != '.':
                    seen.append((c, i))
                    seen.append((j, c))
                    seen.append((i//3, j//3, c))

        return len(seen) == len(set(seen))
