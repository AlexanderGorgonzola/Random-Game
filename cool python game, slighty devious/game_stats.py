class GameStats:
    def __init__(self, Nah_game):
        self.settings = Nah_game.settings
        self.reset_stats()
        self.game_active = False
        self.score = 0

    def reset_stats(self):
        self.health = self.settings.max_health