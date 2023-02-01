class Button:
    """
    The Button class provides the implementation for creating a button for a user interface.

    Attributes:
    - image (pygame.Surface): The surface object to display on the button
    - x_pos (int): The x coordinate of the button center
    - y_pos (int): The y coordinate of the button center
    - font (pygame.font.Font): The font object to render the text of the button
    - base_color (tuple): The base color of the text in (R, G, B) format
    - hovering_color (tuple): The color of the text when hovering over the button in (R, G, B) format
    - text_input (str): The text to be displayed on the button
    - text (pygame.Surface): The surface object of the text on the button
    - rect (pygame.Rect): The rectangle object representing the button image
    - text_rect (pygame.Rect): The rectangle object representing the text on the button

    """
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        """
        Initializes the Button object with the provided parameters.

        Args:
        - image (pygame.Surface): The surface object to display on the button
        - pos (tuple): The position of the button center in (x, y) format
        - text_input (str): The text to be displayed on the button
        - font (pygame.font.Font): The font object to render the text of the button
        - base_color (tuple): The base color of the text in (R, G, B) format
        - hovering_color (tuple): The color of the text when hovering over the button in (R, G, B) format

        """
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        """
        Updates the button on the provided screen.

        Args:
        - screen (pygame.Surface): The surface object to update the button on.

        """
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def check_for_input(self, position):
        """
        Checks if the provided position is within the bounds of the button.

        Args:
        - position (tuple): The position to check, in (x, y) format.

        Returns:
        - bool: True if the position is within the bounds of the button, False otherwise.

        """
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            return True
        return False

    def change_color(self, position):
        """
        Changes the color of the text on the button based on the provided position.
        If the position is within the bounds of the button, the text color changes to the hovering color.
        If the position is outside the bounds of the button, the text color changes to the base color.

        Args:
        - position (tuple): The position to check, in (x, y) format.

        """
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)
