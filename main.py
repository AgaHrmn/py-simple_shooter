import pygame, sys
from time import sleep

from settings import Settings
from player import Player
from bullets import Bullet
from target import Target
from stats import Stats
from button import Button

class TargetPractice:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        self.screen.fill(self.settings.bg_color)
        pygame.display.set_caption("Target practice!")

        self.stats = Stats(self)

        self.player = Player(self)
        self.bullets = pygame.sprite.Group()
        self.target = Target(self)

        self.play_button = Button(self, "Play")

        pygame.display.flip()

    def run(self):
        while True:
            self._check_events()

            if self.stats.game_active:
                self.player.move()
                self.bullets.update()

            self._update_screen()
            
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
        elif event.key == pygame.K_UP:
            self.player.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.player.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.player.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.player.moving_down = False

    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.stats.reset_stats()
            self.stats.game_active = True

            self.bullets.empty()
            self.player.center_player()

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_target_edges(self):
        if self.target.check_edges():
            self._change_target_dir()
            
    def _change_target_dir(self):
        self.settings.target_dir *= -1

    def _update_target(self):
        self._target_missed()
        self._check_target_edges()
        self.target.move_target()

        target_hit = pygame.sprite.spritecollide(self.target, self.bullets, True)
        if target_hit:
            sleep(0.2)
        
    def _target_missed(self):
        if self.stats.attempts_left > 0:
            missed_bullets = []
            for bullet in self.bullets.copy():
                if bullet.rect.left >= self.screen_rect.right:
                    missed_bullets.append(bullet)
                    
                    if len(missed_bullets) >= 3:
                        self.stats.attempts_left -= 1
                        self.bullets.empty()
                        self.player.center_player()
                        sleep(1)
                        print(self.stats.attempts_left)
        else:
            self.stats.game_active = False
                
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.player.blit()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
            
        self.target.draw_target()
        if self.stats.game_active:
            self._update_target()

        if not self.stats.game_active:
            self.play_button.draw_button()
        
        pygame.display.flip()



#########################################################################

TP = TargetPractice()
TP.run()