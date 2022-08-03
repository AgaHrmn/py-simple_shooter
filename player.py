import pygame

class Player:
    def __init__(self, game):

        self.screen = game.screen
        self.screen_rect = game.screen_rect
        self.settings = game.settings

        self.image_path = r"C:\Users\aolej\Desktop\Python\python_crash_course\part_2\pygame_excercises\target practice\player.png"
        self.image = pygame.image.load(self.image_path)
        self.rect = self.image.get_rect()

        self.rect.midleft = self.screen_rect.midleft
        self.y = self.rect.y

        self.moving_up = False
        self.moving_down = False

    def blit(self):
        self.screen.blit(self.image, self.rect)

    def move(self):
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= self.settings.player_speed
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.player_speed

    def center_player(self):
        self.rect.midleft = self.screen_rect.midleft
        self.y = self.rect.y
