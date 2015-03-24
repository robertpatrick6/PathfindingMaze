import random

def create_maze(size):
    ''' Creates a maze within the given grid.
        Grid elements are 0s and 1s, with 0s being the path
        and 1s being the start_walls '''
    
    GRID_SIZE = size
    
    # Create grid
    grid = []
    for i in range(GRID_SIZE):
        grid.append([])
        for j in range(GRID_SIZE):
            grid[i].append(1)
            
    
    def set_next_node(current_node):
        ''' Recursively work through grid and set paths '''
        
        def invalid_node(node, direction):
            ''' Returns true if given node is invalid '''
            
            # Check that node isn't border node
            if (node[0] <= 0 or node[0] >= len(grid[0]) - 1 or
                node[1] <= 0 or node[1] >= len(grid) - 1):
                return True
            
            # Check that new node isn't already passable
            elif (grid[node[0]][node[1]] == 0):
                return True
            
            # Check adjacent nodes
            else:
                for i in range(0, 2):
                    for j in range(-1, 2):
                        if (direction == 0):
                            if ((node[0]+j,node[1]-i) != node):
                                if (grid[node[0]+j][node[1]-i] == 0):
                                    return True
                            
                        elif (direction == 1):
                            if ((node[0]+i,node[1]+j) != node):
                                if (grid[node[0]+i][node[1]+j] == 0):
                                    return True
                            
                        elif (direction == 2):
                            if ((node[0]+j,node[1]+i) != node):
                                if (grid[node[0]+j][node[1]+i] == 0):
                                    return True
                            
                        else:
                            if ((node[0]-i,node[1]+j) != node):
                                if (grid[node[0]-i][node[1]+j] == 0):
                                    return True
                            
            
            # Valid node
            return False
            
        
        # Determine direction of new node
        direction = random.randrange(4)
        
        # Set new node
        if direction == 0:
            next_node = (current_node[0], current_node[1] - 1)
        elif direction == 1:
            next_node = (current_node[0] + 1, current_node[1])
        elif direction == 2:
            next_node = (current_node[0], current_node[1] + 1)
        else:
            next_node = (current_node[0] - 1, current_node[1])
            
        new_direction = direction
        while (True):
            
            if (not invalid_node(next_node, new_direction)):
                # Set next node as passable
                grid[next_node[0]][next_node[1]] = 0
                
                # Find next node
                set_next_node(next_node)
                
            # Update to new direction
            new_direction = (new_direction - 1) % 4
            
            # Check if a full rotation has been done
            if (new_direction == direction):
                return
            
            # Set new node
            if new_direction == 0:
                next_node = (current_node[0], current_node[1] - 1)
            elif new_direction == 1:
                next_node = (current_node[0] + 1, current_node[1])
            elif new_direction == 2:
                next_node = (current_node[0], current_node[1] + 1)
            else:
                next_node = (current_node[0] - 1, current_node[1])
        
    
    # Determine start position
    start_wall = random.randrange(4)
    
    if start_wall % 2 == 0:
        start_position = random.randrange(1, len(grid) - 1)
    else:
        start_position = random.randrange(1, len(grid[0]) - 1)
        
    if start_wall == 0:
        start_coord = (start_position, 0)
    elif start_wall == 1:
        start_coord = (len(grid) - 1, start_position)
    elif start_wall == 2:
        start_coord = (start_position, len(grid[0]) - 1)
    else:
        start_coord = (0, start_position)
        
    grid[start_coord[0]][start_coord[1]] = 0
        
    # Recurse through grid
    set_next_node(start_coord)
    
    # Determine end position
    end_wall = random.randrange(4)
    
    if end_wall % 2 == 0:
        exit_position = random.randrange(1, len(grid) - 1)
    else:
        exit_position = random.randrange(1, len(grid[0]) - 1)
        
    while (end_wall == start_wall and exit_position == start_position):
        end_wall = random.randrange(4)
    
        if end_wall % 2 == 0:
            exit_position = random.randrange(1, len(grid) - 1)
        else:
            exit_position = random.randrange(1, len(grid[0]) - 1)
        
    if end_wall == 0:
        if (grid[exit_position][1] != 0):
            if (exit_position <= GRID_SIZE // 2):
                while(grid[exit_position][1] != 0):
                    exit_position = (exit_position+1) % GRID_SIZE
            else:
                while(grid[exit_position][1] != 0):
                    exit_position = (exit_position-1) % GRID_SIZE
                    
        exit_coord = (exit_position, 0)
        
    elif end_wall == 1:
        if (grid[GRID_SIZE - 2][exit_position] != 0):
            if (exit_position <= GRID_SIZE // 2):
                while(grid[GRID_SIZE - 2][exit_position] != 0):
                    exit_position = (exit_position+1) % GRID_SIZE
            else:
                while(grid[GRID_SIZE - 2][exit_position] != 0):
                    exit_position = (exit_position-1) % GRID_SIZE
                    
        exit_coord = (len(grid) - 1, exit_position)
        
    elif end_wall == 2:
        if (grid[exit_position][GRID_SIZE - 2] != 0):
            if (exit_position <= GRID_SIZE // 2):
                while(grid[exit_position][GRID_SIZE - 2] != 0):
                    exit_position = (exit_position+1) % GRID_SIZE
            else:
                while(grid[exit_position][GRID_SIZE - 2] != 0):
                    exit_position = (exit_position-1) % GRID_SIZE
                    
        exit_coord = (exit_position, len(grid[0]) - 1)
        
    else:
        if (grid[1][exit_position] != 0):
            if (exit_position <= GRID_SIZE // 2):
                while(grid[1][exit_position] != 0):
                    exit_position = (exit_position+1) % GRID_SIZE
            else:
                while(grid[1][exit_position] != 0):
                    exit_position = (exit_position-1) % GRID_SIZE
                    
        exit_coord = (0, exit_position)
        
    grid[exit_coord[0]][exit_coord[1]] = 0
    
    return grid