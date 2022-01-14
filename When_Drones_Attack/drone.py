import pygame
from pygame.sprite import Sprite

class Drone(Sprite):
    """A class to represent a single drone in the fleet."""

    def __init__(self, da_game):
        """Initialize the drone and set its starting position."""

        super().__init__()
        self.screen = da_game.screen

        # Load the drone image and set its rect attribute.
        self.image = pygame.image.load('images/drone_01.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)