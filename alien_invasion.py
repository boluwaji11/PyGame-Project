import sys
import pygame

from settings import Settings

# Create the Alien Invasion class
# Overall class to manage game assets and behavior
class AlienInvasion:
    # Initializes background settings
    def __init__(self):
        pygame.init()
        self.settings = Settings()  # An instance of the Settings class

        # Set screen size and game title
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        # Set the background color
        # self.bg_color = (230, 230, 230) # Not needed since already initialized in the Settings module

    # Create the function to start the main loop for the game
    def run_game(self):
        while True:
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()  # To quit the game

            # Redraw the screen during each pass through the loop.
            # Fill the screen with the background color
            self.screen.fill(self.settings.bg_color)

            # Make the most recently drawn screen visible
            pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
