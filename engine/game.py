import pygame
import sys

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
        self.__player = Player((self.__width / 2, self.__height - 50), self.__width, self.__height, 10)
        self.__player_sprite = pygame.sprite.GroupSingle(self.__player)

    def __player_handler(self):
        self.__player_sprite.update()
        self.__player_sprite.draw(self.__screen)
        self.__player.cannon.cannonballs.draw(self.__screen)
        self.__player.red_laser.lasers.draw(self.__screen)
        self.__player.blue_laser.lasers.draw(self.__screen)
