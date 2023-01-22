import pygame
from engine.laser.lasersprite import LaserSprite


class Laser:
    def __init__(self, laser_cooldown, screen_height, color):
        # Laser weapon attributes
        self.__is_laser_available = True
        self.__laser_time = 0
        self.__laser_cooldown = laser_cooldown
        self.__screen_height = screen_height
        self.__color = color

        self.__lasers = pygame.sprite.Group()

    @property
    def laser_time(self):
        return self.__laser_time

    @laser_time.setter
    def laser_time(self, cannon_time):
        self.__laser_time = cannon_time

    @property
    def is_laser_available(self):
        return self.__is_laser_available

    @is_laser_available.setter
    def is_laser_available(self, new_value):
        self.__is_laser_available = new_value

    @property
    def lasers(self):
        return self.__lasers

    def __load_laser(self):
        if not self.__is_laser_available:
            end_time = pygame.time.get_ticks()
            if end_time - self.__laser_time >= self.__laser_cooldown:
                self.__is_laser_available = True
                print("Captain! Laser is ready to fire!")

    def shoot_laser(self, player_position):
        self.__lasers.add(LaserSprite(player_position, self.__screen_height, self.__color))

    def refresh_laser(self):
        self.__load_laser()
        self.__lasers.update()
