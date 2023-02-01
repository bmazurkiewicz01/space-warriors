import pygame


class CannonBall(pygame.sprite.Sprite):
    """
    A class representing a CannonBall in a pygame environment.

    Attributes:
        image (pygame.Surface): The image of the CannonBall.
        rect (pygame.Rect): The rectangle object that defines the size and position of the CannonBall.
        __speed (int): The speed at which the CannonBall travels.
        screen_height (int): The height of the screen.
    """

    def __init__(self, cannonball_position, screen_height, speed=7):
        """
          Initializes a CannonBall instance.

          Args:
              cannonball_position (tuple): The initial position of the CannonBall in (x, y) format.
              screen_height (int): The height of the screen.
              speed (int, optional): The speed at which the CannonBall travels. Defaults to 7.
        """
        super().__init__()
        self.image = pygame.image.load("resources/cannonball.png").convert_alpha()
        self.rect = self.image.get_rect(center=cannonball_position)
        self.__speed = speed
        self.screen_height = screen_height

    def __destroy_cannonball(self):
        """
        Destroys the CannonBall if it goes beyond the screen boundaries.
        """
        if self.rect.y <= -50 or self.rect.y >= self.screen_height + 30:
            self.kill()

    def update(self):
        """
        Updates the position of the CannonBall by subtracting its speed from the y-coordinate.
        """
        self.rect.y -= self.__speed
        self.__destroy_cannonball()
