class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_length = 800
        self.bg_color = (94, 50, 50)
        
        #No player?
        self.player_speed = 0.5
        self.max_health = 3

        #Bulle... I mean Pew Pew Ammo
        self.bullet_speed = 0.6
        self.bullet_width = 6
        self.bullet_height = 15
        self.bullet_color = (0, 0, 0)
        self.bullets_allowed = 10

        #Chicken Butt :)
        self.enemy_speed = 0.15
        self.enemy_points = 10