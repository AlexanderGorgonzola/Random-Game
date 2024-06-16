import pygame.font
class Bullet_direction:

    def __init__(self, Nah_game):
        self.screen = Nah_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = Nah_game.settings

        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 30)
    
    def direction_facing(self, direction):
        direction_str = str(f"Direction: " + direction)
        self.direction_image = self.font.render(direction_str, True, self.text_color, self.settings.bg_color)
        self.direction_rect = self.direction_image.get_rect()
        self.direction_rect.right = self.screen_rect.right - 20
        self.direction_rect.top = 20
    def show_direction(self):
        self.screen.blit(self.direction_image, self.direction_rect)