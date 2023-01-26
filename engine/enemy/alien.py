import pygame

from engine.weapon.laser.lasersprite import LaserSprite


class Alien(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("resources/alien.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, direction):
        self.rect.x += direction

    def prepare_laser(self, screen_height):
        laser_sprite = LaserSprite(self.rect.center, screen_height, (55, 128, 255), -10)
        return laser_sprite

