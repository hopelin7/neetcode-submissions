class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
            seen = set()
            for j in range(cols):
                if board[i][j] == '.':
                    continue 
                if board[i][j] in seen:
                    return False 
                seen.add(board[i][j])
        for j in range(cols):
            seen = set()
            for i in range(rows):
                if board[i][j] == '.':
                    continue 
                if board[i][j] in seen:
                    return False 
                seen.add(board[i][j])
        for square in range(rows):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True