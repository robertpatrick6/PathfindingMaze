from game_object import Game_Object
from collections import deque

import pathfinding
import random



class Player_Object(Game_Object):
    
    def __init__(self, x_coord, y_coord, game_map, canvas):
        ''' Initializes a player object at given position on game game_map'''
        
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.game_map = game_map
        self.canvas = canvas
        self.current_dest = self.game_map.get_node(self.get_position())
        
        # Used to find a new path after set number of moves
        self.recalc_counter = 0
        self.RECALC_COUNT = 3
        
        # Movement speed on screen as a fraction of a tile
        self.speed = .2
        
        # Current tile pixel size based on canvas pixel size
        self.tile_height = self.canvas.winfo_height() // self.game_map.get_height()
        self.tile_width = self.canvas.winfo_width() // self.game_map.get_width()
        
        # Current pixel offset from current grid coordinates
        self.x_offset = 0
        self.y_offset = 0
        
        # Initialize destination path to empty deque and moving to False
        self.dest_path = deque()
        self.moving = False
        
        # Drawing size (proportion of tile) and color
        self.size = .5
        self.color = 'BLUE'
        
        # Used to time finding new paths
        self.random_path_counter = 0
        self.RANDOM_PATH_COUNT = 30
        
        # PATHFINDING TEST CALL
        # pathfinding.find_path(self.game_map.get_node((12,0)), self.game_map.get_node((5,16)), game_map)
    
    def _draw(self):
        ''' Draws the player to the given canvas '''
        
        self.tile_height = self.canvas.winfo_height() // self.game_map.get_height()
        self.tile_width = self.canvas.winfo_width() // self.game_map.get_width()

        player_height = (int)(self.size * self.tile_height)
        player_width = (int)(self.size * self.tile_width)
        
        self.x = (self.x_coord * self.tile_width + (self.tile_width // 2) - player_width // 2) + self.x_offset
        self.y = (self.y_coord * self.tile_height + (self.tile_height // 2) - player_height // 2) + self.y_offset
        
        self.canvas.create_rectangle(self.x, self.y, self.x + self.size * self.tile_width, self.y + self.size * self.tile_height,
                                     fill = self.color, outline = self.color)
        
    
    def _update(self):
        ''' Updates the player's state, moving the character along a path if it has one '''
        
        if len(self.dest_path) != 0 and not self.moving:
            self.current_dest = self.dest_path.pop()
            
            if self.current_dest.is_passable():
                self.moving = True
                self.recalc_counter += 1
                
            else:
                if len(self.dest_path) != 0:
                    self.dest_path = pathfinding.find_path(self.game_map.get_node(self.get_position()), self.dest_path.popleft(), self.game_map)
                
                else:
                    self.current_dest = self.game_map.get_node(self.get_position())
                    
                self.recalc_counter = 0
            
        elif self.moving:
            # Move NE
            if self.x < self.current_dest.get_x() * self.tile_width + (self.tile_width // 2) - self.size * self.tile_width // 2 and \
            self.y > self.current_dest.get_y() * self.tile_height + (self.tile_height // 2) - self.size * self.tile_height // 2:
                self.x_offset += self.speed * self.tile_width
                self.y_offset -= self.speed * self.tile_height
                
            # Move NW
            elif self.x > self.current_dest.get_x() * self.tile_width + (self.tile_width // 2) - self.size * self.tile_width // 2 and \
            self.y > self.current_dest.get_y() * self.tile_height + (self.tile_height // 2) - self.size * self.tile_height // 2:
                self.x_offset -= self.speed * self.tile_width
                self.y_offset -= self.speed * self.tile_height
            
            # Move SE
            elif self.x < self.current_dest.get_x() * self.tile_width + (self.tile_width // 2) - self.size * self.tile_width // 2 and \
            self.y < self.current_dest.get_y() * self.tile_height + (self.tile_height // 2) - self.size * self.tile_height // 2:
                self.x_offset += self.speed * self.tile_width
                self.y_offset += self.speed * self.tile_height
                
            # Move SW
            elif self.x > self.current_dest.get_x() * self.tile_width + (self.tile_width // 2) - self.size * self.tile_width // 2 // 2 and \
            self.y < self.current_dest.get_y() * self.tile_height + (self.tile_height // 2) - self.size * self.tile_height // 2:
                self.x_offset -= self.speed * self.tile_width
                self.y_offset += self.speed * self.tile_height
            
            # Move E
            elif self.x < self.current_dest.get_x() * self.tile_width + (self.tile_width // 2) - self.size * self.tile_width // 2:
                self.x_offset += self.speed * self.tile_width
            
            # Move W
            elif self.x > self.current_dest.get_x() * self.tile_width + (self.tile_width // 2) - self.size * self.tile_width // 2:
                self.x_offset -= self.speed * self.tile_width
            
            # Move S
            elif self.y < self.current_dest.get_y() * self.tile_height + (self.tile_height // 2) - self.size * self.tile_height // 2:
                self.y_offset += self.speed * self.tile_height
            
            # Move N
            elif self.y > self.current_dest.get_y() * self.tile_height + (self.tile_height // 2) - self.size * self.tile_height // 2:
                self.y_offset -= self.speed * self.tile_height
                
            if (abs(self.current_dest.get_x() * self.tile_width + (self.tile_width // 2) - self.size * self.tile_width // 2 - self.x) <= (self.speed*self.tile_width) and
                abs(self.current_dest.get_y() * self.tile_height + (self.tile_height // 2) - self.size * self.tile_height // 2 - self.y) <= (self.speed*self.tile_height)):
                
                self.x_offset = 0
                self.y_offset = 0
                
                self.moving = False
                
                self.x_coord = self.current_dest.get_x()
                self.y_coord = self.current_dest.get_y()
                
                if self.recalc_counter == self.RECALC_COUNT:
                    self.recalc_counter = 0
                    if len(self.dest_path) != 0:
                        self.dest_path = pathfinding.find_path(self.game_map.get_node(self.get_position()), self.dest_path.popleft(), self.game_map)
            
        else:
            self.recalc_counter = 0
            
            # UNCOMMENT TO ALLOW PLAYER TO RANDOMLY MOVE ON ITS OWN
            # Create random destination if update counter >= RANDOM_PATH_COUNT
##            if self.random_path_counter >= self.RANDOM_PATH_COUNT:
##                
##                new_rand_dest_coordinates = None
##                while (new_rand_dest_coordinates == None or not self.game_map.get_node(new_rand_dest_coordinates).is_passable()):
##                    new_rand_dest_coordinates = (random.randrange(self.game_map.get_width()), random.randrange(self.game_map.get_height()))
##                
##                self.dest_path = pathfinding.find_path(self.game_map.get_node((self.x_coord, self.y_coord)), \
##                                                       self.game_map.get_node(new_rand_dest_coordinates), \
##                                                        self.game_map)
##                
##                self.game_map.set_dest_node(new_rand_dest_coordinates)
##                
##                self.random_path_counter = 0
##                
##            else:
##                self.random_path_counter += 1
                
                
    def is_position(self, coordinates):
        ''' Returns True if given coordinates are the coordinates of the player or the player's current destination,
            returns False otherwise. '''
        
        return True if ((coordinates[0] == self.x_coord and coordinates[1] == self.y_coord) or (coordinates[0] == self.current_dest.get_x() and coordinates[1] == self.current_dest.get_y())) else False
    
    
    def get_position(self):
        ''' Returns the current coordinates of the player '''
        
        return (self.x_coord, self.y_coord)
    
    
    def move_to(self, tk_event):
        ''' Sets a path to follow to the given destination coordinates '''
        
        click_coords = (tk_event.x // self.tile_width, tk_event.y // self.tile_height)
         
        self.dest_path = pathfinding.find_path(self.game_map.get_node((self.x_coord, self.y_coord)), self.game_map.get_node(click_coords), self.game_map)
        
        self.game_map.set_dest_node(click_coords)
        
        # Resest random path counter
        self.random_path_counter = 0
         
        
