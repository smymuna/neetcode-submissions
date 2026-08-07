class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        fresh = 0

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))

                elif grid[row][col] == 1:
                    fresh += 1
                
        minutes = 0
        
        while queue and fresh > 0:

            for _ in range(len(queue)):
                row, col = queue.popleft()

                for dr, dc in directions:
                    newRow = row + dr
                    newCol = col + dc

                    if (
                        0 <= newRow < rows and
                        0 <=newCol < cols and
                        grid[newRow][newCol] == 1
                    ):
                        grid[newRow][newCol] = 2
                        fresh -= 1
                        queue.append((newRow, newCol))

            minutes += 1

        return minutes if fresh == 0 else -1