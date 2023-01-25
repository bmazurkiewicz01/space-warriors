import pygame


class CannonBall(pygame.sprite.Sprite):
    def __init__(self, cannonball_position, screen_height, speed=7):
        super().__init__()
        self.image = pygame.image.load("resources/cannonball.png").convert_alpha()
        self.rect = self.image.get_rect(center=cannonball_position)
        self.__speed = speed
        self.screen_height = screen_height

    def __destroy_cannonball(self):
        if self.rect.y <= -50 or self.rect.y >= self.screen_height + 30:
            self.kill()

    def update(self):
        self.rect.y -= self.__speed
        self.__destroy_cannonball()
