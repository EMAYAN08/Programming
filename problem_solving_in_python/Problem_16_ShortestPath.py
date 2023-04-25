"""
You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. 
Each False boolean represents a tile you can walk on.
Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. 
If there is no possible path, then return null. You can move up, left, down, and right. 
You cannot move through walls. 
You cannot wrap around the edges of the board.
For example, given the following board:
[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7, 
since we would need to go through (1, 2) because there is a wall everywhere else on the second row.
"""

from collections import deque

def shortest_path(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    queue = deque([(start, 0)])
    visited = set([start])
    
    while queue:
        (row, col), steps = queue.popleft()
        
        if (row, col) == end:
            return steps
        
        for (r, c) in ((row-1, col), (row+1, col), (row, col-1), (row, col+1)):
            if (0 <= r < rows and 0 <= c < cols and maze[r][c] == False and (r, c) not in visited):
                queue.append(((r, c), steps+1))
                visited.add((r, c))
    
    return None # No path found

# Test the function with the example given in the prompt
maze = [[False, False, False, False],
        [True, True, False, True],
        [False, False, False, False],
        [False, False, False, False]]

start = (3, 0)
end = (0, 0)

print(shortest_path(maze, start, end)) # Output: 7
