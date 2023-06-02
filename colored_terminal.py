def printRed(string_message):
    print(f"\033[31m{string_message}\033[00m")


def printGreen(string_message):
    print(f"\033[32m{string_message}\033[00m")


def printYellow(string_message):
    print(f"\033[33m{string_message}\033[00m")


def printBlue(string_message):
    print(f"\033[34m{string_message}\033[00m")


def printPurple(string_message):
    print(f"\033[35m{string_message}\033[00m")


def printCyan(string_message):
    print(f"\033[36m{string_message}\033[00m")


def printWhite(string_message):
    print(f"\033[37m{string_message}\033[00m")


def returnRed(string_message):
    return f"\033[31m{string_message}\033[00m"


def returnGreen(string_message):
    return f"\033[32m{string_message}\033[00m"


def returnYellow(string_message):
    return f"\033[33m{string_message}\033[00m"


def returnBlue(string_message):
    return f"\033[34m{string_message}\033[00m"


def returnPurple(string_message):
    return f"\033[35m{string_message}\033[00m"


def returnCyan(string_message):
    return f"\033[36m{string_message}\033[00m"


def returnWhite(string_message):
    return f"\033[37m{string_message}\033[00m"


# BOLD
def printBold(string_message):
    print(f"\033[1m{string_message}\033[00m")


def returnBold(string_message):
    return f"\033[1m{string_message}\033[00m"


# UNDERLINE
def printUnderline(string_message):
    print(f"\033[4m{string_message}\033[00m")


def returnUnderline(string_message):
    return f"\033[4m{string_message}\033[00m"


# ITALICS
def printItalics(string_message):
    print(f"\033[3m{string_message}\033[00m")


def returnItalics(string_message):
    return f"\033[3m{string_message}\033[00m"


def returnStrike(string_message):
    return f"\033[9m{string_message}\033[00m"

    # result = ''
    # for c in string_message:
    #     result = result + c + '\u0336'
    # return result
