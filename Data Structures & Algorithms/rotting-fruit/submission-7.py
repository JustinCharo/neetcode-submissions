from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Try bfs, need a deque for o(1) dequeues
        # Can't do dfs, because when traversing by depth, an orange that wasn't rotten at
        # minute 3 may be rotten later such as on minute 8
        # Approach, add rotten fruit to queue, check adjacent and if any fresh:
        # Rot and add to queue
        queue = deque()
        fresh = 0
        time = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
        
        directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        while fresh > 0 and queue:
            for i in range(len(queue)):
                i, j = queue.popleft()

                for dx, dy in directions:
                    row, col = i + dx, j + dy
                    if row in range(len(grid)) and col in range(len(grid[0])) and grid[row][col] == 1:
                        queue.append((row, col))
                        grid[row][col] = 2
                        fresh -= 1
            
            time += 1 
            
        if fresh == 0:
            return time
        else:
            return -1


