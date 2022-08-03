class Settings:
    def __init__(self):

        # screen
        self.bg_color = (230,230,230)
        self.screen_width = 1280
        self.screen_height = 720

        # player
        self.player_color = (120,200,200)
        self.player_speed = 1
        self.attempts = 3

        # target
        self.target_width = 60
        self.target_height = 120
        self.target_color = (0, 120, 100)
        self.target_speed = 0.3

        self.target_dir = 1 # 1 down, -1 up

        # bullets
        self.bullet_width = 20
        self.bullet_height = 10
        self.bullet_speed = 1
        self.bullet_color = (50,50,65)
        self.bullets_allowed = 5
        

        