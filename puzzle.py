from collections import Counter
from my_timer import MyTimer
from tools import clear, printProgressBarMin
from random import choice
from colored_terminal import returnGreen, returnRed, returnBold, returnUnderline


class Puzzle:
    def __init__(self, every_word, puzzle_str, player):
        self.every_word = every_word
        self.puzzle_str = puzzle_str
        self.player = player
        self.puzzle_time = (
            self.player.level_time * (len(self.puzzle_str) - 3) + self.player.extra_time
        )
        self.timer = MyTimer(self.puzzle_time, self.end_puzzle)
        self.possible = self.return_anagrams()
        self.correct = []
        self.msg = "Type your guess below."
        self.playing = False
        self.is_won = False

    @property
    def player_score(self):
        return sum(len(x) * self.player.score_mult[len(x)] for x in self.correct)

    @property
    def total_score(self):
        return sum(len(x) * self.player.score_mult[len(x)] for x in self.possible)

    @property
    def percent_score(self):
        return self.player_score / self.total_score

    def return_anagrams(self):
        letters_count = Counter(self.puzzle_str)
        anagrams = set()
        for word in self.every_word.all_words:
            if not set(word) - set(self.puzzle_str):
                check_word = {
                    k for k, v in Counter(word).items() if v <= letters_count[k]
                }
                if check_word == set(word):
                    anagrams.add(word)

        anagram_list = [x for x in anagrams if len(x) >= self.player.min_length]
        return sorted(anagram_list, key=lambda x: len(x), reverse=True)

    def guess_word(self, word):
        word = word.lower()
        if word == "":
            return ""
        if word == "q":
            self.end_puzzle()
            return
        elif word == "f":
            if self.player.freebies <= 0:
                return "You don't have any freebies left."
            words = set(self.possible) - set(self.correct)
            word = choice(list(words))
            self.player.freebies -= 1
        elif word in self.correct:
            return f"{word} has already been guessed."
        elif word not in self.possible:
            return f"{word} is not in the puzzle."
        self.correct.append(word)
        return f"{word} is correct!"

    def print_header(self):
        clear()
        self.player.show_player_header()
        printProgressBarMin(
            self.player_score, self.total_score, self.player.win_percent
        )
        print()
        print(f"{self.player_score} of {self.total_score}")
        print(f"{self.timer.remaining:.2f} remaining.")
        print()
        print(sorted(self.correct))
        print()
        print(self.msg)
        print()
        print("-------", " ".join(self.puzzle_str.upper()), "-------")

    def play(self):
        self.playing = True
        self.timer.start()
        while self.playing and self.timer.remaining > 0:
            self.print_header()
            player_guess = input("> ")
            self.msg = self.guess_word(player_guess)
            if self.percent_score >= 1:
                self.end_puzzle()
                self.playing = False
        self.playing = False

    def word_list_into_len_dict(self, word_list):
        letter_count_dict = {}
        for word in word_list:
            if len(word) in letter_count_dict:
                letter_count_dict[len(word)].append(word)
            else:
                letter_count_dict[len(word)] = [word]
        return letter_count_dict

    def end_puzzle(self):
        self.player.extra_time = 0
        remaining = self.timer.remaining
        self.timer.cancel()
        mult = 1
        if self.percent_score >= self.player.win_percent:
            self.is_won = True
            if self.percent_score >= 1:
                mult = self.player.complete_mult
                if self.player.upgrades.perks["add_time"].unlocked:
                    self.player.extra_time = remaining
        self.player.score += self.player_score * mult

        self.draw_scoreboard()
        self.playing = False

    def draw_scoreboard(self):
        clear()
        self.player.show_player_header()
        print()
        if self.is_won:
            msg = returnGreen("Congratulations, you won this round!")
        else:
            msg = returnRed("Sorry, you didn't score high enough this round")
        print(msg)
        print()
        # Turn possible words into a dict based on len, and highlight correct in green
        all_dict = self.word_list_into_len_dict(self.possible)
        for word_len, words in all_dict.items():
            print(f"{word_len}: ", end="")
            for word in sorted(words):
                if word in self.correct:
                    print(returnGreen(word), end=" ")
                else:
                    print(f"{word}", end=" ")
            print()
        print()

        # Turn correct into a dict by len, then add up the score (count * length * mult)
        print(f"{self.player_score/self.total_score:.1%}")
        print()
        print(returnUnderline("Num * Count * Multiplier = Score"))
        correct_dict = self.word_list_into_len_dict(self.correct)
        for word_len, words in sorted(correct_dict.items()):
            count = len(words)
            mult = self.player.score_mult[word_len]
            score = count * word_len * mult
            print(f"{word_len}s:\t{word_len} * {count} * {mult}\t= {float(score)}")
        print()
        if self.player_score / self.total_score == 1:
            mult = self.player.complete_mult
            print(f"Round Score: \t\t{self.player_score}")
            print(f"Bonus! (x{mult}) Score:\t{self.player_score*mult}")
            if self.player.upgrades.perks["add_time"].unlocked:
                print(f"Time added:\t\t{self.player.extra_time:.1f} seconds")
        else:
            print(f"Round Score: \t\t{self.player_score}")
        print(f"Player Total: \t\t{returnBold(self.player.score)}")
