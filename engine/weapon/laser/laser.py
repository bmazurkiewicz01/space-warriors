from engine.weapon.laser.lasersprite import LaserSprite
from engine.weapon.weapon import Weapon


class Laser(Weapon):
    def __init__(self, laser_cooldown, screen_height, color):
        super().__init__(laser_cooldown, screen_height)
        self.__color = color

    def shoot_weapon(self, player_position):
        self._Weapon__weapon_shots.add(LaserSprite(player_position, self._Weapon__height, self.__color))
