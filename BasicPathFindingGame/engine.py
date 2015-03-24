import tkinter



class Engine:
    
    def __init__(self, game):
        ''' Initialize window and set it as the game's window '''

        self.game = game
        self.main_window = tkinter.Tk()
        
        self.game.set_window(self.main_window)
        
        # Currently set to ~30 frames per second
        self.refresh_time = 1000 // 30
        
    
    def _draw_all(self):
        ''' Draw all things necessary from the game and set update to run again after certain amount of time'''
        
        self.game._draw_all()
            
        self.main_window.after(self.refresh_time, self._update_all)
    
    
    def _update_all(self):
        ''' Update all thing necessary from the game and call _draw_all method '''
                
        self.game._update_all()
            
        self._draw_all()
    
    
    def start(self):
        ''' Start the game and begin update/draw cycle if not already started '''

        if not self.game.get_running():
            self.game.start_game()
            self._update_all()
            self.main_window.mainloop()