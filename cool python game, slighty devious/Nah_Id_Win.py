import random
import time
import threading
import pygame
import sys
from settings import Settings
from player import Player
from bullet import Bullet
from ammo import Ammo
from ammo import ammo_left
from enemy import Enemy
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
class Silly:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((1200,800))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_length = self.screen.get_rect().height
        pygame.display.set_caption("Nah, Id Win")
        self.stats = GameStats(self)
        self.am = Ammo(self)
        self.sb = Scoreboard(self)
        self.player = Player(self)
        self.bullets = pygame.sprite.Group()
        self.bullet = Bullet(self)
        self.enemies = pygame.sprite.Group()
        self.play_button = Button(self, "Nah, Id Win (click)")
        self.enemies_killed = 0
    def run_game(self):
        while True:
            self._check_events()
            if self.stats.game_active:
                self.player.update()
                self.bullets.update()
                self._update_enemies()
                self._update_bullets()
                self._create_enemies()
            self._update_screen()
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
    def _check_keydown_events(self, event):
        global ammo_left
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = True
        elif event.key == pygame.K_DOWN:
            self.player.moving_down = True
        elif event.key == pygame.K_UP:
            self.player.moving_up = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_r:
            time.sleep(0.4)
            ammo_left = 1 + self.enemies_killed
            self.am.prep_ammo(ammo_left)
        elif (event.key == pygame.K_w) or (event.key == pygame.K_a) or (event.key == pygame.K_d) or (event.key == pygame.K_s):
            self.bullet.bullet_direction(event)

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = False
        elif event.key == pygame.K_UP:
            self.player.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.player.moving_down = False
    
    def _fire_bullet(self):
        global ammo_left
        if len(self.bullets) < self.settings.bullets_allowed and not(ammo_left == 0):
            ammo_left -= 1
            self.am.prep_ammo(ammo_left)
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    def _update_bullets(self):
        for bullet in self.bullets.copy():
            if (bullet.rect.bottom <= 0) or (bullet.rect.left <= 0) or (bullet.rect.top >= 800) or (bullet.rect.right >= 1200):
                self.bullets.remove(bullet)
        collisions = pygame.sprite.groupcollide(self.bullets, self.enemies, True, True)
        if collisions:
            for enemies in collisions.values():
                self.stats.score += self.settings.enemy_points * len(enemies)
            self.sb.prep_score()
            if self.enemies_killed < 12:
                self.enemies_killed += 1
        self._create_enemies()

    def _create_enemies(self):
        enemy = Enemy(self, self.player)
        if self.enemies_killed < 12:
            if len(self.enemies) < (8 + self.enemies_killed): #amount of enemy spawns
                enemy.x = random.randint(1, 1200)
                enemy.rect.x = enemy.x
                if random.randint(1,2) == 1:
                    enemy.y = 1
                else:
                    enemy.y = 780
                    enemy.rect.y = enemy.y
                self.enemies.add(enemy)
                self._repeat_create()
        else:
            if len(self.enemies) < 20: #amount of enemy spawns
                enemy.x = random.randint(1, 1200)
                enemy.rect.x = enemy.x
                if random.randint(1,2) == 1:
                    enemy.y = 1
                else:
                    enemy.y = 780
                    enemy.rect.y = enemy.y
                self.enemies.add(enemy)
                self._repeat_create()

    def _repeat_create(self):
        t = threading.Timer(random.randint(5, 10), self._create_enemies)
        t.start()
    
    def _update_enemies(self):
        self.enemies.update()
        if pygame.sprite.spritecollideany(self.player, self.enemies):
            self._player_hit()
    def _player_hit(self):
        if self.stats.health > 1:
            self.stats.health -= 1
            self.sb.prep_players()
            self.player.center_player()
            self.enemies.empty()
            self.bullets.empty()
            time.sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
    
    def _check_play_button(self, mouse_pos):
        global ammo_left
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.stats.reset_stats()
            self.stats.game_active = True
            self.stats.score = 0
            self.sb.prep_players()
            self.sb.prep_score()
            self.enemies.empty()
            self.bullets.empty()
            self.enemies_killed = 0
            ammo_left = 1
            self.player.center_player()
            self._create_enemies()
            pygame.mouse.set_visible(False)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.player.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.am.show_ammo()
        self.enemies.draw(self.screen)
        self.sb.show_score()
        if not self.stats.game_active:
            self.play_button.draw_button()
        pygame.display.flip()

if __name__ == "__main__":
    Nah = Silly()
    Nah.run_game()