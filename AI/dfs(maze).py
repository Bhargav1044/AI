def dfs_maze(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    path = []
    visited = set()

    # Directions for moving: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def dfs(x, y):
        # If out of bounds or at a wall, return False
        if x < 0 or y < 0 or x >= rows or y >= cols or maze[x][y] == 1 or (x, y) in visited:
            return False

        # Add to visited set and path
        visited.add((x, y))
        path.append((x, y))

        # If we reached the end, return True
        if (x, y) == end:
            return True

        # Explore neighbors in each direction
        for dx, dy in directions:
            if dfs(x + dx, y + dy):
                return True

        # If no path is found, backtrack
        path.pop()
        return False

    # Run DFS from the start position
    if dfs(*start):
        # Create a copy of the maze to mark the path
        maze_with_path = [row[:] for row in maze]
        
        # Mark the solution path with "*"
        for x, y in path:
            maze_with_path[x][y] = "*"
        
        # Print the maze with the solution path
        print("Maze with path from start to end:")
        for row in maze_with_path:
            print(" ".join(str(cell) if cell != "*" else "*" for cell in row))
    else:
        print("No path found")

# Example usage
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
start = (0, 0)  # Starting point
end = (4, 4)    # Ending point

dfs_maze(maze, start, end)
