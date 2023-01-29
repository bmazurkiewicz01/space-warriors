import pygame
from engine.weapon.cannon.cannon import Cannon
from engine.weapon.laser.laser import Laser


class Player(pygame.sprite.Sprite):
    def __init__(self, player_position, screen_width, screen_height, speed, screen):
        # Initialization of player
        super().__init__()
        self.image = pygame.image.load("resources/spaceship1.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom=player_position)
        self.__screen = screen
        self.__health = 100

        # Player movement attributes
        self.__screen_width = screen_width
        self.__screen_height = screen_height
        self.__speed = speed

        # Create weapons objects
        self.__weapons = [Cannon(3000, screen_height, "Cannon"), Laser(1200, screen_height, "Red Laser", (255, 0, 0)),
                          Laser(1200, screen_height, "Blue Laser", (0, 0, 255))]

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, new_value):
        self.__health = new_value

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

    def __render_health_bar(self, percentage_complete, x, y, width, height, bar_color, empty_bar_color):
        # Render health bar
        filled_width = int(width * percentage_complete)
        empty_width = width - filled_width
        filled_bar = pygame.Rect(x, y, filled_width, height)
        empty_bar = pygame.Rect(x + filled_width, y, empty_width, height)
        pygame.draw.rect(self.__screen, bar_color, filled_bar)
        pygame.draw.rect(self.__screen, empty_bar_color, empty_bar)

        # Render health name text
        font = pygame.font.Font(None, 30)
        health_name_text = font.render("Health", True, (255, 255, 255))
        text_rect = health_name_text.get_rect()
        text_rect.x = x
        text_rect.y = y - 25
        self.__screen.blit(health_name_text, text_rect)

    def update(self):
        # Refresh player status
        self.__get_user_input()
        self.__adjust_player_position()
        self.__render_health_bar(self.__health / 100, 10, self.__screen_height - 30, 100, 20, (255, 0, 100), (255, 255, 255))

        # Refresh weapons status
        self.__weapons[0].refresh_weapon(self.__screen, 120, self.__screen_height - 30, (169, 169, 169), (255, 255, 255))
        self.__weapons[1].refresh_weapon(self.__screen, self.__screen_width - 220, self.__screen_height - 30,
                                         (255, 0, 0), (255, 255, 255))
        self.__weapons[2].refresh_weapon(self.__screen, self.__screen_width - 110, self.__screen_height - 30,
                                         (0, 0, 255), (255, 255, 255))
