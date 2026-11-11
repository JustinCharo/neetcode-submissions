class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # DFS through a 1 found, and we want to mark each 1 found as visited, create a max count and relax it
        # if a larger island is found
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        max_area = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(i, j):
            # need to check bounds and check for 0 or 1
            if i < 0 or i > rows - 1 or j < 0 or j > cols - 1:
                return 0
            if grid[i][j] == 0:
                return 0
            area = 1
            grid[i][j] = 0
            for dx, dy in directions:
                area += dfs(i + dx, j + dy)
            
            return area
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    new_area = dfs(i, j)
                    max_area = max(max_area, new_area)
        
        return max_area