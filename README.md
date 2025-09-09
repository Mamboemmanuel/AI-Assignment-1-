# AI-Assignment-1-

---

## **1. Maze Problem (Algorithmic Problem Solving)**

### **a) Start State**

- The start state is the cell where the agent (or robot) begins its journey in the maze.
- In a 5x5 grid, if we choose the top-left corner, the start state is `(0, 0)`.
-  The representation is usually as a tuple of coordinates `(row, column)`, e.g., `(0, 0)`.

### **b) Goal State**

- The goal state is the destination cell the agent must reach.
- In a 5x5 grid, if we choose the bottom-right corner, the goal state is `(4, 4)`.
- As a tuple of coordinates, e.g., `(4, 4)`.

### **c) Possible Actions from Each Cell**

- **Actions available**:  
  From any cell `(x, y)` in the maze, the agent can move:
    - **Up**: `(x-1, y)` if `x > 0`
    - **Down**: `(x+1, y)` if `x < (N-1)` (here N=5)
    - **Left**: `(x, y-1)` if `y > 0`
    - **Right**: `(x, y+1)` if `y < (N-1)`
- **Restrictions**:
    - Cannot move through walls/obstacles (represented as `1` in the maze).
    - Cannot move outside the grid (indices must remain within bounds).

### **d) Valid Solution Paths Using Search Strategies**

#### **i. Breadth-First Search (BFS)**

- This finds the shortest path in an unweighted maze.
- It explores all neighboring cells before moving to the next layer.
- **Sample Python Code**:

```python name=maze_bfs.py
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
```

#### **ii. Depth-First Search (DFS)**

- **Use Case**: Explores a path fully before backtracking; not guaranteed to find the shortest path.
- **How it works**: Goes as deep as possible before backtracking.
- **Sample Python Code**:

```python name=maze_dfs.py
def dfs(maze, start, goal):
    stack = [(start, [start])]
    visited = set()
    visited.add(start)
    rows, cols = len(maze), len(maze[0])
    while stack:
        (x, y), path = stack.pop()
        if (x, y) == goal:
            return path
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x+dx, y+dy
            if 0<=nx<rows and 0<=ny<cols and maze[nx][ny]==0 and (nx,ny) not in visited:
                stack.append(((nx,ny), path+[(nx,ny)]))
                visited.add((nx,ny))
    return None

dfs_solution = dfs(maze, start, goal)
print("DFS Solution Path:", dfs_solution)
```

#### **iii. A* Search**

- **Use Case**: Finds the shortest path efficiently using a heuristic.
- **Heuristic**: Manhattan distance (for grid mazes).
- **How it works**: Uses both the path cost so far and an estimated cost to the goal.
- **Code**:

```python name=maze_astar.py
import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    open_set = []
    heapq.heappush(open_set, (heuristic(start, goal), 0, start, [start]))
    visited = set()
    while open_set:
        _, cost, (x, y), path = heapq.heappop(open_set)
        if (x, y) == goal:
            return path
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x+dx, y+dy
            if 0<=nx<rows and 0<=ny<cols and maze[nx][ny]==0 and (nx,ny) not in visited:
                heapq.heappush(open_set, (cost+1+heuristic((nx,ny), goal), cost+1, (nx,ny), path+[(nx,ny)]))
    return None

astar_solution = a_star(maze, start, goal)
print("A* Solution Path:", astar_solution)
```

#### **Comparison Table**

| Search Strategy | Pros                 | Cons                    | Best Use            |
|-----------------|----------------------|-------------------------|---------------------|
| BFS             | Finds shortest path  | Memory intensive        | Small/simple mazes  |
| DFS             | Simple, low memory   | Not guaranteed optimal  | Path existence      |
| A*              | Optimal, efficient   | Heuristic needed        | Large/complex mazes |

## **2. AI System for Ambulance Dispatch in a City**

### **a) State Space**

- Each state represents the ambulance’s position in the city.
- **Grid Model:** `(x, y)` intersection on a city grid.
- **Graph Model:** Nodes as intersections, edges as roads.

### **b) Actions**

- Move to an adjacent, reachable intersection.
- Possible directions: up, down, left, right (or more, if the road network allows).

### **c) Goal**

- Reach the intersection where the emergency occurred.

### **d) Path Cost**

- Path cost can be:
    - **Distance** between intersections.
    - **Estimated time** (considering traffic, speed limits, etc.).
    - **Number of moves/edges traversed**.

### **e) Suitable Search Strategy & Justification**

-  A* Search
- **Why?**
    - The city is large (large state space).
    - Need to find the fastest or shortest route under constraints.
    - A* can use domain-specific heuristics (straight-line distance, estimated travel time).
- **How?**
    - Use A* with a heuristic that estimates remaining time/distance (e.g., Manhattan or Euclidean distance, or live traffic data).
    - Edge costs can reflect real road conditions and traffic.

#### **Example: A* for Ambulance Dispatch**

```python name=ambulance_astar.py
import heapq

def heuristic(a, b):
    # Use real-time data as a heuristic
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_city(city_map, start, goal):
    open_set = []
    heapq.heappush(open_set, (heuristic(start, goal), 0, start, [start]))
    g_cost = {start: 0}
    while open_set:
        _, cost, current, path = heapq.heappop(open_set)
        if current == goal:
            return path
        for neighbor, move_cost in city_map.get(current, []):
            new_cost = g_cost[current] + move_cost
            if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal)
                heapq.heappush(open_set, (priority, new_cost, neighbor, path + [neighbor]))
    return None

# Example city_map: adjacency list with weighted edges
city_map = {
    (0,0): [((0,1), 2), ((1,0), 1)],
    (0,1): [((0,0), 2), ((0,2), 2)],
    (1,0): [((0,0), 1), ((1,1), 2)],
    (1,1): [((1,0), 2), ((0,1), 2)],
    (0,2): [((0,1), 2)],
    # ... add more nodes as needed
}

start = (0,0)
goal = (0,2)
solution = a_star_city(city_map, start, goal)
```



### **Summary Table: Ambulance Dispatch**

| Element         | Description                                       | Example                                   |
|-----------------|--------------------------------------------------|-------------------------------------------|
| State Space     | Ambulance location (grid or node in road graph)  | (x, y) = (3, 5)                           |
| Actions         | Move to adjacent intersection/node               | Up, Down, Left, Right                     |
| Goal            | Reach emergency location                         | (x, y) = (7, 8)                           |
| Path Cost       | Distance/time/traffic-based cost                 | Edge cost: 2 min between two intersections|
| Search Strategy | A* Search                                        | Heuristic: Manhattan/EUclidean/Traffic    |


### **Justification for A\* Search**

- **Optimality:** Finds the shortest/fastest path if heuristic is admissible.
- **Efficiency:** Explores fewer states than uniform-cost or BFS.
- **Scalability:** Suitable for large, real-world networks.
- **Flexibility:** Can incorporate real-time data (traffic, road closures).
