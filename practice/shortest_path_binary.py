from collections import deque  # deque provides O(1) FIFO operations, internally uses doubly linked list blocks

class Solution:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)  # store matrix dimension once to avoid repeated len() calls
        
        if not grid or grid[0][0] != 0 or grid[n-1][n-1] != 0:  # validate empty grid and blocked start/end
            return -1  # if start or end blocked, no path possible
        
        directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]  
        # 8 possible movements stored once in memory
        
        queue = deque([(0,0,1)])  # initialize queue with (row, col, distance)
        grid[0][0] = 1  # mark starting cell visited directly to avoid extra visited matrix
        
        while queue:  # BFS loop runs until queue empty
            row, col, dist = queue.popleft()  # pop left ensures FIFO (shortest path expansion)
            
            if row == n-1 and col == n-1:  # check if destination reached
                return dist  # return immediately since BFS guarantees shortest
            
            for dr, dc in directions:  # explore all 8 neighbors
                nr, nc = row + dr, col + dc  # compute neighbor coordinates
                
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    # bounds check prevents invalid memory access
                    # value 0 ensures cell is open and not visited
                    
                    grid[nr][nc] = 1  # mark visited to prevent duplicate processing
                    queue.append((nr, nc, dist + 1))  
                    # append neighbor with incremented distance (next BFS layer)
        
        return -1  # if queue exhausted without reaching end, path does not exist