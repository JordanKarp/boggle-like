from game import Game
from game_options import Options
from high_score_manager import HighScoreManager
from enum import Enum
from tools import clear, inputNumber
from data.settings import HIGH_SCORE_FILE, GAME_NAME


class Menu(Enum):
    NEW_GAME = 1
    OPTIONS = 2
    HIGH_SCORE = 3
    QUIT = 4


class App:
    def __init__(self):
        self.running = False
        self.game = None
        self.options = Options()
        self.high_scores = HighScoreManager(HIGH_SCORE_FILE)

    def get_user_name(self):
        clear()
        print(f"Welcome to {GAME_NAME}")
        return input("Who's playing today? ")

    def main_menu(self):
        clear()
        print(f"Welcome to {GAME_NAME}")
        for m in Menu:
            name = m.name.replace("_", " ").capitalize()
            print(f"{m.value}: {name}")
        choice = inputNumber("> ", (1, len(Menu)))
        return Menu(choice)

    def get_save_file_player(self):
        return

    def run(self):
        self.running = True
        name = self.get_user_name()
        while self.running:
            choice = self.main_menu()
            match choice:
                case Menu.NEW_GAME:
                    # Choose game
                    self.game = Game(name, self.high_scores)
                    self.game.new_game()
                    self.running = False
                case Menu.OPTIONS:
                    self.options.run()
                case Menu.HIGH_SCORE:
                    self.high_scores.show()
                case Menu.QUIT:
                    self.running = False


if __name__ == "__main__":
    app = App()
    app.run()
