import pygame.font
from pygame.sprite import Group
from player import Player
class Scoreboard:
    def __init__(self, Nah_game):
        self.Nah_game = Nah_game
        self.screen = Nah_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = Nah_game.settings
        self.stats = Nah_game.stats
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 50)
        self.prep_score()
        self.prep_players()
    def prep_score(self):
        score_str = str("Score: " + str(self.stats.score))
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 0
    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.players.draw(self.screen)

    def prep_players(self):
        self.players = Group()
        for player_number in range(self.stats.health):
            player = Player(self.Nah_game)
            player.rect.x = player_number * (player.rect.width + 5)
            player.rect.y = 35
            self.players.add(player)