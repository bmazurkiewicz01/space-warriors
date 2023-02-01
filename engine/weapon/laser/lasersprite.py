import pygame


class LaserSprite(pygame.sprite.Sprite):
    """
    A class to represent a laser sprite in a game. The laser sprite is a rect-shaped object that moves vertically
    on the screen.

    Attributes:
        image (pygame.Surface): The Surface object representing the laser sprite.
        rect (pygame.Rect): The Rect object representing the bounding box of the laser sprite.
        __speed (int): The speed at which the laser sprite moves vertically on the screen.
        screen_height (int): The height of the screen on which the laser sprite is displayed.
    """
    def __init__(self, laser_position, screen_height, color, speed=15):
        """
        The constructor for the LaserSprite class.

        Args:
            laser_position (tuple): A tuple representing the (x, y) position of the laser sprite.
            screen_height (int): The height of the screen on which the laser sprite is displayed.
            color (tuple): A tuple representing the RGB color of the laser sprite.
            speed (int): The speed at which the laser sprite moves vertically on the screen. Defaults to 15.

        """
        super().__init__()
        self.image = pygame.Surface((4, 20))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=laser_position)
        self.__speed = speed
        self.screen_height = screen_height

    def __destroy_laser(self):
        """
        A helper method to remove the laser sprite from the game when it goes out of the screen.
        """
        if self.rect.y <= -50 or self.rect.y >= self.screen_height + 30:
            self.kill()

    def update(self):
        """
        A method that updates the position of the laser sprite on the screen. The laser sprite moves vertically
        up at a rate determined by the speed attribute. If the laser sprite goes out of the screen, it is removed
        from the game using the __destroy_laser() method.
        """
        self.rect.y -= self.__speed
        self.__destroy_laser()
