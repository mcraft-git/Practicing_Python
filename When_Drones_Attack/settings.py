
class Settings:
    """A class to store all settings for When Drones Attack."""

    def __init__(self):
        """Initialize the game's settings."""

        # Screen settings.
        self.screen_width = 1600
        self.screen_height = 1024
        self.bg_color = (19,2,2)

        # Shuttle settings.
        self.shuttle_speed = 1.2

        # Bullet settings.
        self.bullet_speed = 1.0
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 5