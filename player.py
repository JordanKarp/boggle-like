from upgrades import UpgradeSystem
from data import settings
from colored_terminal import returnBold, returnBlue


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.extra_lives = 0
        self.freebies = 0
        self.win_percent = 0
        self.level_time = 0
        self.score_mult = {}
        self.complete_mult = 0
        self.min_length = 0
        self.extra_time = 0
        self.upgrades = {}

    def new_player(self):
        self.score = 0
        self.extra_lives = settings.EXTRA_LIVES
        self.freebies = settings.FREEBIES
        self.win_percent = settings.WIN_PERCENT
        self.level_time = settings.LEVEL_TIME
        self.score_mult = settings.SCORE_MULTIPLIERS
        self.complete_mult = settings.BONUS_MULTIPLIER
        self.min_length = settings.MIN_WORD_LENGTH
        self.extra_time = 0
        self.upgrades = UpgradeSystem(self)
        self.upgrades.load_upgrades(settings.UPGRADE_FILE_PATH)

    def load_player(self, player):
        self.score = player.score
        self.extra_lives = player.extra_lives
        self.freebies = player.freebies
        self.win_percent = player.win_percent
        self.level_time = player.level_time
        self.score_mult = player.score_mult
        self.complete_mult = player.complete_mult
        self.min_length = player.min_length
        self.extra_time = player.extra_time
        self.upgrades = player.upgrades

    def show_player_header(self):
        name_text = f"{self.name}: {self.score}"
        info_text = f"{self.freebies} freebies \t Lives:{self.extra_lives}"
        print(returnBlue(returnBold(name_text)))
        print(returnBlue(info_text))
        print(returnBlue("*" * 50))
