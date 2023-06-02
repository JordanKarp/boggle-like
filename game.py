# from colored_terminal import returnBold, returnStrike
from word_dictionary import WordDictionary
from puzzle_factory import PuzzleFactory
from player import Player
from high_score_manager import GameScore
from tools import clear, inputNumber
from data.settings import WORD_FILE

# import pickle


class Game:
    def __init__(self, name, high_scores):
        self.name = name
        self.high_scores = high_scores
        self.playing = False
        self.word_dict = None
        self.player = None
        self.puzzle_factory = None
        self.active_puzzle = None

    def get_word_len(self):
        clear()
        self.player.show_player_header()
        print("Get Ready!")
        # TODO: adjust range
        return inputNumber("How many letters? ", [4, 5])

    def show_puzzle_description(self):
        t = self.player.level_time * (len(self.active_puzzle.puzzle_str) - 3)
        et = self.player.extra_time
        if et > 0:
            print(f"You have {t} (+{et:.2f}) seconds to find as many words as you can.")
        else:
            print(f"You have {t} seconds to find as many words as you can.")
        print(f"This puzzle has a max score of {self.active_puzzle.total_score}.")
        input("Press any key to proceed.")

    def win_whats_next(self):
        print("1. Next round \n2. Upgrades Menu \n3. Quit")
        choice = inputNumber("> ", [1, 3])
        match choice:
            case 2:
                self.player.upgrades.show()
            case 3:
                self.add_score()
                self.playing = False

    def lose_whats_next(self):
        if self.player.extra_lives > 0:
            print(f"Extra life used! {self.player.extra_lives} left.")
            self.win_whats_next()
        else:
            self.add_score()
            print("1. New Game")
            print("2. High Scores")
            print("3. Quit")
            choice = inputNumber("> ", [1, 3])
            match choice:
                case 1:
                    # Do I swap the below lines?
                    self.new_game()
                    self.playing = False
                case 2:
                    self.high_scores.show()
                    self.playing = False
                case 3:
                    self.playing = False

    def add_score(self):
        self.high_scores.add_and_check_score(
            GameScore(self.name.ljust(20), self.player.score)
        )

    def run(self):
        while self.playing:
            word_len = self.get_word_len()
            self.active_puzzle = self.puzzle_factory.create_random(word_len)
            self.show_puzzle_description()
            self.active_puzzle.play()
            if self.active_puzzle.is_won:
                self.win_whats_next()
            else:
                self.lose_whats_next()

    def new_game(self):
        self.word_dict = WordDictionary(WORD_FILE)
        self.player = Player(self.name)
        self.player.new_player()
        self.puzzle_factory = PuzzleFactory(self.word_dict, self.player)
        self.playing = True
        self.run()
