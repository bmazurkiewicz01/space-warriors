import pygame
from random import choice

from engine.enemy.alien import Alien
from engine.enemy.block import obstacle_shape, Block
from engine.weapon.laser.laser import Laser


class Level:
    def __init__(self, screen, width, height, obstacle_amount=6, alien_rows=6, alien_columns=8):
        # Initialize level attributes
        self.__screen = screen
        self.__width = width
        self.__height = height
        self.__alien_rows = alien_rows
        self.__alien_columns = alien_columns

        self.__is_level_locked = False
        self.__is_level_finished = False

        # Initialize obstacles
        self.__obstacle_shape = obstacle_shape
        self.__block_size = 13
        self.__blocks = pygame.sprite.Group()
        self.__obstacle_amount = obstacle_amount
        obstacle_offsets = [num * (self.__width / obstacle_amount) for num in range(obstacle_amount)]
        self.__create_obstacles(self.__width / 25, 650, *obstacle_offsets)

        # Initialize aliens
        self.__alien_direction = 2
        self.__aliens = pygame.sprite.Group()
        self.__aliens_weapons = pygame.sprite.Group()

    @property
    def is_level_locked(self):
        return self.__is_level_locked

    @is_level_locked.setter
    def is_level_locked(self, new_value):
        self.__is_level_locked = new_value

    @property
    def is_level_finished(self):
        return self.__is_level_finished

    @is_level_finished.setter
    def is_level_finished(self, new_value):
        self.__is_level_finished = new_value

    def enemy_handler(self):
        self.__blocks.draw(self.__screen)
        self.__aliens.draw(self.__screen)
        self.__aliens.update(self.__alien_direction)
        self.__adjust_alien_position()

        self.__aliens_weapons.update()
        self.__aliens_weapons.draw(self.__screen)

    def alien_attack(self):
        self.__alien_shoot()

    def __create_obstacles(self, x_start, y_start, *offset):
        for x_offset in offset:
            for row_index, row in enumerate(self.__obstacle_shape):
                for column_index, column in enumerate(row):
                    if column == 'x':
                        x = ((column_index * self.__block_size) + x_start) + x_offset
                        y = (row_index * self.__block_size) + y_start
                        block = Block(self.__block_size, (255, 90, 90), x, y)
                        self.__blocks.add(block)

    def initialize_aliens(self, x_offset=100, y_offset=80, x_start=70, y_start=60):
        for row_index, row in enumerate(range(self.__alien_rows)):
            for column_index, column in enumerate(range(self.__alien_columns)):
                x = column_index * x_offset + x_start
                y = row_index * y_offset + y_start
                alien = Alien(x, y)
                self.__aliens.add(alien)

    def __adjust_alien_position(self):
        if self.__aliens.sprites():
            for alien in self.__aliens.sprites():
                if alien.rect.right >= self.__width:
                    self.__alien_direction = -2
                    self.__alien_move_down(2)
                elif alien.rect.left <= 0:
                    self.__alien_direction = 2
                    self.__alien_move_down(2)

    def __alien_move_down(self, distance):
        if self.__aliens.sprites():
            for alien in self.__aliens.sprites():
                alien.rect.y += distance

    def __alien_shoot(self):
        if self.__aliens.sprites():
            alien = choice(self.__aliens.sprites())
            self.__aliens_weapons.add(alien.prepare_laser(self.__height))
