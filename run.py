from colorama import Fore, Style
from prettytable import PrettyTable
import time

t = PrettyTable()


def start_selection(mode):
    """
    request for user to select either rules to play the game,
    or to start the game.
    """
    try:
        if mode.lower() == "play":
            return True
        elif mode.lower() == "rules":
            print("rules to be displayed here")
            return False
        elif mode.lower() not in ["play", "rules"]:
            raise KeyError
    except KeyError:
        print(f"your entry of '{mode}' is not recognised,"
              "please type either 'play','rules' or 'exit'")
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
        possible_answers = ["1", "2", "3","99"]
        setting = input()
        
        if validate_entry(possible_answers, setting) is True:
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
    difficulty = get_difficulty().lower()
    print("Creating template....")
    print("Scribbling down the answers...")
    print(f"{difficulty} has been selected\n")

# Generating string used for open function.
    pull_puzzle = "sudoku_" + difficulty + "_display"
    pull_answer = "sudoku_" + difficulty + "_answer"
    play_game(pull_puzzle, pull_answer)


def play_game(pull_puzzle, pull_answer):
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

    with open(pull_answer + ".txt") as a:
        answer = a.readlines()
    with open(pull_puzzle + ".txt") as f:
        puzzle = f.readlines()

    # Converting display & puzzle to number array
    for i in range(len(answer)):
        answer[i] = answer[i].strip('\n').split(',')
    for i in range(len(puzzle)):
        puzzle[i] = puzzle[i].strip('\n').split(',')

    # Formatting  for table to display the quiz.
    t.field_names = ["XY", "A", "B", "C", "D", "E", "F", "G", "H", "I"]
    t._min_width = {"A": 4, "C": 4, "F": 4}
    t.align["A"] = "r"
    t.align["C"] = "l"
    t.align["F"] = "l"

    for line in range(len(puzzle)):
        t.add_rows([puzzle[line]])

    _puzzle = []
    for item in puzzle:
        for _item in item:
            _puzzle.append(_item)

    possible_answers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    grid_locations = []

    # search for all grid reference options (saves typing)
    for x in range(97, 106):
        for y in range(1, 10):
            locations = chr(x) + str(y)
            grid_locations.append(locations)
    
    # Variables for score/performance
    guesses = 0
    s_time = time.time()
    # start time in seconds
    print(f"Time started = {s_time}")

    while "0" in _puzzle:
        # Displays puzzle to the user
        print(t)
        # Requesting user to enter field and guess
        grid_entry = input(_p_y + "Your grid ref: \n" + _p_reset)
        answer_entry = input(_p_y + "your guess: \n" + _p_reset)

        print(f"Your entry is {answer_entry} in {grid_entry}")
        print("Checking if your answer is correct....")

        # Check if entry matches answer            
        if validate_entry(possible_answers, answer_entry) is True:
            if validate_entry(grid_locations, grid_entry.lower()) is True:
                if test_entry(answer, grid_entry, answer_entry, puzzle) is True:
                    print(_p_g + "Congrats, you've guessed Correct" + _p_reset)
                    print("Please enter your next entry:")
                    guesses = guesses + 1
                    print(f"Total guesses = {guesses}")
                else:
                    print(_p_r + "Sorry, that is incorrect." + _p_reset)
                    print(_p_r + "Please try again" + _p_reset)
                    guesses = guesses + 1
                    print(f"Total guesses = {guesses}")

    end_game(guesses, s_time)


def list_display(display, location, answer):
    """
    Updates _puzzle for while statement in play_game()
    """
    _puzzle = []
    for item in display:
        for _item in item:
            _puzzle.append(_item)
    return _puzzle


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


def test_entry(answer, grid_entry, answer_entry, puzzle,):
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
        print(Fore.RED + "This field has already been entered" + _p_reset)
        return False
    elif int(answer[int(grid_y)-1][int(grid_x)]) == int(answer_entry):
        # formats answer to display in color
        answer_entry = Fore.GREEN + answer_entry + Style.RESET_ALL
        #Updates puzzle display with new guess
        puzzle[int(grid_y)-1][int(grid_x)+1] = answer_entry
        location = puzzle[int(grid_y)-1][int(grid_x)+1]
        list_display(puzzle, location, answer_entry)
        # re-populates PrettyTable
        t.clear_rows()
        for line in range(len(puzzle)):
            t.add_rows([puzzle[line]]) 
        

    # if statement does not update _puzzle, does not update above
        return True
    else:
        return False


def end_game(guesses, s_time):
    f_time = time.time()
    t_time = int(s_time) - int(f_time)
    print("Congratulations for completing the game!")
    print(f"Total guesses to completion = {guesses}")
    print(f"Total time to complete = {t_time}")


def intro():
    """
    Greets the user and starts the Sudoku application
    """
    print("\033[1;33m Welcome to my Sodoku Challenge application!\n\033[0;0m")
    user = input("Enter your name\n")
    print(f"\nThank you {user.capitalize()},\n"
          f"Type 'rules' if you wish for me to explain how to play\n"
          f"Or type 'play' if you wish to start playing")
    while True:
        mode = input()

        if start_selection(mode):
            print("\nStarting the game now...")
            break


def run():
    """
    Generating order of processes for the game
    """
    intro()
    create_puzzle()


run()


# implement timestamp at starting of game
# implement timestamp at end of game
# including attempted guesses
# leaderboard to show time and guesses, selectable boards ?
