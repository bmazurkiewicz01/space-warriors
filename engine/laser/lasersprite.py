import pygame


class LaserSprite(pygame.sprite.Sprite):
    def __init__(self, laser_position, screen_height, color, speed=15):
        super().__init__()
        self.image = pygame.Surface((4, 20))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=laser_position)
        self.__speed = speed
        self.screen_height = screen_height

    def __destroy_laser(self):
        if self.rect.y <= -50 or self.rect.y >= self.screen_height + 30:
            self.kill()

    def update(self):
        self.rect.y -= self.__speed
        self.__destroy_laser()
