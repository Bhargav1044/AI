import heapq

# Define the goal state for the 8-puzzle
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Utility function to calculate the Manhattan distance (heuristic)
def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                x, y = divmod(state[i][j] - 1, 3)
                distance += abs(x - i) + abs(y - j)
    return distance

# Function to get the neighbors (possible moves)
def get_neighbors(state):
    neighbors = []
    x, y = next((i, j) for i in range(3) for j in range(3) if state[i][j] == 0)
    
    # Possible moves: down, up, right, left
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

# Function to solve the 8-puzzle using A* algorithm
def a_star(start):
    # Priority queue with (cost, steps, state) and visited set
    queue = [(manhattan_distance(start), 0, start, [])]
    visited = set()
    
    while queue:
        cost, steps, state, path = heapq.heappop(queue)
        
        # Convert the state to a tuple for hashing
        state_tuple = tuple(tuple(row) for row in state)
        
        if state == goal_state:
            return path + [state]
        
        if state_tuple in visited:
            continue
        visited.add(state_tuple)
        
        # Explore neighbors
        for neighbor in get_neighbors(state):
            new_path = path + [state]
            heapq.heappush(queue, (steps + 1 + manhattan_distance(neighbor), steps + 1, neighbor, new_path))
    
    return None

# Helper function to print a state
def print_state(state):
    for row in state:
        print(row)
    print()

# Example usage
start_state = [
    [1, 2, 3],
    [5, 0, 6],
    [4, 7, 8]
]

solution = a_star(start_state)
print("Steps to solve the puzzle:")
for step in solution:
    print_state(step)
