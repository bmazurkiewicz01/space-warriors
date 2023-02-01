import pygame
from engine.weapon.cannon.cannon import Cannon
from engine.weapon.laser.laser import Laser


class Player(pygame.sprite.Sprite):
    """
    A class representing the player in the game.

    Attributes:
        image (pygame.Surface): Surface of the player's image.
        rect (pygame.Rect): Rectangle surrounding the player's image.
        __screen (pygame.Surface): Surface of the game screen.
        __health (int): Health of the player.
        __score (int): Score of the player.
        __screen_width (int): Width of the game screen.
        __screen_height (int): Height of the game screen.
        __speed (int): Speed of the player.
        __weapons (List[Cannon, Laser]): List of weapons used by the player.
        __laser_sound (pygame.mixer.Sound): Sound of the laser.
        __cannon_sound (pygame.mixer.Sound): Sound of the cannon.

    Args:
        player_position (Tuple[int, int]): Initial position of the player.
        screen_width (int): Width of the game screen.
        screen_height (int): Height of the game screen.
        speed (int): Speed of the player.
        screen (pygame.Surface): Surface of the game screen.
    """
    def __init__(self, player_position, screen_width, screen_height, speed, screen):
        """
        Initialize player's attributes, weapons and sounds.
        """
        # Initialization of player
        super().__init__()
        self.image = pygame.image.load("resources/spaceship1.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom=player_position)
        self.__screen = screen
        self.__health = 100
        self.__score = 0

        # Player movement attributes
        self.__screen_width = screen_width
        self.__screen_height = screen_height
        self.__speed = speed

        # Create weapons objects
        self.__weapons = [Cannon(3000, screen_height, "Cannon"), Laser(600, screen_height, "Red Laser", (255, 0, 0)),
                          Laser(600, screen_height, "Blue Laser", (0, 0, 255))]

        # Laser sound
        self.__laser_sound = pygame.mixer.Sound("audio/laser.wav")
        self.__laser_sound.set_volume(0.4)

        # Cannon sound
        self.__cannon_sound = pygame.mixer.Sound("audio/cannon_shoot.wav")
        self.__cannon_sound.set_volume(0.6)

    @property
    def health(self):
        """Get the current health value of the player."""
        return self.__health

    @health.setter
    def health(self, new_value):
        """Set a new value for the player's health."""
        self.__health = new_value

    @property
    def weapons(self):
        """Get a list of all the weapons currently equipped by the player."""
        return self.__weapons

    @property
    def score(self):
        """Get the current score of the player."""
        return self.__score

    @score.setter
    def score(self, new_value):
        """Set a new value for the player's score."""
        self.__score = new_value

    def __get_user_input(self):
        """Handle all the user inputs for player's movement and weapon activation."""
        keys = pygame.key.get_pressed()

        # Movement event handler
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.x -= self.__speed
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x += self.__speed

        # Cannon event handler
        if (keys[pygame.K_SPACE]) and self.__weapons[0].is_weapon_available:
            self.__cannon_sound.play()
            self.__weapons[0].shoot_weapon((self.rect.centerx, self.rect.centery - 64))
            self.__weapons[0].is_weapon_available = False
            self.__weapons[0].time = pygame.time.get_ticks()
        if (keys[pygame.K_q]) and self.__weapons[1].is_weapon_available:
            self.__weapons[1].shoot_weapon((self.rect.centerx - 51.5, self.rect.centery - 32))
            self.__weapons[1].is_weapon_available = False
            self.__weapons[1].time = pygame.time.get_ticks()
            self.__laser_sound.play()
        if (keys[pygame.K_e]) and self.__weapons[2].is_weapon_available:
            self.__weapons[2].shoot_weapon((self.rect.centerx + 51.5, self.rect.centery - 32))
            self.__weapons[2].is_weapon_available = False
            self.__weapons[2].time = pygame.time.get_ticks()
            self.__laser_sound.play()

    def __adjust_player_position(self):
        """
        Adjusts the player's position on the screen to ensure that it stays within the bounds of the screen.
        """
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.__screen_width:
            self.rect.right = self.__screen_width

    def __render_health_bar(self, percentage_complete, x, y, width, height, bar_color, empty_bar_color):
        """
        Renders the health bar of the player.

        :param percentage_complete: float representing the percentage of health remaining
        :param x: int x-coordinate of the health bar on the screen
        :param y: int y-coordinate of the health bar on the screen
        :param width: int width of the health bar
        :param height: int height of the health bar
        :param bar_color: tuple representing RGB values of the filled part of the bar
        :param empty_bar_color: tuple representing RGB values of the empty part of the bar
        """
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

    def __display_score(self):
        """
        Displays the current score of the player on the screen.
        """
        font = pygame.font.Font(None, 30)
        health_name_text = font.render(f"Score: {self.__score}", True, (255, 255, 255))
        text_rect = health_name_text.get_rect()
        text_rect.x = 10
        text_rect.y = 10
        self.__screen.blit(health_name_text, text_rect)

    def update(self):
        """
        Updates the player's status, including getting user input, adjusting player's position, rendering health bar,
        displaying score, and refreshing weapons status.
        """
        # Refresh player status
        self.__get_user_input()
        self.__adjust_player_position()
        self.__render_health_bar(self.__health / 100, 10, self.__screen_height - 30, 100, 20, (255, 0, 100),
                                 (255, 255, 255))
        self.__display_score()

        # Refresh weapons status
        self.__weapons[0].refresh_weapon(self.__screen, 120, self.__screen_height - 30, (169, 169, 169),
                                         (255, 255, 255))
        self.__weapons[1].refresh_weapon(self.__screen, self.__screen_width - 220, self.__screen_height - 30,
                                         (255, 0, 0), (255, 255, 255))
        self.__weapons[2].refresh_weapon(self.__screen, self.__screen_width - 110, self.__screen_height - 30,
                                         (0, 0, 255), (255, 255, 255))
