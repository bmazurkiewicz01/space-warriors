import pygame
from abc import abstractmethod, ABC


class Weapon(ABC):
    """
    The Weapon class is an abstract base class representing a weapon.

    Attributes:
    __is_weapon_available (bool): A boolean value indicating whether the weapon is available or not.
    __time (int): The time at which the weapon was last used.
    __cooldown (int): The time it takes for the weapon to reload after being used.
    __height (int): The height of the weapon.
    __weapon_name (str): The name of the weapon.
    __weapon_shots (pygame.sprite.Group): A group of shot objects.

    Methods:
    __render_loading_bar(percentage_complete, screen, x, y, width, height, bar_color, empty_bar_color): Renders a loading bar on the screen to indicate the reload progress of the weapon.
    __load_weapon(screen, bar_x, bar_y, bar_color, empty_bar_color): Loads the weapon and updates the reload progress on the screen.
    shoot_weapon(player_position): Abstract method to shoot the weapon. Must be implemented by subclasses.
    refresh_weapon(screen, bar_x, bar_y, bar_color, empty_bar_color): Refreshes the weapon by loading it and updating its shots.
    """
    def __init__(self, cooldown, height, weapon_name):
        """
        Initialize the Weapon class with the following parameters:

        Parameters:
        cooldown (int): Time it takes to reload the weapon.
        height (int): The height of the weapon on the screen.
        weapon_name (str): The name of the weapon.
        """
        # Weapon attributes
        self.__is_weapon_available = True
        self.__time = 0
        self.__cooldown = cooldown
        self.__height = height
        self.__weapon_name = weapon_name

        self.__weapon_shots = pygame.sprite.Group()

    @property
    def time(self):
        """
        Get the current time of the weapon.
        """
        return self.__time

    @time.setter
    def time(self, new__time):
        """
        Set the new time for the weapon.

        Parameters:
        new__time (int): The new time for the weapon.
        """
        self.__time = new__time

    @property
    def is_weapon_available(self):
        """
        Check if the weapon is available.
        """
        return self.__is_weapon_available

    @is_weapon_available.setter
    def is_weapon_available(self, new_value):
        """
        Set the availability of the weapon.

        Parameters:
        new_value (bool): The new availability status of the weapon.
        """
        self.__is_weapon_available = new_value

    @property
    def weapon_shots(self):
        """
        Get the group of shots fired by the weapon.
        """
        return self.__weapon_shots

    def __render_loading_bar(self, percentage_complete, screen, x, y, width, height, bar_color, empty_bar_color):
        """
        Render the loading bar for the weapon.

        Parameters:
        percentage_complete (float): The percentage of the reload process completed.
        screen (pygame.Surface): The screen on which to render the loading bar.
        x (int): The x-coordinate of the loading bar on the screen.
        y (int): The y-coordinate of the loading bar on the screen.
        width (int): The width of the loading bar.
        height (int): The height of the loading bar.
        bar_color (tuple): The color of the filled part of the loading bar.
        empty_bar_color (tuple): The color of the empty part of the loading bar.
        """
        # Render loading bar
        filled_width = int(width * percentage_complete)
        empty_width = width - filled_width
        filled_bar = pygame.Rect(x, y, filled_width, height)
        empty_bar = pygame.Rect(x + filled_width, y, empty_width, height)
        pygame.draw.rect(screen, bar_color, filled_bar)
        pygame.draw.rect(screen, empty_bar_color, empty_bar)

        # Render weapon name text
        font = pygame.font.Font(None, 30)
        weapon_name_text = font.render(self.__weapon_name, True, (255, 255, 255))
        text_rect = weapon_name_text.get_rect()
        text_rect.x = x
        text_rect.y = y - 25
        screen.blit(weapon_name_text, text_rect)

    def __load_weapon(self, screen, bar_x, bar_y, bar_color, empty_bar_color):
        """
        Load the weapon, updating its availability and rendering the loading bar.

        Parameters:
        screen (pygame.Surface): The screen on which to render the loading bar.
        bar_x (int): The x-coordinate of the loading bar on the screen.
        bar_y (int): The y-coordinate of the loading bar on the screen.
        bar_color (tuple): The color of the filled part of the loading bar.
        empty_bar_color (tuple): The color of the empty part of the loading bar.
        """
        if self.__is_weapon_available:
            self.__render_loading_bar(1, screen, bar_x, bar_y, 100, 20, bar_color, empty_bar_color)
        else:
            end_time = pygame.time.get_ticks()
            elapsed_time = end_time - self.__time
            percentage_complete = elapsed_time / self.__cooldown
            self.__render_loading_bar(percentage_complete, screen, bar_x, bar_y, 100, 20, bar_color, empty_bar_color)
            if elapsed_time >= self.__cooldown:
                self.__is_weapon_available = True

    @abstractmethod
    def shoot_weapon(self, player_position):
        """
        Abstract method for shooting the weapon. To be implemented by a subclass.

        Parameters:
        player_position (tuple): The position of the player.
        """
        pass

    def refresh_weapon(self, screen, bar_x, bar_y, bar_color, empty_bar_color):
        """
        Refreshes the weapon, loading the weapon if necessary and updating the weapon shots.

        Parameters:
        screen (pygame.Surface): The game screen.
        bar_x (int): X position of the loading bar on the screen.
        bar_y (int): Y position of the loading bar on the screen.
        bar_color (tuple): RGB color code of the filled bar.
        empty_bar_color (tuple): RGB color code of the empty bar.

        Returns:
        None
        """
        self.__load_weapon(screen, bar_x, bar_y, bar_color, empty_bar_color)
        self.__weapon_shots.update()
