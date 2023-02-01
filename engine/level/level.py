import pygame
from random import choice

from engine.enemy.alien import Alien
from engine.enemy.block import obstacle_shape, Block


class Level:
    """
    This class represents a level in the game, including all elements in the level such as obstacles, aliens, and background music.

    Attributes:
        __screen (pygame.Surface): The surface to be used for displaying the game.
        __width (int): The width of the screen.
        __height (int): The height of the screen.
        __alien_rows (int): The number of rows of aliens in the level.
        __alien_columns (int): The number of columns of aliens in the level.
        __is_level_locked (bool): Whether the level is locked or not.
        __is_level_finished (bool): Whether the level is finished or not.
        __level_name (str): The name of the level.
        __obstacle_shape (list): A list of strings representing the shape of the obstacles.
        __block_size (int): The size of each obstacle block.
        __blocks (pygame.sprite.Group): A group containing all the obstacle blocks in the level.
        __obstacle_amount (int): The number of obstacles in the level.
        __alien_direction (int): The direction the aliens are moving in the level.
        __aliens (pygame.sprite.Group): A group containing all the aliens in the level.
        __aliens_weapons (pygame.sprite.Group): A group containing all the weapons the aliens have fired.
        __alien_damage (int): The damage the aliens deal.
        __alien_shooting_time (int): The time between the aliens' shots.
        __level_music (pygame.mixer.Sound): The audio for the level.
        __laser_sound (pygame.mixer.Sound): The sound for the aliens' laser.

    Methods:
        enemy_handler: Handles the display of the aliens and obstacles on the screen.
        alien_attack: Initiates an attack from the aliens.
        __create_obstacles: Helper method for creating obstacles in the level.
        initialize_aliens: Initializes the aliens in the level.

    Properties:
        is_level_locked: Whether the level is locked or not.
        is_level_finished: Whether the level is finished or not.
        alien_weapons: A group containing all the weapons the aliens have fired.
        blocks: A group containing all the obstacle blocks in the level.
        aliens: A group containing all the aliens in the level.
        alien_damage: The damage the aliens deal.
        alien_shooting_time: The time between the aliens' shots.
        game_music: The audio for the level.
        level_name: The name of the level.
    """
    def __init__(self, screen, width, height, level_name, obstacle_amount=6, alien_rows=6, alien_columns=16,
                 alien_damage=15,
                 alien_shooting_time=1200, level_audio_path="audio/game_music.wav"):
        """
        The constructor of the Level class initializes various attributes and creates obstacles and aliens.

        Attributes:
        screen (pygame.Surface): The screen where the game is displayed.
        width (int): The width of the screen.
        height (int): The height of the screen.
        level_name (str): The name of the level.
        obstacle_amount (int): The amount of obstacles in the level. Default is 6.
        alien_rows (int): The amount of rows of aliens. Default is 6.
        alien_columns (int): The amount of columns of aliens. Default is 16.
        alien_damage (int): The damage dealt by the aliens. Default is 15.
        alien_shooting_time (int): The time between alien shooting. Default is 1200.
        level_audio_path (str): The path to the audio file for the level. Default is "audio/game_music.wav".

        Class Variables:
        __screen (pygame.Surface): The screen where the game is displayed.
        __width (int): The width of the screen.
        __height (int): The height of the screen.
        __alien_rows (int): The amount of rows of aliens.
        __alien_columns (int): The amount of columns of aliens.
        __is_level_locked (bool): The status of the level, locked or not.
        __is_level_finished (bool): The status of the level, finished or not.
        __level_name (str): The name of the level.
        __obstacle_shape (str): The shape of the obstacles.
        __block_size (int): The size of the obstacles.
        __blocks (pygame.sprite.Group): A group containing all the obstacles in the level.
        __obstacle_amount (int): The amount of obstacles in the level.
        __alien_direction (int): The direction of movement of the aliens.
        __aliens (pygame.sprite.Group): A group containing all the aliens in the level.
        __aliens_weapons (pygame.sprite.Group): A group containing all the weapons used by the aliens in the level.
        __alien_damage (int): The damage dealt by the aliens.
        __alien_shooting_time (int): The time between alien shooting.
        __level_music (pygame.mixer.Sound): The audio for the level.
        __laser_sound (pygame.mixer.Sound): The audio for the laser shot by the aliens.
        """
        # Initialize level attributes
        self.__screen = screen
        self.__width = width
        self.__height = height
        self.__alien_rows = alien_rows
        self.__alien_columns = alien_columns

        self.__is_level_locked = False
        self.__is_level_finished = False
        self.__level_name = level_name

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
        self.__alien_damage = alien_damage
        self.__alien_shooting_time = alien_shooting_time

        # Level audio
        self.__level_music = pygame.mixer.Sound(level_audio_path)
        self.__level_music.set_volume(0.2)
        self.__laser_sound = pygame.mixer.Sound("audio/laser.wav")
        self.__laser_sound.set_volume(0.4)

    @property
    def is_level_locked(self):
        """
        This property returns the value of the private attribute `__is_level_locked`
        indicating whether the level is locked or not.

        Returns:
            bool: True if the level is locked, False otherwise.
        """
        return self.__is_level_locked

    @is_level_locked.setter
    def is_level_locked(self, new_value):
        """
        This property sets the value of the private attribute `__is_level_locked`
        to indicate whether the level is locked or not.

        Args:
            new_value (bool): True if the level should be locked, False otherwise.
        """
        self.__is_level_locked = new_value

    @property
    def is_level_finished(self):
        """
        This property sets the value of the private attribute `__is_level_finished`
        to indicate whether the level is finished or not.

        Args:
            new_value (bool): True if the level should be finished, False otherwise.
        """
        return self.__is_level_finished

    @is_level_finished.setter
    def is_level_finished(self, new_value):
        """
        This property sets the value of the private attribute `__is_level_finished`
        to indicate whether the level is finished or not.

        Args:
            new_value (bool): True if the level should be finished, False otherwise.
        """
        self.__is_level_finished = new_value

    @property
    def alien_weapons(self):
        """
        This property returns the value of the private attribute `__aliens_weapons`,
        which contains information about the weapons the aliens have.

        Returns:
            any: The value of the `__aliens_weapons` attribute.
        """
        return self.__aliens_weapons

    @property
    def blocks(self):
        """
        This property returns the value of the private attribute `__blocks`,
        which contains information about the blocks in the level.

        Returns:
            any: The value of the `__blocks` attribute.
        """
        return self.__blocks

    @property
    def aliens(self):
        """
        This property returns the value of the private attribute `__aliens`,
        which contains information about the aliens in the level.

        Returns:
            any: The value of the `__aliens` attribute.
        """
        return self.__aliens

    @property
    def alien_damage(self):
        """
        This property returns the value of the private attribute `__alien_damage`,
        which contains information about the damage the aliens can cause.

        Returns:
            any: The value of the `__alien_damage" attribute
        """
        return self.__alien_damage

    @property
    def alien_shooting_time(self):
        """
        This property returns the value of the private attribute `__alien_shooting_time`,
        which contains information about the time intervals between alien shootings.

        Returns:
            any: The value of the `__alien_shooting_time` attribute.
        """
        return self.__alien_shooting_time

    @property
    def game_music(self):
        """
        This property returns the value of the private attribute `__level_music`,
        which contains information about the music played during the level.

        Returns:
            any: The value of the `__level_music` attribute.
        """
        return self.__level_music

    @property
    def level_name(self):
        """
        This property returns the value of the private attribute `__level_name`,
        which contains the name of the level.

        Returns:
            str: The name of the level.
        """
        return self.__level_name

    def enemy_handler(self):
        """
        This method is responsible for handling all the enemies in the game.
        It updates and draws all the blocks, aliens and alien weapons on the screen.

        Returns:
            None
        """
        self.__blocks.draw(self.__screen)
        self.__aliens.draw(self.__screen)
        self.__aliens.update(self.__alien_direction)
        self.__adjust_alien_position()

        self.__aliens_weapons.update()
        self.__aliens_weapons.draw(self.__screen)

    def alien_attack(self):
        """
        This method is responsible for the aliens attacking the player.
        It shoots the laser beam from a random alien.

        Returns:
            None
        """
        self.__alien_shoot()

    def __create_obstacles(self, x_start, y_start, *offset):
        """
        This method is responsible for creating the obstacles in the game.
        It takes in the starting x and y positions and the offset of each obstacle and adds them to the __blocks sprite group.

        Args:
            x_start (int): The starting x position of the first obstacle.
            y_start (int): The starting y position of the first obstacle.
            *offset: The offset of each obstacle in the x direction.

        Returns:
            None
        """
        for x_offset in offset:
            for row_index, row in enumerate(self.__obstacle_shape):
                for column_index, column in enumerate(row):
                    if column == 'x':
                        x = ((column_index * self.__block_size) + x_start) + x_offset
                        y = (row_index * self.__block_size) + y_start
                        block = Block(self.__block_size, (255, 90, 90), x, y)
                        self.__blocks.add(block)

    def initialize_aliens(self, x_offset=100, y_offset=80, x_start=70, y_start=60):
        """
        Initializes the aliens in the game.

        Parameters:
        x_offset (int, optional): The horizontal offset between each alien in the grid. Default is 100.
        y_offset (int, optional): The vertical offset between each row of aliens in the grid. Default is 80.
        x_start (int, optional): The x-coordinate of the first alien in the grid. Default is 70.
        y_start (int, optional): The y-coordinate of the first row of aliens in the grid. Default is 60.

        Returns:
        None
        """
        # Initialize obstacles
        self.__obstacle_shape = obstacle_shape
        self.__blocks = pygame.sprite.Group()
        obstacle_offsets = [num * (self.__width / self.__obstacle_amount) for num in range(self.__obstacle_amount)]
        self.__create_obstacles(self.__width / 25, 650, *obstacle_offsets)

        # Initialize aliens
        self.__aliens = pygame.sprite.Group()
        self.__aliens_weapons = pygame.sprite.Group()

        for row_index, row in enumerate(range(self.__alien_rows)):
            for column_index, column in enumerate(range(self.__alien_columns)):
                x = column_index * x_offset + x_start
                y = row_index * y_offset + y_start
                alien = Alien(x, y)
                self.__aliens.add(alien)

    def __adjust_alien_position(self):
        """
        Adjusts the position of the aliens in the game if they reach either the left or right edge of the screen.

        Returns:
        None
        """
        if self.__aliens.sprites():
            for alien in self.__aliens.sprites():
                if alien.rect.right >= self.__width:
                    self.__alien_direction = -2
                    self.__alien_move_down(2)
                elif alien.rect.left <= 0:
                    self.__alien_direction = 2
                    self.__alien_move_down(2)

    def __alien_move_down(self, distance):
        """
        Moves all the aliens down by a certain distance.

        Parameters:
        distance (int): The distance to move the aliens down by.

        Returns:
        None
        """
        if self.__aliens.sprites():
            for alien in self.__aliens.sprites():
                alien.rect.y += distance

    def __alien_shoot(self):
        """
        Allows random alien to shoot a laser in the game.

        Returns:
        None
        """
        if self.__aliens.sprites():
            alien = choice(self.__aliens.sprites())
            self.__aliens_weapons.add(alien.prepare_laser(self.__height))
            self.__laser_sound.play()
