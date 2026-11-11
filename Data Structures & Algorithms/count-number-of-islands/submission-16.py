class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows, num_cols = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        sum = 0

        def dfs(row, col):
            if (row < 0 or row > num_rows - 1 or col < 0 or col > num_cols - 1):
                return
            if grid[row][col] == '0':
                return
            grid[row][col] = '0'
            
            for dx, dy in directions:
                dfs(row + dx, col + dy)

        for i in range(num_rows):
            for j in range(num_cols):
                if (grid[i][j] == '1'):
                    dfs(i, j)
                    sum += 1

        return sum            