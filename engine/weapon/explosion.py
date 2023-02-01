import pygame


class Explosion(pygame.sprite.Sprite):
    """
    A class representing an explosion in a game.

    This class extends the pygame.sprite.Sprite class and is used to represent
    an explosion in a game. It uses a series of images to simulate the explosion
    animation.

    Attributes:
        __images_list (list): A list of images used to animate the explosion.
        __current_index (int): The current index in the __images_list to display.
        image (pygame.Surface): The current image to display for the explosion.
        rect (pygame.Rect): The rectangle representing the position and size of the explosion.
        __counter (int): A counter to keep track of how many update cycles have passed.
        __explosion_speed (int): The number of update cycles between each change in the explosion animation.
    """

    def __init__(self, x, y, explosion_speed=10, image_path="resources/exp", scale=(150, 150)):
        """
        Initialize a new explosion.

        Args:
            x (int): The x-coordinate of the center of the explosion.
            y (int): The y-coordinate of the center of the explosion.
            explosion_speed (int, optional): The number of update cycles between each change in the explosion animation. Defaults to 10.
            image_path (str, optional): The path to the directory containing the explosion images. Defaults to "resources/exp".
            scale (tuple, optional): The size to scale the explosion images to. Defaults to (150, 150).
        """
        super().__init__()
        self.__images_list = []
        for image_number in range(1, 6):
            image = pygame.image.load(f"{image_path}{image_number}.png")
            image = pygame.transform.scale(image, scale)
            self.__images_list.append(image)
        self.__current_index = 0
        self.image = self.__images_list[self.__current_index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.__counter = 0
        self.__explosion_speed = explosion_speed

    def update(self):
        """
        Update the state of the explosion.

        This method updates the state of the explosion by incrementing the counter,
        updating the current image to display based on the counter, and killing the
        explosion once the animation is complete.
        """
        self.__counter += 1

        if self.__counter >= self.__explosion_speed and self.__current_index < len(self.__images_list) - 1:
            self.__counter = 0
            self.__current_index += 1
            self.image = self.__images_list[self.__current_index]
        if self.__current_index >= len(self.__images_list) - 1 and self.__counter >= self.__explosion_speed:
            self.kill()
