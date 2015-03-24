import tkinter



class Game:
    
    def __init__(self):
        ''' Initializes all necessary variables for a generic game '''
        
        self.objects = set()
        self.running = False
        self.main_canvas = None
        self.main_window = None
        
        
    def _draw_all(self):
        ''' Draws all objects within the game '''
        
        if self.main_canvas != None:
            self.main_canvas.delete(tkinter.ALL)
            
            for game_obj in self.objects:
                game_obj._draw(self.main_canvas)
            
            
    def _update_all(self):
        ''' Draws all objects within the game '''
        
        for game_obj in self.objects:
            game_obj._update()
        
        
    def get_objects(self):
        ''' Returns all objects within the game '''
        
        return self.objects
    
    
    def get_running(self):
        ''' Return the current running state of the game '''
        
        return self.running
    
    
    def set_window(self, window):
        ''' Set the game's display window '''
        
        self.main_window = window
        
        
    def start_game(self):
        ''' Starts the game '''
        
        self.running = True