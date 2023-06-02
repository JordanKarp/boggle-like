from os import path
import pickle
from dataclasses import dataclass
from tools import clear


@dataclass
class GameScore:
    name: str
    score: float


class HighScoreManager:
    def __init__(self, scoreboard_file=None, max_num_high_scores=10):
        self.max_num_high_scores = max_num_high_scores
        self.scoreboard = self.load_scores(scoreboard_file)

    @property
    def highscore(self):
        return 0 if self.scoreboard == [] else self.scoreboard[0].score

    # Return a scoreboard or set the scoreboard ?
    def load_scores(self, scoreboard_file):
        try:
            with open(scoreboard_file, "rb") as file:
                scoreboard = pickle.load(file)
        except OSError:
            scoreboard = []
        return scoreboard

    def save_scores(self):
        with open(path.join("data", "scoreboard.dat"), "wb") as file:
            pickle.dump(self.scoreboard, file)

    def add_and_check_score(self, game_score):
        # Add Score
        self.scoreboard.append(game_score)
        # Sort and limit to to max number of scores
        self.scoreboard.sort(key=lambda x: x.score, reverse=True)
        if len(self.scoreboard) >= self.max_num_high_scores:
            self.scoreboard = self.scoreboard[: self.max_num_high_scores]
        # Save Scoreboard
        self.save_scores()

    def show(self):
        clear()
        print("All-Time High Scores")
        for i, game_score in enumerate(self.scoreboard, 1):
            place = f"{str(i)}."
            print(f"{place.ljust(3)} {game_score.name} \t{game_score.score}")
        input()
