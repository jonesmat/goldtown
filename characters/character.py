

class Character():
    
    def __init__(self):
        
        # Defines the character as a PC or NPC.  NPCs don't respond to 
        # player input.
        self.is_player = False

        # ***
        # *** input
        # ***
        self.key_left_down = False
        self.key_up_down = False
        self.key_right_down = False
        self.key_down_down = False
        