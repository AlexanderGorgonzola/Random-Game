import pygame.font
ammo_left = 1
class Ammo:

    def __init__(self, Nah_game):
        self.screen = Nah_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = Nah_game.settings
        self.ammo = ammo_left

        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 40)
        self.prep_ammo(ammo_left)
    
    def prep_ammo(self, ammo):
        ammo_str = str("Ammo: " + str(ammo))
        self.ammo_image = self.font.render(ammo_str, True, self.text_color, self.settings.bg_color)
        self.ammo_rect = self.ammo_image.get_rect()
    def show_ammo(self):
        self.screen.blit(self.ammo_image, self.ammo_rect)