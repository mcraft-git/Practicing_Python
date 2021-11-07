
import sys
import pygame
from settings import Settings
from shuttle import Shuttle

class DronesAttack:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""

        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("When DRONES Attack!?")

        self.shuttle = Shuttle(self)
    

    def run_game(self):
        """Start the main loop for the game."""

        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            self.shuttle.blitme()

            # Make the most recently drawn screen visible.
            pygame.display.flip()


if __name__ == '__main__':

    # Make a game instance and run the game.
    da = DronesAttack()
    da.run_game()