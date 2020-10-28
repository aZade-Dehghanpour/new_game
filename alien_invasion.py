import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """ Overall class that manages the game assets and behaviours"""

    def __init__(self):
        #Initialize the game and create game resources
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def run_game(self):
        #start the main loop for the gaem
        while True:
            #watch out for keyboard and mouse events
            self._check_events()
            #Update location of ship
            self.ship.update()
            #Update screen
            self._update_screen()
            
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type ==pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self,event):
        if event.key == pygame.K_DOWN:
            self.ship.move_down = True
        elif event.key == pygame.K_UP:
            self.ship.move_up = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self,event):
        if event.key == pygame.K_DOWN: 
            self.ship.move_down = False
        elif event.key == pygame.K_UP:
            self.ship.move_up = False

    def _update_screen(self):
        """Update images on the screen and make most recently drawn surface visible"""
        
        #redraw the screen during each pass through the loop
        self.screen.fill(self.settings.screen_bg_color)
        #Draw ship at its current location
        self.ship.blitme()
        #make the most recently drawn screen visible
        pygame.display.flip()

if __name__ == "__main__":
    #make a game instance and run the game
    ai_game = AlienInvasion()
    ai_game.run_game()