
GAME_NAME = 'ScrambleRPG'

UPGRADE_FILE_PATH = 'data/upgrades.csv'
HIGH_SCORE_FILE = 'data/scoreboard.dat'
WORD_FILE = 'words/TWL06.txt'


EXTRA_LIVES = 0
FREEBIES = 3
WIN_PERCENT = 0.60
LEVEL_TIME = 30
MIN_WORD_LENGTH = 2
BONUS_MULTIPLIER = 2

SCORE_MULTIPLIERS = {
    2: 0.5,
    3: 1,
    4: 1.5,
    5: 2,
    6: 2.5,
    7: 3,
    8: 3.5,
    9: 4,
    10: 4.5
}


def score_mult(length, ):
    return round(.5 * length - .3, 2)
