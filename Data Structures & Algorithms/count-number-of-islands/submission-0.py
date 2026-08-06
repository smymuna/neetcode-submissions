class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return
            
            if grid[row][col] == "0":
                return
            
            if (row, col) in visited:
                return

            visited.add((row, col))

            for dr, dc in directions:
                newRow = row + dr
                newCol = col + dc
                dfs(newRow, newCol)

        islands = 0

        for row in range(rows):
            for col in range(cols):

                if grid[row][col] == "1" and (row, col) not in visited:
                    islands += 1
                    dfs(row, col)
        
        return islands