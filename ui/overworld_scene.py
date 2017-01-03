import pygame
from pygame import locals
from pygame import Rect


class Scene():
    
    def __init__(self):
        self.viewport_rect = Rect(0, 0, 1, 1)
        self.device_rect = Rect(0, 0, 1, 1)

    def get_vp_x_from_dev_x(self, dev_x):
        ratio = self.device_rect.w / self.viewport_rect.w
        device_shift = dev_x - device_rect.x
		vp_shift = device_shift / ratio;

		return viewport_rect.x + vp_shift

    def get_vp_y_from_dev_y(self, dev_y):
        ratio = self.device_rect.h / self.viewport_rect.h
        device_shift = dev_y - device_rect.y
		vp_shift = device_shift / ratio

		return viewport_rect.y + vp_shift

    def get_dev_x_from_vp_x(self, vp_x):
        ratio = self.device_rect.w / self.viewport_rect.w
        vp_shift = vp_x - viewport_rect.x
		dev_shift = vp_shift / ratio;

		return device_rect.x + dev_shift

    def get_dev_y_from_vp_y(self, vp_y):
        ratio = self.device_rect.h / self.viewport_rect.h
        vp_shift = vp_y - viewport_rect.y
		dev_shift = vp_shift / ratio;

		return device_rect.y + dev_shift


class OverworldScene(Scene):

    def __init__(self):
        super().__init__()
        self.viewport_rect = Rect(0, 0, 1000, 1000)

    def update(self, clock_delta):
        pass

    def draw(self, surface):
        self.device_rect = surface.get_rect()

        surface.fill(pygame.Color(255, 255, 255))