from engine.weapon.laser.lasersprite import LaserSprite
from engine.weapon.weapon import Weapon


class Laser(Weapon):
    """
    A class representing the Laser weapon in the game. This weapon extends the `Weapon` class and overrides the `shoot_weapon` method.
    The laser weapon is characterized by a unique color and speed that is set during initialization.

    Attributes:
        laser_cooldown (int): The time in milliseconds that the weapon needs to cool down between two shots.
        screen_height (int): The height of the screen.
        weapon_name (str): The name of the weapon.
        __color (tuple): The color of the laser.
        __speed (int): The speed of the laser.
    """
    def __init__(self, laser_cooldown, screen_height, weapon_name, color, speed=15):
        """
        The constructor for the Laser class.

        Args:
            laser_cooldown (int): The time in milliseconds that the weapon needs to cool down between two shots.
            screen_height (int): The height of the screen.
            weapon_name (str): The name of the weapon.
            color (tuple): The color of the laser.
            speed (int, optional): The speed of the laser. Defaults to 15.
        """
        super().__init__(laser_cooldown, screen_height, weapon_name)
        self.__color = color
        self.__speed = speed

    def shoot_weapon(self, position):
        """
        Shoot the laser weapon.

        Args:
            position (tuple): The position of the laser shot.

        Returns:
            None
        """
        self._Weapon__weapon_shots.add(LaserSprite(position, self._Weapon__height, self.__color, self.__speed))
