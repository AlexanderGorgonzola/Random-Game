import time
import pygame
from pygame.sprite import Sprite
direction = "up"
class Bullet(Sprite):

    def __init__(self, Nah_game):
        super().__init__()
        self.screen = Nah_game.screen
        self.settings = Nah_game.settings
        self.color = self.settings.bullet_color
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.center = Nah_game.player.rect.center
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    
    def update(self):
        global direction
        if direction == "up":
            self.y -= self.settings.bullet_speed
            self.rect.y = self.y
        elif direction == "down":
            self.y += self.settings.bullet_speed
            self.rect.y = self.y
        elif direction == "left":
            self.x -= self.settings.bullet_speed
            self.rect.x = self.x
        elif direction == "right":
            self.x += self.settings.bullet_speed
            self.rect.x = self.x
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def bullet_direction(self, event):
        global direction
        if event.key == pygame.K_w:
            direction = "up"
            time.sleep(0.1)
        if event.key == pygame.K_s:
            direction = "down"
            time.sleep(0.1)
        if event.key == pygame.K_a:
            direction = "left"
            time.sleep(0.1)
        if event.key == pygame.K_d:
            direction = "right"
            time.sleep(0.1)