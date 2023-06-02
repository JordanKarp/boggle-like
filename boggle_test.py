from collections import Counter
import os
from random import choice
from string import ascii_lowercase

# from threading import Timer
from my_timer import MyTimer


def clear():
    _ = os.system("cls") if os.name == "nt" else os.system("clear")


def load_words(word_file):
    with open(word_file, "r") as f:
        dictionary = f.read()
    return [x.lower() for x in dictionary.split("\n")]


def return_anagrams(letters, word_list):
    MIN_WORD_LENGTH = 2
    letters = letters.lower()
    letters_count = Counter(letters)

    anagrams = set()
    for word in word_list:
        if not set(word) - set(letters):
            check_word = {k for k, v in Counter(word).items() if v <= letters_count[k]}
            if check_word == set(word):
                anagrams.add(word)

    anagram_list = [x for x in anagrams if len(x) >= MIN_WORD_LENGTH]
    print(len(anagram_list))
    return sorted(anagram_list, key=lambda x: len(x), reverse=True)


def word_list_length_counter(word_list):
    letter_count_dict = {}
    for word in word_list:
        if len(word) in letter_count_dict:
            letter_count_dict[len(word)].append(word)
        else:
            letter_count_dict[len(word)] = [word]

    return letter_count_dict


def boggle_dict_counter_print(word_dict):
    for k, v in word_dict.items():
        print(f"{k}: {len(v)}")


def boggle_dict_print(word_dict):
    for k, v in word_dict.items():
        print(f"{k}: {sorted(v)}")


def is_word_in_list(word, word_list):
    return word in word_list


def checkVowels(string):  # use-defined function
    return any(char in "aeiouAEIOU" for char in string)


def get_random_letters(num):
    vowels = ["a", "e", "i", "o", "u"]
    result = "".join(choice(ascii_lowercase) for _ in range(num - 1))
    if all(char not in vowels for char in result):
        result += choice(vowels)
    else:
        result += choice(ascii_lowercase)

    return result


wList = load_words("TWL06.txt")

word_len = 5
# WORD = choice(wList)
WORD = get_random_letters(word_len)

all_possible_words = return_anagrams(WORD, wList)
word_dict = word_list_length_counter(all_possible_words)

PUZZLE_TIME = 90
PUZZLE_PERCENT = 0.50
STARTING_FREEBIES = 1
POINTS_MULT = {
    2: 0.5,
    3: 1,
    4: 1.5,
    5: 2,
    6: 2.5,
    7: 3,
    8: 3.5,
    9: 4,
    10: 4.5,
    11: 5,
    12: 5.5,
    13: 6,
}


class Player:
    def __init__(self):
        self.puzzle_time = PUZZLE_TIME
        self.point_multipliers = POINTS_MULT
        self.puzzle_percent = PUZZLE_PERCENT
        self.freebies = STARTING_FREEBIES


class AnagramGenerator:
    def __init__(self, word_list):
        self.all_words = word_list
        self.puzzle_letters = ""
        self.puzzle_possible_words = []
        self.correct_words = []

    @property
    def player_custom_score(self):
        return sum(len(x) * POINTS_MULT[len(x)] for x in self.correct_words)

    @property
    def total_custom_score(self):
        return sum(len(x) * POINTS_MULT[len(x)] for x in self.puzzle_possible_words)

    def guess_word(self, word):
        if word in self.correct_words:
            return f"{word} has already been guessed."
        if word not in self.puzzle_possible_words:
            return f"{word} is not in the puzzle."

        self.correct_words.append(word)
        return f"{word} is correct!"

    def set_puzzle(self, puzzle_letters):
        self.correct_words = []
        self.puzzle_letters = puzzle_letters.lower()
        self.puzzle_possible_words = self.return_anagrams()

    def reveal(self):
        return [
            word
            for word in self.puzzle_possible_words
            if word not in self.correct_words
        ]

    def return_anagrams(self):
        MIN_WORD_LENGTH = 2
        letters_count = Counter(self.puzzle_letters)

        anagrams = set()
        for word in self.all_words:
            if not set(word) - set(self.puzzle_letters):
                check_word = {
                    k for k, v in Counter(word).items() if v <= letters_count[k]
                }
                if check_word == set(word):
                    anagrams.add(word)

        anagram_list = [x for x in anagrams if len(x) >= MIN_WORD_LENGTH]
        print(len(anagram_list))
        return sorted(anagram_list, key=lambda x: len(x), reverse=True)

    def times_up(self):
        print("Sorry, time's up")
        self.end_game()

    def end_game(self):
        global playing
        print("Game Over")
        print(self.player_custom_score)
        print(self.total_custom_score)
        print(f"= {self.player_custom_score/self.total_custom_score:.1%}")
        playing = False


game = AnagramGenerator(wList)
game.set_puzzle(WORD)
playing = True

timeout = word_len * 30 - 90
t = MyTimer(timeout, game.times_up)
t.start()

current_score = 0
max_score = game.total_custom_score

log = ""

while playing:
    clear()
    print("Score:", current_score)
    print("Max score:", max_score)
    print("Time left: ", round(t.remaining(), 2))
    print(log)
    print()
    print(f"Words so far: {game.correct_words}")
    print()
    print("-------", WORD, "-------")
    print()
    guess = input("> ")
    if guess == "quit":
        t.cancel()
        playing = False
    if guess == "reveal":
        t.cancel()
        print(game.reveal())
        playing = False
    msg = game.guess_word(guess)
    log = msg
    current_score = game.player_custom_score
