import pygame

class Target:
    def __init__(self, game):

        self.screen = game.screen
        self.screen_rect = game.screen_rect
        self.settings = game.settings
        self.color = self.settings.target_color

        self.rect = pygame.Rect(0,0, self.settings.target_width, self.settings.target_height)
        self.rect.midright = self.screen_rect.midright

        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

        self.moving_up = True
        self.moving_down = True

    def draw_target(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def check_edges(self):
        if self.rect.top <= 0 or self.rect.bottom >= self.screen_rect.bottom:
            return True

    def move_target(self):
            self.y += (self.settings.target_speed * self.settings.target_dir)
            self.rect.y = self.y


    
