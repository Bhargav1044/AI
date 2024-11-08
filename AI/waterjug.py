from collections import deque

# Function to check if the target can be reached
def water_jug_bfs(cap_a, cap_b, target):
    # To track visited states
    visited = set()
    
    # Queue to store the states (jug A, jug B) and the path taken
    queue = deque([((0, 0), [])])  # Start with both jugs empty and an empty path
    
    while queue:
        (a, b), path = queue.popleft()
        
        # If we reach the target amount in either jug, return the path
        if a == target or b == target:
            path.append((a, b))
            return path
        
        # Skip this state if it's already visited
        if (a, b) in visited:
            continue
        visited.add((a, b))
        
        # Generate possible actions and add them to the queue
        # Each new state appends to the path to show the sequence of moves
        
        # Fill jug A
        queue.append(((cap_a, b), path + [(cap_a, b)]))
        
        # Fill jug B
        queue.append(((a, cap_b), path + [(a, cap_b)]))
        
        # Empty jug A
        queue.append(((0, b), path + [(0, b)]))
        
        # Empty jug B
        queue.append(((a, 0), path + [(a, 0)]))
        
        # Pour water from A to B
        new_a = a - min(a, cap_b - b)
        new_b = b + min(a, cap_b - b)
        queue.append(((new_a, new_b), path + [(new_a, new_b)]))
        # Pour water from B to A
        new_a = a + min(b, cap_a - a)
        new_b = b - min(b, cap_a - a)
        queue.append(((new_a, new_b), path + [(new_a, new_b)]))
    
    return "No solution found"

# Example usage
cap_a = 4  # Capacity of jug A
cap_b = 3  # Capacity of jug B
target = 2  # Target amount of water

solution_path = water_jug_bfs(cap_a, cap_b, target)
print("Steps to reach the target amount of water:")
for step in solution_path:
    print(step)
