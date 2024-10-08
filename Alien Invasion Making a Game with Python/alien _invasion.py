import sys
import pygame

from Beggining.dictinary import alien, new_alien
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.clock = pygame.time.Clock()  # Initialize the clock here
        self.settings = Settings()
        self.screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width=self.screen.get_rect().width
        self.settings.screen_height=self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets=pygame.sprite.Group()
        self.aliens=pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()

            for bullet in self.bullets.copy():
                if bullet.rect.bottom<=0:
                    self.bullets.remove(bullet)
            print(len(self.bullets))



            self._update_screen()
            self.clock.tick(60)  # Use the clock to control the frame rate


    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.rect.x +=1
            self.ship.moving_right =True
        elif event.key==pygame.K_LEFT:
            self.ship.moving_left=True
        elif event.key ==pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()


    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right=False
        elif event.key==pygame.K_LEFT:
            self.ship.moving_left=False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets)<self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)



    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom<=0:
                self.bullets.remove(bullet)

    def _create_fleet(self):
        alien=Alien(self)

        alien_width, alien_height =alien.rect.size

        current_x, current_y =alien_width,alien_height
        while current_y<(self.settings.screen_height - 3* alien_height):
            while current_x < (self.settings.screen_widthq       - 2 * alien_width):
                self._create_aliens(current_x,current_y)
                current_x+=2*alien_width

                current_x = alien_width
                current_y += 2 * alien_height



    def _create_aliens(self,x_position,y_position):
        new_alien=Alien(self)
        new_alien.x=x_position
        new_alien.rect.x=x_position
        new_alien.rect.y=y_position
        self.aliens.add(new_alien)



    def _update_screen(self):
            self.screen.fill(self.settings.bg_color)
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            self.ship.blitme()
            self.aliens.draw((self.screen))
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
