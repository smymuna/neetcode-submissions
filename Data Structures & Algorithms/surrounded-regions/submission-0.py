class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        
        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        def dfs(row, col):
            if(
                row < 0 or row >= ROWS or
                col < 0 or col >= COLS or
                board[row][col] != "O"
            ):
                return
        
            board[row][col] = "T"

            for dr, dc in directions:
                newRow = row + dr
                newCol = col +dc

                dfs(newRow, newCol)

        for col in range(COLS):
            if board[0][col] == "O":
                dfs(0, col)

            if board[ROWS - 1][col] == "O":
                dfs(ROWS - 1, col)

        for row in range(ROWS):
            if board[row][0] == "O":
                dfs(row, 0)

            if board[row][COLS - 1] == "O":
                dfs(row, COLS - 1)

        for row in range(ROWS):
            for col in range(COLS):

                if board[row][col] == "O":
                    board[row][col] = "X"

                elif board[row][col] == "T":
                    board[row][col] = "O"