import pygame
from pygame.sprite import Sprite
from player import Player
import settings
from pygame.locals import *
class Enemy(Sprite):
    


    def __init__(self, Nah_game, p):
        super().__init__()
        self.screen = Nah_game.screen
        self.settings = Nah_game.settings
        self.player = p
        self.image = pygame.image.load("images/enemy.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
            
    def update(self):
        if self.x > self.player.x:
            self.x -= self.settings.enemy_speed
            self.rect.x = self.x
        elif self.x < self.player.x:
            self.x += self.settings.enemy_speed
            self.rect.x = self.x
        if self.y < self.player.y:
            self.y += self.settings.enemy_speed
            self.rect.y = self.y
        elif self.y > self.player.y:
            self.y -= self.settings.enemy_speed
            self.rect.y = self.y