import sys
import pygame


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = (230, 230, 230)
        self.clock = pygame.time.Clock()  # Initialize the clock here

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Fill the screen with the background color.
            self.screen.fill(self.bg_color)  # Add this line to fill the screen with the background color

            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)  # Use the clock to control the frame rate


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
