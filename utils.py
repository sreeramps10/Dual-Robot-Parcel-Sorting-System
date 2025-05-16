import random
import time
import heapq
# === A* algorithm ===

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_neighbours(node, grid_width, grid_height, obstacles):
    neighbours = []
    x, y = node
    possible_moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for dx, dy in possible_moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < grid_width and 0 <= ny < grid_height and (nx, ny) not in obstacles:
            neighbours.append((nx, ny))
        
    return neighbours

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

def a_star(start, goal, obstacles, grid_width, grid_height):
    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbour in get_neighbours(current, grid_width, grid_height, obstacles):
            tentative_g_score = g_score[current] + 1  # All moves cost 1

            if neighbour not in g_score or tentative_g_score < g_score[neighbour]:
                came_from[neighbour] = current
                g_score[neighbour] = tentative_g_score
                f_score[neighbour] = tentative_g_score + heuristic(neighbour, goal)
                heapq.heappush(open_set, (f_score[neighbour], neighbour))

    return []


# === ID Generator ===

parcel_counter = {
    'A': 0,
    'B': 0,
    'C': 0,
}

def generate_random_parcel_id():
    delivery_point = random.choice(['A', 'B', 'C'])
    parcel_counter[delivery_point] += 1
    parcel_id = f"{delivery_point}-{parcel_counter[delivery_point]:04d}"
    return parcel_id, delivery_point

# === Time ===

class Timer:
    def __init__(self, interval_sec):
        self.interval = interval_sec
        self.last_time = time.time()

    def ready(self):
        """Returns True if the time interval has passed since the last reset."""
        return time.time() - self.last_time >= self.interval

    def reset(self):
        """Resets the timer."""
        self.last_time = time.time()
        