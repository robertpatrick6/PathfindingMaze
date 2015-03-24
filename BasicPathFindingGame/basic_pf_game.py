from game import Game
from player_object import Player_Object
from game_map import Game_Map

import tkinter 



class Basic_PF_Game(Game):
    
    def __init__(self):
        ''' Initialize Basic_Game '''
        
        Game.__init__(self)
        
        # Create the game tile map
#         self.game_map = Game_Map()          # Create a blank game map that is all passable initially
        self.game_map = Game_Map('map.txt') # Create a game map using the given text file
        

    
    def _draw_all(self):
        
        def _draw_game_map():
            
            tile_height = self.main_canvas.winfo_height() // self.game_map.get_height()
            tile_width = self.main_canvas.winfo_width() // self.game_map.get_width()
            
            for i in range(self.game_map.get_height()):
                for j in range(self.game_map.get_width()):
                    if (not self.game_map.get_node((j,i)).is_passable()):
                        self.main_canvas.create_rectangle(j*tile_width, i*tile_height,
                                                          (j+1)*tile_width, (i+1)*tile_height,
                                                          fill = "BLACK", outline = "BLACK")
                        
                    elif (self.game_map.check_dest_node((j,i))):
                        self.main_canvas.create_rectangle(j*tile_width, i*tile_height,
                                                          (j+1)*tile_width, (i+1)*tile_height,
                                                          fill = "RED", outline = "RED")
            
        if self.main_canvas != None:
            self.main_canvas.delete(tkinter.ALL)
        
        _draw_game_map()
        
        for game_obj in self.objects:
            game_obj._draw()
        
    
    def set_window(self, window):
        
        Game.set_window(self, window)
        
        # Create a canvas to draw on
        self.main_canvas = tkinter.Canvas(master = self.main_window, width = 800, height = 800, background = '#FFFFFF')
        self.main_canvas.grid(row = 0, column = 0, sticky = tkinter.NSEW, padx = 0, pady = 0)
        self.main_window.rowconfigure(0, weight = 1)
        self.main_window.columnconfigure(0, weight = 1)
        
        # Add player to window (Should be done elsewhere, needs redesign)
        self.add_player()
        
        # Bind commands for the mouse:
        # 1) Left-Mouse will set a path for the player
        # 2) Right-Mouse will toggle a tile between passable and impassable
        self.main_window.bind('<ButtonRelease-1>', self.player.move_to)
        self.main_window.bind('<ButtonRelease-3>', self.toggle_node)
        
        
    def add_player(self):
        
        self.player = Player_Object(1,1,self.game_map,self.main_canvas)
        self.objects.add(self.player)
        
        self.game_map.set_dest_node((1,1))
        
    
    def toggle_node(self, tk_event):
        ''' Finds the coordinates clicked on the screen, and toggles the appropriate node
            between passable and impassable '''
        
        click_coords = (tk_event.x // (self.main_canvas.winfo_width() // self.game_map.get_width()), tk_event.y // (self.main_canvas.winfo_height() // self.game_map.get_height()))
        
        if not self.player.is_position(click_coords):
            self.game_map.toggle_node(click_coords)