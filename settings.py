class Settings:
    """A class to stor all settings for alien invasion"""
    def __init__(self):
        #initialize the game settings

        #screen settings
        self.screen_height = 800
        self.screen_width = 1200
        self.screen_bg_color = (60,60,60)

        #Ship settings
        self.ship_speed = 2.5

        #Bullet settings
        self.bullet_speed = 1
        self.bullet_color = (255,255,255)
        self.bullet_height = 3
        self.bullet_width = 15

