import pygame
from pygame import locals

from input.input_handler import InputHandler
from ui.overworld_scene import OverworldScene
from characters.human import Human


pygame.init()
clock = pygame.time.Clock()

surface = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Goldtown')

# A list of all the active game objects.  Game objects are expected
# to respect a simple api: update(clock_delta), draw(surface).
game_objects = []

h = Human()
h.is_player = True
game_objects.append()

# The currently active scene
scene = OverworldScene()


while True:
    clock_delta = clock.get_time()

    # ***
    # *** Handler the user's input and notify each game object
    # ***
    InputHandler.handle(pygame.event.get(), game_objects) 

    # ***
    # *** UPDATE
    # ***
    scene.update(clock_delta)

    for game_object in game_objects:
        game_object.update(clock_delta)

    # ***
    # *** DRAW
    # ***
    scene.draw(surface)
    
    for game_object in game_objects:
        game_object.draw(surface)


    pygame.display.update()
    clock.tick(60)


