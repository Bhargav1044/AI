import random

WALL, PATH = 1, 0

class MazeGenerator:
    def __init__(self, width, height):
        self.width, self.height = width, height
        self.maze = [[WALL] * width for _ in range(height)]

    def generate_maze(self, r, c):
        self.maze[r][c] = PATH
        for dy, dx in random.sample([(0, 2), (0, -2), (2, 0), (-2, 0)], 4):
            nr, nc = r + dy, c + dx
            if 0 < nr < self.height and 0 < nc < self.width and self.maze[nr][nc] == WALL:
                self.maze[nr][nc] = self.maze[r + dy // 2][c + dx // 2] = PATH
                self.generate_maze(nr, nc)

    def print_maze(self):
        for row in self.maze:
            print(''.join('#' if cell == WALL else ' ' for cell in row))

# Instantiate and generate the maze
maze = MazeGenerator(7, 7)
maze.generate_maze(1, 1)
maze.print_maze()
