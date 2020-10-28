from settings import Settings
import pygame

class Ship:
    """A class to manage the ship"""
    def __init__(self,ai_game):

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.image = pygame.image.load("images/my_ship.png")
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft
        self.move_up = False
        self.move_down = False
        self.y = float(self.rect.y)


    def update(self):
        if self.move_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
            self.rect.y = self.y
        elif self.move_down and self.rect.bottom < self.settings.screen_height:
            self.y +=self.settings.ship_speed
            self.rect.y = self.y
        
    def blitme(self):
        self.screen.blit(self.image,self.rect)
