
import sys
import pygame
from settings import Settings
from shuttle import Shuttle
from bullet import Bullet
from drone import Drone

class DronesAttack:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""

        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("When DRONES Attack!?")

        self.shuttle = Shuttle(self)

        # The pygame 'sprite.Group()' class behaves like a list,
        # but with a few extra features.
        self.bullets = pygame.sprite.Group()
        self.drones = pygame.sprite.Group()

        self._create_fleet()


    def run_game(self):
        """Start the main loop for the game."""

        while True:
            self._check_events()
            self.shuttle.update()
            self._update_bullets()
            self._update_screen()


    def _check_events(self):
        """Respond to key presses and mouse events."""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # IF a keyboard key press is received...
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            # IF a keyboard key release is received...
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self,event):
        """Respond to key presses."""

        # IF the key is the RIGHT ARROW key...
        if event.key == pygame.K_RIGHT:
            # Move the shuttle to the right.
            self.shuttle.moving_right = True
        # IF the key is the LEFT ARROW key...
        elif event.key == pygame.K_LEFT:
            # Move the shuttle to the left.
            self.shuttle.moving_left = True

        # Same deal for up and down arrow presses.
        elif event.key == pygame.K_DOWN:
            self.shuttle.moving_down = True
        elif event.key == pygame.K_UP:
            self.shuttle.moving_up = True
        
        # If the 'q' key is pressed, exit game.
        elif event.key == pygame.K_q:
            sys.exit()

        elif event.key == pygame.K_SPACE:
            self._fire_bullet()


    def _check_keyup_events(self,event):
        """Respond to key releases."""

        # IF the key is the right arrow key...
        if event.key == pygame.K_RIGHT:
            # Stop right-wise shuttle movement.
            self.shuttle.moving_right = False
        # IF the key is the left arrow key...
        elif event.key == pygame.K_LEFT:
            # Stop left-wise shuttle movement.
            self.shuttle.moving_left = False

        # Same deal for up and down arrow releases.
        elif event.key == pygame.K_DOWN:
            self.shuttle.moving_down = False
        elif event.key == pygame.K_UP:
            self.shuttle.moving_up = False

    
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""

        # This statement ensures the player can only have
        # a set amount of bullets on screen at once.
        if len(self.bullets) < self.settings.bullets_allowed:

            new_bullet = Bullet(self)

            # The 'add()' method is like append, but used specifically with Pygame groups.
            self.bullets.add(new_bullet)


    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""

        # Update bullet positions.
        self.bullets.update()

        # This loop will remove bullets from memory once they are offscreen.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)


    def _create_drone(self, drone_number, row_number):
        """Create a drone and place it in the row."""

        # Make a drone and find the number of drones in a row.
        # Spacing between each drone is equal to one drone width.
        drone = Drone(self)
        drone_width, drone_height = drone.rect.size

        # We set each drone's 'x attribute' position as equal to its width...
        # ...plus twice its width (to account for the space between drones)...
        # ...multiplied by its drone number.
        # (Remember, each drone starts at the leftmost point of the available space).
        # We save the result of our calculation as the x-position of the drone's 'rect'...
        drone.rect.x = drone_width + 2 * drone_width * drone_number

        # ...and similarly calculate the y-position, based on the height and row number...
        drone.rect.y = drone_height + 2 * drone.rect.height * row_number

        # ...then finally add that drone to the Group object.
        self.drones.add(drone)


    def _create_fleet(self):
        """Create the fleet of drones."""

        drone = Drone(self)
        drone_width, drone_height = drone.rect.size

        # Here we define the available screen space for our drone rows,
        # including space on either side of the fleet equal to the width of 1 drone.
        available_space_x = self.settings.screen_width - (2 * drone_width)

        # Next we calculate the total number of possible drones for a row of drones.
        # The '//' operator is for Floor Division. which drops any remainder (leaving an integer).
        # We multiply drone width by 2 to account for equivalent space between each drone.
        number_drones_x = available_space_x // (2 * drone_width)

        shuttle_height = self.shuttle.rect.height

        # Now we will define the total available screen space for multiple rows of drones,
        # leaving some space (breathing room) between the shuttle and the closest row of drones.
        available_space_y = (self.settings.screen_height - (3 * drone_height) - 2 * shuttle_height)

        # We can calculate the total number of rows we can have,
        # including equal vertical space between rows,
        # by dividing the available space by 2 x drone height.
        number_rows = available_space_y // (2 * drone_height)

        # We create a loop here that counts from 0 to the number of vertical rows we can make,
        # 
        # creating a drone object from our "Drone()"" class,
        # using our "_create_drone()" method on each element.
        for row_number in range(number_rows):
            for drone_number in range(number_drones_x):
                self._create_drone(drone_number, row_number)


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""

        self.screen.fill(self.settings.bg_color)
        self.shuttle.blitme()

        # Calling the "draw_bullet" method we wrote in the "Bullet()"" class
        # for each bullet in the Group (see "bullet.py" module).
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # When we call 'draw()' on a 'Group' object in Pygame,
        # Pygame draws each element in the Group at the position
        # defined by its 'rect' attribute.
        # This method requires a single arg: a surface
        # upon which to draw elements from the group.
        self.drones.draw(self.screen)

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':

    # Make a game instance and run the game.
    da = DronesAttack()
    da.run_game()