import pygame.locals


class InputHandler():
    
    _inputs = 
    {
        'key_left_down' : False,
        'key_up_down' : False,
        'key_right_down' : False,
        'key_down_down' : False
    }

    @staticmethod
    def handle(events, game_objects):
        
        inputs = dict(_inputs)  # Fresh copy of _inputs for this "tick"

        for event in events:
            ### KEYBOARD ###
            if event.type == pygame.locals.KEYDOWN:  
                if event.key == pygame.locals.K_LEFT:
                    inputs['key_left_down'] = True
    
        