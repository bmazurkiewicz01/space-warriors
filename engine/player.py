import pygame
from engine.cannon.cannon import Cannon


class Player(pygame.sprite.Sprite):
    def __init__(self, player_position, screen_width, screen_height, speed):
        # Initialization of player
        super().__init__()
        self.image = pygame.image.load("resources/spaceship1.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom=player_position)

        # Player movement attributes
        self.__screen_width = screen_width
        self.__screen_height = screen_height
        self.__speed = speed

        # Create cannon object
        self.__cannon = Cannon(2000, screen_height)

    @property
    def cannon(self):
        return self.__cannon

    def __get_user_input(self):
        keys = pygame.key.get_pressed()

        # Movement event handler
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.x -= self.__speed
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x += self.__speed

        # Cannon event handler
        if keys[pygame.K_SPACE] and self.__cannon.is_cannon_available:
            self.__cannon.shoot_cannon(self.rect.center)
            self.__cannon.is_cannon_available = False
            self.__cannon.cannon_time = pygame.time.get_ticks()

    def __adjust_player_position(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.__screen_width:
            self.rect.right = self.__screen_width

    def update(self):
        self.__get_user_input()
        self.__adjust_player_position()
        self.__cannon.refresh_cannon()
