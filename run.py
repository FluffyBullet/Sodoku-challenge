from colorama import Fore, Style
from prettytable import PrettyTable
import time

t = PrettyTable()
lb = PrettyTable()


def start_selection(mode):
    """
    request for user to select either rules to play the game,
    or to start the game.
    """
    try:
        if mode.lower() == "play":
            return True
        elif mode.lower() == "rules":
            print("\nSudoku is a 9x9 Grid of cells broken into 3 grids")
            print("first is the row, second the column and third is a cube.")
            print("Each section is to contain numbers between 1 & 9,")
            print("but cannot contain duplicate values")
            print("To play the game, first enter the grid ref, i.e A1 or D4")
            print("Then your answer, i.e 6 or 2")
            print("On hitting return/enter, the grid will update")
            print("and continue until complete\n")
            print("to proceed, type 'play'\n")

            return False
        elif mode.lower() == "leaderboard":
            print(lb)

        elif mode.lower() not in ["play", "rules"]:
            raise KeyError
    except KeyError:
        print(f"your entry of '{mode}' is not recognised,"
              "please type either 'play' or 'rules'")
        return False


def get_difficulty():
    """
    Allows the user to select the difficulty of the game they are starting.
    """
    print("Enter your difficulty setting,\n"
          "1 for Easy \n"
          "2 for Medium \n"
          "3 for Hard \n")
    while True:
        # User entry for difficulty
        possible_ans = ["1", "2", "3", "99"]
        setting = input()

        if validate_entry(possible_ans, setting) is True:
            difficulty = ""
            if setting == "1":
                difficulty = "Easy"
            elif setting == "2":
                difficulty = "Medium"
            elif setting == "3":
                difficulty = "Hard"
            elif setting == "99":
                difficulty = "test"
            return difficulty


def create_puzzle():
    """
    Reads the difficulty setting selected, then creates the grid.
    """
    # Grabbing settings and displaying selection
    global difficulty
    difficulty = get_difficulty().lower()
    print("Creating template....")
    print("Scribbling down the answers...")
    print(f"{difficulty} has been selected\n")

    # Generating string used for open function.
    pull_puzzle = "sudoku_" + difficulty + "_display"
    pull_ans = "sudoku_" + difficulty + "_answer"
    play_game(pull_puzzle, pull_ans)


def puzzle_list(puzzle):
    """
    Generates array of puzzle values
    """
    _puzzle = []
    for item in puzzle:
        for _item in item:
            _puzzle.append(_item)
    return _puzzle


def play_game(pull_puzzle, pull_ans):
    """
    Function to hold the body of Sudoku puzzle
    """

    # Color formatting for text
    _p_y = Fore.YELLOW
    _p_g = Fore.GREEN
    _p_r = Fore.RED
    _p_reset = Style.RESET_ALL

    # Response to user to show still working
    print("Your puzzle is as follows:")
    # Pulling data from text files
    with open(pull_ans + ".txt") as a:
        ans = a.readlines()
    with open(pull_puzzle + ".txt") as f:
        puzzle = f.readlines()

    # Converting display & puzzle to number array
    for i in range(len(ans)):
        ans[i] = ans[i].strip('\n').split(',')
    for i in range(len(puzzle)):
        puzzle[i] = puzzle[i].strip('\n').split(',')

    # Formatting  for table to display the quiz.
    t.field_names = ["XY", "A", "B", "C", "D", "E", "F", "G", "H", "I"]
    t._min_width = {"A": 4, "C": 4, "F": 4}
    t.align["A"] = "r"
    t.align["C"] = "l"
    t.align["F"] = "l"

    # Populating PrettyTable with information
    for line in range(len(puzzle)):
        t.add_rows([puzzle[line]])

    # variable for while condition - if game is complete
    _puzzle = puzzle_list(puzzle)
    # Creating variables for entry validation.
    possible_ans = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    grid_locations = []
    # search for all grid reference options (saves typing)
    for x in range(97, 106):
        for y in range(1, 10):
            locations = chr(x) + str(y)
            grid_locations.append(locations)

    # Variables for score/performance
    global guesses
    guesses = 0
    s_time = time.time()

    while "0" in _puzzle:
        _puzzle = []
        for item in puzzle:
            for _item in item:
                _puzzle.append(_item)
    # Displays puzzle to the user
        print(t.get_string(start=0, end=3))
        print(t.get_string(start=3, end=6, header=False))
        print(t.get_string(start=6, end=10, header=False))
    # Requesting user to enter field and guess
        grid_entry = input(_p_y + "Your grid ref: \n" + _p_reset)
        ans_entry = input(_p_y + "your guess: \n" + _p_reset)
        print(f"Your entry is {ans_entry} in {grid_entry}")
        print("Checking if your answer is correct....")
    # Check if entry matches answer
        if validate_entry(possible_ans, ans_entry) is True:
            if validate_entry(grid_locations, grid_entry.lower()) is True:
                if test_entry(ans, grid_entry, ans_entry, puzzle) is True:
                    print(_p_g + "Congrats, you've guessed Correct" + _p_reset)
                    print("Please enter your next entry:")
                    guesses = guesses + 1
                    print(f"Total guesses = {guesses}")
                    _puzzle = puzzle_list(puzzle)
                else:
                    print(_p_r + "Sorry, that is incorrect." + _p_reset)
                    print(_p_r + "Please try again" + _p_reset)
                    guesses = guesses + 1
                    print(f"Total guesses = {guesses}")
    end_game(guesses, s_time)


