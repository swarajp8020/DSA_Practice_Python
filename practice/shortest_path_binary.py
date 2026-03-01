from collections import deque

def shortestPathMatrix(grid):
    n = len(grid)

    if n == 0:
        return -1
    
    if grid[0][0] != 0 or grid[n-1][n-1] != 0:
        return -1
    
    directions = [
        (-1, -1), (-1,0), (-1,1),
        (0, -1),           (0,1),
        (1, -1), (1, 0), (1, 1)
    ]
    queue = deque()
    queue.append((0,0,1))
    grid[0][0] = 1
    while queue:
        row, col, distance = queue.popleft()
        if row == n - 1 and col == n-1:
            return distance
        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc
            
            if 0 <= new_row < n and 0 <= new_col < n:
                if grid[new_row][new_col] == 0:
                    grid[new_row][new_col] = 1
                    queue.append((new_row, new_col, distance + 1))
    return -1

if __name__ == "__main__":
    grid = [[0,0,0],[1,1,0],[1,1,0]]
    print(shortestPathMatrix(grid))