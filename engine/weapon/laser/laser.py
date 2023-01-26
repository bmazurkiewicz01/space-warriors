from engine.weapon.laser.lasersprite import LaserSprite
from engine.weapon.weapon import Weapon


class Laser(Weapon):
    def __init__(self, laser_cooldown, screen_height, weapon_name, color, speed=15):
        super().__init__(laser_cooldown, screen_height, weapon_name)
        self.__color = color
        self.__speed = speed

    def shoot_weapon(self, position):
        self._Weapon__weapon_shots.add(LaserSprite(position, self._Weapon__height, self.__color, self.__speed))