def validate_entry(official, entry):
    """
    Check if answer is possible entry of required field.
    """
    try:
        if entry in official:
            return True
        else:
            raise KeyError
    except KeyError:
        print(f"Entry {entry} is not valid, please try again.")
    except (ValueError):
        print(f"Invalid entry of {entry}, please try again.")


def test_entry(ans, grid_entry, ans_entry, puzzle,):
    """
    checks if guess v answer is correct.
    """
    _p_reset = Style.RESET_ALL
    # To split guess location into single location identifiers
    grid = grid_entry
    grid_x = grid[0].lower()
    grid_y = grid[1]

    # Converts grid a-j ref to numeric value
    if grid_x == 'a':
        grid_x = 0
    elif grid_x == 'b':
        grid_x = 1
    elif grid_x == 'c':
        grid_x = 2
    elif grid_x == 'd':
        grid_x = 3
    elif grid_x == 'e':
        grid_x = 4
    elif grid_x == 'f':
        grid_x = 5
    elif grid_x == 'g':
        grid_x = 6
    elif grid_x == 'h':
        grid_x = 7
    elif grid_x == 'i':
        grid_x = 8
    elif grid_x == 'j':
        grid_x = 9

    if puzzle[int(grid_y)-1][int(grid_x)+1] != "0":
        # Checks if entry field has already been entered
        print(Fore.RED + "This field has already been entered" + _p_reset)
        return False
    elif int(ans[int(grid_y)-1][int(grid_x)]) == int(ans_entry):
        # formats answer to display in color
        ans_entry = Fore.GREEN + ans_entry + Style.RESET_ALL
        # Updates puzzle display with new guess
        puzzle[int(grid_y)-1][int(grid_x)+1] = ans_entry
        # Re-populates PrettyTable
        t.clear_rows()
        for line in range(len(puzzle)):
            t.add_rows([puzzle[line]])
        return True
    else:
        return False


def end_game(guesses, s_time):
    """
    On completion summarize details of users performance.
    """
    # Variable for color of text
    _p_g = Fore.GREEN
    _p_y = Fore.LIGHTYELLOW_EX
    _p_reset = Style.RESET_ALL

    # Calculates total time in seconds spent
    global t_time
    f_time = time.time()
    t_time = int(f_time) - int(s_time)

    # Update leaderboard with entry
    lboard = open(f"leaderboard_{difficulty}.txt", "a")
    lboard.write(f'"{user}","{difficulty}","{guesses}","{t_time}"\n')
    lboard.close()

    # Displays users performance
    print(_p_g + "Congratulations for completing the game!" + _p_reset)
    print(f"Total guesses to completion = {guesses}")
    print(f"Total time to complete = {t_time} Seconds\n")
    print(_p_y + "Do you wish to view the leaderboards? (yes/no)" + _p_reset)
    boards = input()
    if boards.lower() == "yes":
        leader_boards()
    print(f"Thank you for playing my game {user}!")


def intro():
    """
    Greets the user and starts the Sudoku application
    """
    print("\033[1;33m Welcome to my Sodoku Challenge application!\n\033[0;0m")
    global user
    user = input("Enter your name\n").capitalize()

    while user.isalpha() != True:
        print("Incorrect entry, please enter your name:")
        user = input("Enter your name\n").capitalize()
    else:
        pass

    print(f"\nThank you {user.capitalize()},\n"
          f"Type 'rules' if you wish for me to explain how to play\n"
          f"Or type 'play' if you wish to start playing")
    while True:
        mode = input()

        if start_selection(mode):
            print("\nStarting the game now...")
            break


def leader_boards():
    """
    Generates leaderboard to display to the user
    """
    lb.field_names = ["name", "difficulty", "guesses", "time(seconds)"]

    with open(f'leaderboard_{difficulty}.txt') as rec:
        leaders = rec.readlines()

    for i in range(len(leaders)):
        leaders[i] = leaders[i].strip("\n").split(",")
    for line in range(len(leaders)):
        lb.add_rows([leaders[line]])

    print(f"{difficulty} difficulty Leaderboard:")
    df = ["name", "guesses", "time(seconds)"]
    lb.sortby = "guesses"
    print(lb.get_string(start=0, end=5, fields=df))


def run():
    """
    Generating order of processes for the game
    """
    intro()
    create_puzzle()


run()
