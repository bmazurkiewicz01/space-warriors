from engine.weapon.cannon.cannonball import CannonBall
from engine.weapon.weapon import Weapon


class Cannon(Weapon):
    """
    This class represents a Cannon Weapon. It is a subclass of the Weapon class and inherits all its attributes and methods.

    Attributes:
    cannon_cooldown (int): Represents the time interval between two consecutive shots from the Cannon.
    screen_height (int): Represents the height of the screen where the game is being played.
    weapon_name (str): Represents the name of the weapon.

    Methods:
    shoot_weapon(player_position): This method shoots a CannonBall object from the player's current position.
    """

    def __init__(self, cannon_cooldown, screen_height, weapon_name):
        """
        This is the constructor for the Cannon class. It initializes the Cannon object by calling the parent class's constructor and passing the parameters.

        Parameters:
        cannon_cooldown (int): Represents the time interval between two consecutive shots from the Cannon.
        screen_height (int): Represents the height of the screen where the game is being played.
        weapon_name (str): Represents the name of the weapon.
        """
        super().__init__(cannon_cooldown, screen_height, weapon_name)

    def shoot_weapon(self, player_position):
        """
        This method creates and adds a new CannonBall object to the array of weapon_shots.

        Parameters:
        player_position (tuple): Represents the player's current position (x, y) from where the CannonBall is being shot.

        """
        self._Weapon__weapon_shots.add(CannonBall(player_position, self._Weapon__height))
