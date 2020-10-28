import pygame
from pygame.sprite import Sprite

class Bullets(Sprite):
    """Class to manage bullets fired from the ship"""
    def __init__(self,aigame):
        #creat bullet at the location of ship
        super().__init__()
        self.screen = aigame.screen
        self.settings = aigame.settings
        self.color = aigame.settings.bullet_color
        self.speed = aigame.settings.bullet_speed
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midleft = aigame.ship.rect.midright
        self.x = float(self.rect.x)

    def update(self):
        self.x +=self.speed
        self.rect.x =self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)

