import pygame
from pygame.sprite import Sprite

class Bullets(Sprite):

    def __init__(self,aigame):
        super().__init__()
        self.screen = aigame.screen
        self.settings = aigame.settings
        self.color = aigame.settings.bullet_color
        self.speed = aigame.settings.bullet_speed
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midleft = aigame.ship.rect.midright
