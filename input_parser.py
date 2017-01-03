import pygame.locals


class PygameInputParser():
    
    _app_input = {
        'quitting' : False
    }

    @staticmethod
    def parse(events, game_objects):

        # quit, minimize, maximize, etc
        app_input = dict(PygameInputParser._app_input)

        for event in events:
            ###########
            ### APP ###
            ###########
            if event.type == pygame.locals.QUIT:
                app_input['quitting'] = True

            ###############
            ### CONTROL ###
            ###############

            ### KEYBOARD ###
            elif event.type == pygame.locals.KEYDOWN:
                if event.key == pygame.locals.K_LEFT:
                    [game_object.set_move_left_down() for game_object in game_objects if game_object.is_player]
                elif event.key == pygame.locals.K_UP:
                    [game_object.set_move_up_down() for game_object in game_objects if game_object.is_player]
                elif event.key == pygame.locals.K_DOWN:
                    [game_object.set_move_down_down() for game_object in game_objects if game_object.is_player]
                elif event.key == pygame.locals.K_RIGHT:
                    [game_object.set_move_right_down() for game_object in game_objects if game_object.is_player]
    
        return app_input