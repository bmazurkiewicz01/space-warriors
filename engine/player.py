import pygame
from engine.weapon.cannon.cannon import Cannon
from engine.weapon.laser.laser import Laser


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

        # Create weapons objects
        self.__weapons = [Cannon(2000, screen_height), Laser(300, screen_height, (255, 0, 0)), Laser(300, screen_height, (0, 0, 255))]

    @property
    def weapons(self):
        return self.__weapons

    def __get_user_input(self):
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()

        # Movement event handler
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.x -= self.__speed
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x += self.__speed

        # Cannon event handler
        if (mouse == (0, 1, 0) or keys[pygame.K_SPACE]) and self.__weapons[0].is_weapon_available:
            self.__weapons[0].shoot_weapon((self.rect.centerx, self.rect.centery - 64))
            self.__weapons[0].is_weapon_available = False
            self.__weapons[0].time = pygame.time.get_ticks()
        if (mouse == (1, 0, 0) or keys[pygame.K_q]) and self.__weapons[1].is_weapon_available:
            self.__weapons[1].shoot_weapon((self.rect.centerx - 51.5, self.rect.centery - 32))
            self.__weapons[1].is_weapon_available = False
            self.__weapons[1].time = pygame.time.get_ticks()
        if (mouse == (0, 0, 1) or keys[pygame.K_e]) and self.__weapons[2].is_weapon_available:
            self.__weapons[2].shoot_weapon((self.rect.centerx + 51.5, self.rect.centery - 32))
            self.__weapons[2].is_weapon_available = False
            self.__weapons[2].time = pygame.time.get_ticks()

    def __adjust_player_position(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.__screen_width:
            self.rect.right = self.__screen_width

    def update(self):
        # Refresh player status
        self.__get_user_input()
        self.__adjust_player_position()

        # Refresh weapons status
        for weapon in self.__weapons:
            weapon.refresh_weapon()
