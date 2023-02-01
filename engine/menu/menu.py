import pygame
import sys
from engine.menu.button import Button


class MainMenu:
    """
    The MainMenu class creates the main menu display and handles interactions with it.

    Attributes:
        __screen (pygame.Surface): The surface on which the main menu is displayed.
        __font (pygame.font.Font): The font used to display text in the main menu.
        __play_button (Button): The play button displayed in the main menu.
        __quit_button (Button): The quit button displayed in the main menu.
        __width (int): The width of the main menu screen.
        __height (int): The height of the main menu screen.
        __is_play_clicked (bool): A flag to determine if the play button has been clicked.
        __new_game (bool): A flag to determine if a new game has been started.

    Properties:
        is_play_clicked: A flag to determine if the play button has been clicked.
        new_game: A flag to determine if a new game has been started.
    """
    def __init__(self, screen, width, height):
        """
        Initializes the main menu with the given screen surface, width, and height.

        Args:
            screen (pygame.Surface): The surface on which the main menu is displayed.
            width (int): The width of the main menu screen.
            height (int): The height of the main menu screen.
        """
        self.__screen = screen
        self.__font = pygame.font.SysFont("arialblack", 100)
        self.__play_button = 0
        self.__quit_button = 0
        self.__width = width
        self.__height = height
        self.__initialize_buttons()
        self.__is_play_clicked = False
        self.__new_game = False

    @property
    def is_play_clicked(self):
        """
        Property that returns the value of the private attribute `__is_play_clicked`
        """
        return self.__is_play_clicked

    @is_play_clicked.setter
    def is_play_clicked(self, new_value):
        """
        Property setter that sets the value of the private attribute `__is_play_clicked`
        """
        self.__is_play_clicked = new_value

    @property
    def new_game(self):
        """
        Property that returns the value of the private attribute `__new_game`
        """
        return self.__new_game

    @new_game.setter
    def new_game(self, new_value):
        """
        Property setter that sets the value of the private attribute `__new_game`
        """
        self.__new_game = new_value

    def __initialize_buttons(self):
        """
        Initializes the play and quit buttons in the main menu.
        """
        self.__play_button = Button(image=pygame.image.load("resources/play_btn.png"), pos=(self.__width / 2, self.__height / 2 - 100),
                             text_input="PLAY", font=self.__font, base_color="White", hovering_color="#d7fcd4")
        self.__quit_button = Button(image=pygame.image.load("resources/quit_btn.png"), pos=(self.__width / 2, self.__height / 2 + 100),
                             text_input="QUIT", font=self.__font, base_color="White", hovering_color="#d7fcd4")

    def run(self):
        """
        Handles interactions in the main menu and updates the screen accordingly.
        """
        while not self.__is_play_clicked:
            self.__screen.fill((30, 30, 30))

            menu_mouse_pos = pygame.mouse.get_pos()

            menu_text = self.__font.render("SPACE WARRIORS", True, "#d7ffa6")
            menu_rect = menu_text.get_rect(center=(self.__width / 2, self.__height / 2 - 300))

            self.__screen.blit(menu_text, menu_rect)

            for button in [self.__play_button, self.__quit_button]:
                button.change_color(menu_mouse_pos)
                button.update(self.__screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.__play_button.check_for_input(menu_mouse_pos):
                        self.__is_play_clicked = True
                        self.__new_game = True
                    if self.__quit_button.check_for_input(menu_mouse_pos):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()
