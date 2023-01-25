import pygame
from abc import abstractmethod, ABC


class Weapon(ABC):
    def __init__(self, cooldown, height, weapon_name):
        # Weapon attributes
        self.__is_weapon_available = True
        self.__time = 0
        self.__cooldown = cooldown
        self.__height = height
        self.__weapon_name = weapon_name

        self.__weapon_shots = pygame.sprite.Group()

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, new__time):
        self.__time = new__time

    @property
    def is_weapon_available(self):
        return self.__is_weapon_available

    @is_weapon_available.setter
    def is_weapon_available(self, new_value):
        self.__is_weapon_available = new_value

    @property
    def weapon_shots(self):
        return self.__weapon_shots

    def __render_loading_bar(self, percentage_complete, screen, x, y, width, height, bar_color, empty_bar_color):
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
        pass

    def refresh_weapon(self, screen, bar_x, bar_y, bar_color, empty_bar_color):
        self.__load_weapon(screen, bar_x, bar_y, bar_color, empty_bar_color)
        self.__weapon_shots.update()
