class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        num_islands = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(i, j):
        # Handle out of bounds
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == "0":
                return

            grid[i][j] = "0"
            for dx, dy in directions:
                move_x = i + dx
                move_y = j + dy
                dfs(move_x, move_y)

        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == "1":
                    dfs(x, y)
                    num_islands += 1
                
        return num_islands