from maze_creation import create_maze
import sys

sys.setrecursionlimit(8000)

if __name__ == '__main__':
    
    grid = create_maze(25)
    
    for i in range(len(grid[0])):
        print(grid[0][i], end = "")
        for j in range(1, len(grid)):
            print("," + str(grid[j][i]), end = "")
        print()
