import pygame
import sys

from engine.enemy.block import obstacle_shape, Block
from engine.menu.menu import MainMenu
from engine.player import Player


class GameManager:
    def __init__(self, width, height) -> None:
        # Initialize pygame window
        pygame.init()
        pygame.display.set_caption("Space Warriors")
        pygame.display.set_icon(pygame.image.load("resources/icon.png"))

        # Initialize GameManager attributes
        self.__is_running = True
        self.__width = width
        self.__height = height
        self.__screen = pygame.display.set_mode((width, height))
        self.__clock = pygame.time.Clock()

        # Player handler variables
        self.__player = 0
        self.__player_sprite = 0

        # Create a MainMenu object to handle game states
        self.__main_menu = MainMenu(self.__screen, width, height)

        # Initialize obstacles
        self.__obstacle_shape = obstacle_shape
        self.__block_size = 13
        self.__blocks = pygame.sprite.Group()
        obstacle_amount = 6
        obstacle_offsets = [num * (self.__width / obstacle_amount) for num in range(obstacle_amount)]
        self.__create_obstacles(self.__width / 25, 650, *obstacle_offsets)

    def run(self) -> None:
        # Main game loop
        while self.__is_running:
            self.__screen.fill((30, 30, 30))

            # Check current game state
            if self.__main_menu.is_play_clicked:
                if self.__main_menu.new_game:
                    self.__initialize_player()
                    self.__main_menu.new_game = False
                    pygame.time.wait(100)
                self.__player_handler()
                self.__enemy_handler()
            else:
                self.__main_menu.run()

            # Event handler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__is_running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.__main_menu.is_play_clicked = False

            # Refresh screen
            pygame.display.update()
            self.__clock.tick(60)

    def __initialize_player(self):
        self.__player = Player((self.__width / 2, self.__height - 80), self.__width, self.__height, 10, self.__screen)
        self.__player_sprite = pygame.sprite.GroupSingle(self.__player)

    def __player_handler(self):
        self.__player_sprite.update()
        self.__player_sprite.draw(self.__screen)
        for weapon in self.__player.weapons:
            weapon.weapon_shots.draw(self.__screen)

    def __enemy_handler(self):
        self.__blocks.draw(self.__screen)

    def __create_obstacle(self, x_start, y_start, x_offset):
        for row_index, row in enumerate(self.__obstacle_shape):
            for column_index, column in enumerate(row):
                if column == 'x':
                    x = ((column_index * self.__block_size) + x_start) + x_offset
                    y = (row_index * self.__block_size) + y_start
                    block = Block(self.__block_size, (255, 90, 90), x, y)
                    self.__blocks.add(block)

    def __create_obstacles(self, x_start, y_start, *offset):
        for x_offset in offset:
            self.__create_obstacle(x_start, y_start, x_offset)
