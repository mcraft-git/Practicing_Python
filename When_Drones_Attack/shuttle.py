
import pygame

class Shuttle:
    """A class to manage the shuttle."""

    def __init__(self,da_game):
        """Initialize the shuttle and set its starting position."""

        self.screen = da_game.screen
        self.settings = da_game.settings
        self.screen_rect = da_game.screen.get_rect()

        # Load the shuttle image and get its rect.
        # The 'convert()' method works on the pixel format,
        # and improves blit processing speed.
        self.image = pygame.image.load('images/troop_shuttle_fin.bmp')
        self.rect = self.image.get_rect()

        # Start each new shuttle at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the shuttle's horizontal position.
        self.x = float(self.rect.x)

        # Store vertical position as float.
        self.y = float(self.rect.y)

        # Movement flags.
        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False


    def update(self):
        """Update the shuttle's position based on the movement flag."""

        # IF movement flag is set to TRUE, update shuttle's x value (not the rect),
        # to move shuttle right or left (depending on key input).
        # (ELIF is not used here because neither movement should have priority over the other)
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.shuttle_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.shuttle_speed
        
        # Update rect object from 'self.x'
        # This allows us to use a FLOAT (decimals) instead of the default INT (no decimals)
        self.rect.x = self.x

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.shuttle_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.shuttle_speed

        # Update rect object from 'self.y'
        self.rect.y = self.y


    
    def blitme(self):
        """Draw the ship at its current location."""
        
        self.screen.blit(self.image, self.rect)