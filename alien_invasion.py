import sys
import pygame
from settings import Settings

class AlienInvasion:
    """ Overall class that manages the game assets and behaviours"""

    def __init__(self):
        #Initialize the game and create game resources
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        #start the main loop for the gaem
        while True:
            #watch out for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #redraw the screen during each pass through the loop
            self.screen.fill(self.settings.screen_bg_color)
            #make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == "__main__":
    #make a game instance and run the game
    ai_game = AlienInvasion()
    ai_game.run_game()