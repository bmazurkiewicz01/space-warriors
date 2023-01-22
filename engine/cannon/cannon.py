import pygame
from engine.cannon.cannonball import CannonBall


class Cannon:
    def __init__(self, cannon_cooldown, screen_height):
        # Cannon weapon attributes
        self.__is_cannon_available = True
        self.__cannon_time = 0
        self.__cannon_cooldown = cannon_cooldown
        self.__screen_height = screen_height

        self.__cannonballs = pygame.sprite.Group()

    @property
    def cannon_time(self):
        return self.__cannon_time

    @cannon_time.setter
    def cannon_time(self, cannon_time):
        self.__cannon_time = cannon_time

    @property
    def is_cannon_available(self):
        return self.__is_cannon_available

    @is_cannon_available.setter
    def is_cannon_available(self, new_value):
        self.__is_cannon_available = new_value

    @property
    def cannonballs(self):
        return self.__cannonballs

    def __load_cannon(self):
        if not self.__is_cannon_available:
            end_time = pygame.time.get_ticks()
            if end_time - self.__cannon_time >= self.__cannon_cooldown:
                self.__is_cannon_available = True
                print("Captain! Cannon is ready to fire!")

    def shoot_cannon(self, player_position):
        self.__cannonballs.add(CannonBall(player_position, self.__screen_height))

    def refresh_cannon(self):
        self.__load_cannon()
        self.__cannonballs.update()
