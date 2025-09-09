from collections import deque

def bfs(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    queue = deque()
    queue.append((start, [start]))
    visited = set()
    visited.add(start)
    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == goal:
            return path
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x+dx, y+dy
            if 0<=nx<rows and 0<=ny<cols and maze[nx][ny]==0 and (nx,ny) not in visited:
                queue.append(((nx,ny), path+[(nx,ny)]))
                visited.add((nx,ny))
    return None

maze = [
    [0,0,0,0,0],
    [1,1,0,1,0],
    [0,0,0,1,0],
    [0,1,1,0,0],
    [0,0,0,0,0]
]

start = (0,0)
goal = (4,4)
solution = bfs(maze, start, goal)
print("BFS Solution Path:", solution)