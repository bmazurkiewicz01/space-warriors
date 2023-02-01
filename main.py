import json
from engine.game import GameManager

if __name__ == '__main__':
    with open("config.json") as file:
        config = json.load(file)

    game_manager = GameManager(config["width"], config["height"], config["levels"])
    game_manager.run()
