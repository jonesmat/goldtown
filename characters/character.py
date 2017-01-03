

class Character():
    
    def __init__(self):
        
        # Defines the character as a PC or NPC.  NPCs don't respond to 
        # player input.
        self.is_player = False

        # ***
        # *** input
        # ***
        self.move_left_down = False
        self.move_up_down = False
        self.move_right_down = False
        self.move_down_down = False
        
    def set_move_left_down(self, state):
        self.move_left_down = state
        
    def set_move_up_down(self, state):
        self.move_up_down = state
        
    def set_move_right_down(self, state):
        self.move_right_down = state
        
    def set_move_down_down(self, state):
        self.move_down_down = state