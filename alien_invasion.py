import sys
import pygame

class AlienInvasion:
    """ Overall class that manages the game assets and behaviours"""

    def __init__(self):
        #Initialize the game and create game resources
        pygame.init()
        self.screen = pygame.display.set_mode((500,500))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        #start the main loop for the gaem
        while True:
            #watch out for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
        #make the most recently drawn screen visible
        pygame.display.flip()

if __name__ == "__main__":
    #make a game instance and run the game
    ai_game = AlienInvasion()
    ai_game.run_game()