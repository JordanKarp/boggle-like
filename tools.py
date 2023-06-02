import os


def clear():
    _ = os.system("cls") if os.name == "nt" else os.system("clear")


def inputNumber(message, accepted_range=None):
    while True:
        try:
            userInput = int(input(message))
            if accepted_range and (
                userInput < accepted_range[0] or userInput > accepted_range[1]
            ):
                raise ValueError
        except ValueError:
            if accepted_range:
                print(
                    f"Please pick between {accepted_range[0]} and {accepted_range[1]}."
                )
            else:
                print("Please try again.")
            continue
        else:
            return userInput


def inputYesNo(message):
    yeses = ["Y", "Yes", "y", "yes", 1]
    nos = ["N", "No", "n", "no", 2]
    while True:
        try:
            userInput = input(message)
            if userInput in yeses:
                return True
            elif userInput in nos:
                return False
            raise ValueError
        except ValueError:
            print(f"Please pick either {yeses} or {nos}.")
            continue


def printProgressBar(
    iteration,
    total,
    prefix="",
    suffix="",
    decimals=1,
    length=50,
    fill="█",
    printEnd="\r",
):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + "-" * (length - filledLength)
    print(f"\r{prefix} |{bar}| {percent}% {suffix}", end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()


def printProgressBarMin(
    iteration,
    total,
    minimum,
    prefix="",
    suffix="",
    decimals=1,
    length=50,
    fill="█",
    printEnd="\r",
):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        minimum     - Required  : Min to turn green (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    perc = iteration / float(total)
    percent = ("{0:." + str(decimals) + "f}").format(100 * perc)
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + "-" * (length - filledLength)
    p_bar = f"\r{prefix} |{bar}| {percent}% {suffix}"
    if perc >= minimum:
        print(f"\033[92m{p_bar} \033[00m", end=printEnd)
    else:
        print(p_bar, end=printEnd)

    # Print New Line on Complete
    if iteration == total:
        print()
