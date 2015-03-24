class Game_Object:
    
    def __init__(self, x_pos, y_pos):
        ''' Initialize a generic game object '''
        
        self.x = x_pos
        self.y = y_pos
        
    
    def _draw(self):
        ''' Generic draw method that does nothing. Override if necessary. '''
        
        pass
    
    
    def _update(self):
        ''' Generic update method that does nothing. Override if necessary. '''
        
        pass
    
    
    def get_pos(self):
        ''' Returns the current (x,y) position as a 2-tuple '''
        
        return (self.x, self.y)