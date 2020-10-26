from settings import Settings
import pygame

class Ship:
    """A class to manage the ship"""
    def __init__(self,ai_game):

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load("images/my_ship.png")
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft

    def blitme(self):
        self.screen.blit(self.image,self.rect)
