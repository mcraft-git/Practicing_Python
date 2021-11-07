
import pygame

class Shuttle:
    """A class to manage the shuttle."""

    def __init__(self,da_game):
        """Initialize the shuttle and set its starting position."""

        self.screen = da_game.screen
        self.screen_rect = da_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images\\troop_shuttle_fin.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self):
        """Draw the ship at its current location."""
        
        self.screen.blit(self.image, self.rect)