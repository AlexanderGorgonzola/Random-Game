import time
import pygame
from ammo import ammo_left
from pygame.sprite import Sprite
class Player(Sprite):
    def __init__(self, Nah_game):
        super().__init__()
        self.screen = Nah_game.screen
        self.settings = Nah_game.settings
        self.screen_rect = Nah_game.screen.get_rect()
        self.image = pygame.image.load('images/player.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    def update(self):
        global direction
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.player_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.player_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.player_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.player_speed
        self.rect.x = self.x
        self.rect.y = self.y
        print(f"X: {self.x}")
        print(f"X: {self.y}")
        player_x = self.x
        player_y = self.y
    def blitme(self):
        self.screen.blit(self.image, self.rect)
    def reload(self):
        global ammo_left
        time.sleep(3)
        ammo_left = 5
    def center_player(self):
        self.rect.center = self.screen_rect.center
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)