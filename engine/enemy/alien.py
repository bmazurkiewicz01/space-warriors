import pygame

from engine.weapon.laser.lasersprite import LaserSprite


class Alien(pygame.sprite.Sprite):
    """
    A class representing an alien in the game.

    Attributes:
    image (pygame.Surface): The surface representing the alien.
    rect (pygame.Rect): The rect representing the position of the alien.
    """

    def __init__(self, x, y):
        """
        Initializes an alien object.
        Load the image file, set the rect attribute to a Rect object with top-left corner at (x, y).

        Parameters:
        x (int): The x-coordinate of the top-left corner of the alien.
        y (int): The y-coordinate of the top-left corner of the alien.
        """
        super().__init__()
        self.image = pygame.image.load("resources/alien.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, direction):
        """
        Update the position of the Alien.

        Parameters:
        direction (int): The direction and amount to move the Alien on the x-axis.
        """
        self.rect.x += direction

    def prepare_laser(self, screen_height):
        """
        Prepare a LaserSprite instance for the Alien.

        Parameters:
        screen_height (int): The height of the screen.

        Returns:
        LaserSprite: A LaserSprite instance initialized with the center of the Alien as its starting position,
        the screen height as its ending position, the color (55, 128, 255), and a speed of -10.
        """
        laser_sprite = LaserSprite(self.rect.center, screen_height, (55, 128, 255), -10)
        return laser_sprite
