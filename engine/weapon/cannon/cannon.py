from engine.weapon.cannon.cannonball import CannonBall
from engine.weapon.weapon import Weapon


class Cannon(Weapon):
    def __init__(self, cannon_cooldown, screen_height, weapon_name):
        super().__init__(cannon_cooldown, screen_height, weapon_name)

    def shoot_weapon(self, player_position):
        self._Weapon__weapon_shots.add(CannonBall(player_position, self._Weapon__height))
