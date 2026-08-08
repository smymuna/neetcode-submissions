class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        def dfs(row, col, visited):
            visited.add((row, col))

            for dr, dc in directions:
                newRow = row + dr
                newCol = col + dc

                if(
                    0 <= newRow < rows and
                    0 <= newCol < cols and
                    (newRow, newCol) not in visited and
                    heights[newRow][newCol] >= heights[row][col]
                ):
                    dfs(newRow, newCol, visited)

        for col in range(cols):
            dfs(0, col, pacific)
            dfs(rows - 1, col, atlantic)

        for row in range(rows):
            dfs(row, 0, pacific)
            dfs(row, cols - 1, atlantic)

        result = []

        for row in range(rows):
            for col in range(cols):
                if (row, col) in pacific and (row, col) in atlantic:
                    result.append([row, col])
        
        return result