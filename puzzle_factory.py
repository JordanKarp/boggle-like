from puzzle import Puzzle
from random import choice
from string import ascii_lowercase

MIN_NUMBER_OF_WORDS = 3


class PuzzleFactory:
    def __init__(self, word_dict, player):
        self.word_dict = word_dict
        self.player = player

    def load_player(self, player):
        self.player = player

    def create_random(self, word_len):
        lets = self.get_random_letters(word_len)
        p = Puzzle(self.word_dict, lets, self.player)
        while len(p.possible) < MIN_NUMBER_OF_WORDS:
            lets = self.get_random_letters(word_len)
            p = Puzzle(self.word_dict, lets, self.player)
        return p

    @staticmethod
    def get_random_letters(num):
        vowels = ["a", "e", "i", "o", "u"]
        result = "".join(choice(ascii_lowercase) for _ in range(num - 1))
        if all(char not in vowels for char in result):
            result += choice(vowels)
        else:
            result += choice(ascii_lowercase)

        return result
