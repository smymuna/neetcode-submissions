class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        INF = 2147483647

        queue = deque()

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append((row, col))

        while queue:
            row, col = queue.popleft()

            for dr, dc in directions:
                newRow= row + dr
                newCol = col + dc
                
                if (newRow < 0 or newRow >= rows or newCol < 0 or newCol >= cols):
                    continue
                
                if grid[newRow][newCol] != INF:
                    continue
                
                grid[newRow][newCol] = grid[row][col] + 1

                queue.append((newRow, newCol))