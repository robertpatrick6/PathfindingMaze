class Game_Map:
    ''' Represents the 2d node map for the game '''
    
    class Map_Node:
        ''' Represents the tiles within a Game_Map '''
    
        def __init__(self, x_coord, y_coord, passable):
            ''' Creates a Map_Node with coordinates (x_coord, y_coord) that
                is passable if passable == 0, otherwise it is impassable. '''
            
            self.x = x_coord
            self.y = y_coord
            self.passable = passable
            
        def get_adjacent_nodes(self, game_map):
            ''' Returns a set containing 2-tuples for the coordinates of adjacent
                nodes '''
            
            tuple_set = set()
            
            if self.x > 0:
                tuple_set.add((self.x-1,self.y))
            
            if self.x < game_map.get_width() - 1:
                tuple_set.add((self.x+1,self.y))
                
            if self.y > 0:
                tuple_set.add((self.x,self.y-1))
            
            if self.y < game_map.get_height() - 1:
                tuple_set.add((self.x,self.y+1))
                
            if self.x < game_map.get_width() - 1 and self.y > 0:
                tuple_set.add((self.x+1,self.y-1))
            
            if self.x < game_map.get_width() - 1 and self.y < game_map.get_height() - 1:
                tuple_set.add((self.x+1,self.y+1))
                
            if self.x > 0 and self.y > 0:
                tuple_set.add((self.x-1,self.y-1))
                
            if self.x > 0 and self.y < game_map.get_height() - 1:
                tuple_set.add((self.x-1,self.y+1))
            
            return tuple_set
        
        def get_coordinates(self):
            ''' Returns 2-tuple of the x,y coordinates '''
            
            return (self.x, self.y)
        
        def get_x(self):
            ''' Returns the x coordinate of the node '''
            
            return self.x
        
        def get_y(self):
            ''' Returns the y coordinate of the node '''
            
            return self.y
        
        def is_passable(self):
            ''' Returns a bool representing whether or not the node is passable '''
            
            return (True if self.passable == '0' else False)
        
        def toggle_node(self):
            ''' Switches the node between passable and impassable '''
            
            if self.is_passable():
                self.passable = '1'
            else:
                self.passable = '0'
        
    
    def __init__(self, file_name=''):
        ''' Creates a Game_Map by creating a dict of Map_Nodes
            based on the given text file. '''
        
        self.dest_node = None
        
        if file_name != '':
            file_array = map = []
            with open(file_name) as file:
                for line in file:
                    file_array.append(line.rstrip().split(','))
                
            self.width = max([len(x) for x in file_array])
            self.height = len(file_array)
            for i in range(self.height):
                file_array[i].extend([1 for j in range(self.width - len(file_array))])
                
            self.node_map = dict()
            for i in range(self.height):
                for j in range(self.width):
                    self.node_map[(j,i)] = Game_Map.Map_Node(j,i,file_array[i][j])
        
        else:
            self.width = 20
            self.height = 20
            
            self.node_map = dict()
            for i in range(self.height):
                for j in range(self.width):
                    self.node_map[(j,i)] = Game_Map.Map_Node(j,i,'0')
                    
    def set_dest_node(self, coordinates):
        ''' Sets the current destination node '''
        
        self.dest_node = coordinates
        
        
    def check_dest_node(self, coordinates):
        ''' Returns true if coordinates are current destination node '''
        
        return self.dest_node == coordinates
    
                
    def get_adjacent_nodes(self, coordinates):
        ''' Returns the pasable Map_Nodes adjacent to the given x,y coordinates as a set '''
        
        if (coordinates[0] >= 0 and coordinates[0] < self.width) and (coordinates[1] >= 0 and coordinates[1] < self.height):
            node_set = set()
            
            for node in self.node_map[coordinates].get_adjacent_nodes(self):
                
                if self.node_map[node].is_passable():
                    
                    # SE
                    if node[0] > coordinates[0] and node[1] > coordinates[1]:
                        if self.get_node((node[0] - 1, node[1])).is_passable() and self.get_node((node[0], node[1] - 1)).is_passable():
                            node_set.add(self.node_map[node])
                            continue
                    
                    # SW
                    elif node[0] < coordinates[0] and node[1] > coordinates[1]:
                        if self.get_node((node[0] + 1, node[1])).is_passable() and self.get_node((node[0], node[1] - 1)).is_passable():
                            node_set.add(self.node_map[node])
                            continue
                    
                    # NE
                    elif node[0] > coordinates[0] and node[1] < coordinates[1]:
                        if self.get_node((node[0] - 1, node[1])).is_passable() and self.get_node((node[0], node[1] + 1)).is_passable():
                            node_set.add(self.node_map[node])
                            continue
                    
                    # NW
                    elif node[0] < coordinates[0] and node[1] < coordinates[1]:
                        if self.get_node((node[0] + 1, node[1])).is_passable() and self.get_node((node[0], node[1] + 1)).is_passable():
                            node_set.add(self.node_map[node])
                            continue
                    
                    # N-S-E-W
                    else:
                        node_set.add(self.node_map[node])
            
            return node_set
        
        else:
            return set()
        
        
    def get_node(self, coordinates):
        ''' Returns the Map_Node at given x,y coordinates '''
        
        return self.node_map[coordinates]
    
    
    def get_width(self):
        ''' Returns the width of the game map '''
        
        return self.width
    
        
    def get_height(self):
        ''' Returns the height of the game map '''
        
        return self.height
    
    
    def toggle_node(self, coordinates):
        ''' Toggles a node between passable and impassable '''
        
        self.node_map[coordinates].toggle_node()