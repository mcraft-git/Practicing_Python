import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the shuttle."""

    def __init__(self, da_game):
        """Create a bullet object at the shuttles's current position."""

        super().__init__()
        self.screen = da_game.screen
        self.settings = da_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0,0),
        # then set position based on shuttle's rect.
        # (This will make it look like bullets are fired from the shuttle.)
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = da_game.shuttle.rect.midtop
        
        # Store the bullet's Y position as a decimal value.
        # (This will be used to adjust the bullet's speed.)
        self.y = float(self.rect.y)
    

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.

        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    
    def draw_bullet(self):
        """Draw a bullet to the screen."""

        pygame.draw.rect(self.screen, self.color, self.rect)