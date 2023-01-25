from abc import abstractmethod, ABC

import pygame


class Weapon(ABC):
    def __init__(self, cooldown, height):
        # Weapon attributes
        self.__is_weapon_available = True
        self.__time = 0
        self.__cooldown = cooldown
        self.__height = height

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

    def __load_weapon(self):
        if not self.__is_weapon_available:
            end_time = pygame.time.get_ticks()
            if end_time - self.__time >= self.__cooldown:
                self.__is_weapon_available = True

    @abstractmethod
    def shoot_weapon(self, player_position):
        pass

    def refresh_weapon(self):
        self.__load_weapon()
        self.__weapon_shots.update()
