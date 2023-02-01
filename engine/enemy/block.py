import pygame

obstacle_shape = [
    '   xxxxxxx   ',
    '  xxxxxxxxx  ',
    ' xxxxxxxxxxx ',
    'xxxxxxxxxxxxx',
    'xxxxxxxxxxxxx',
    'xxxxxx xxxxxx',
    ' xxxxx xxxxx ',
    ' xxx     xxx ',
    ' xx       xx '
]


class Block(pygame.sprite.Sprite):
    """
    A class representing a block in the game.

    Attributes:
    image (pygame.Surface): The surface representing the block.
    rect (pygame.Rect): The rect representing the position of the block.
    """

    def __init__(self, size, color, x, y):
        """
        Initializes a block object.

        Parameters:
        size (int): The size of the block in pixels.
        color (tuple): The color of the block in RGB format.
        x (int): The x-coordinate of the top-left corner of the block.
        y (int): The y-coordinate of the top-left corner of the block.
        """
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))
