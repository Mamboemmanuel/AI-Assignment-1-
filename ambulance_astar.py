import heapq

def heuristic(a, b):
    # Use Manhattan distance or real-time data as a heuristic
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
print("Ambulance A* Solution Path:", solution)