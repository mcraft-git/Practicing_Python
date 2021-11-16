import sys
import pygame
from pygame.constants import KEYUP
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
            self._check_events()
            self.shuttle.update()
            self._update_screen()


    def _check_events(self):
        """Respond to key presses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                    
            # IF a keyboard key press is received...
            elif event.type == pygame.KEYDOWN:
                # IF the key is the RIGHT ARROW key...
                if event.key == pygame.K_RIGHT:
                    # Move the shuttle to the right.
                    self.shuttle.moving_right = True
                # IF the key is the LEFT ARROW key...
                elif event.key == pygame.K_LEFT:
                    # Move the shuttle to the left.
                    self.shuttle.moving_left = True

            # IF a keyboard key release is received...
            elif event.type == pygame.KEYUP:
                # IF the key is the right arrow key...
                if event.key == pygame.K_RIGHT:
                    # Stop right-wise shuttle movement.
                    self.shuttle.moving_right = False
                # IF the key is the left arrow key...
                elif event.key == pygame.K_LEFT:
                    # Stop left-wise shuttle movement.
                    self.shuttle.moving_left = False



    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.shuttle.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':

    # Make a game instance and run the game.
    da = DronesAttack()
    da.run_game()