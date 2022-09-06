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
        elif mode.lower() != "play" or "rules":
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
        setting = input()
        difficulty = ""
        try:
            if int(setting) == 1:
                difficulty = "easy"
            elif int(setting) == 2:
                difficulty = "medium"
            elif int(setting) == 3:
                difficulty = "hard"
            elif setting != 1 or 2 or 3:
                raise AttributeError
            return difficulty
        except AttributeError:
            print(f"{setting} is an invalid reference, please enter"
                  "play/rules/exit")
            return False

def create_puzzle():
    """
    Reads the difficulty setting selected, then creates the grid.
    """

    difficulty = get_difficulty()
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
    # Response to user to show still working
    print("Your puzzle is as follows:")
    print("\033[1;33;40m  A B C D E F G H I \033[0m ")

    possible_answers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    grid_locations = []

    # search for all grid reference options (saves typing)
    for x in range(97, 106):
        for y in range(1, 10):
            locations = chr(x) + str(y)
            grid_locations.append(locations)

    with open(pull_puzzle + ".txt") as f:
        puzzle = f.readlines()

    for line in range(len(puzzle)):
        print(f"\033[1;33;40m{line + 1}\033[0m " + puzzle[line])
    with open(pull_answer + ".txt") as a:
        answer = a.readlines()

    for i in range(len(answer)):
        answer[i] = answer[i].strip('\n').split(',')
    # Converting display puzzle to number array
    for i in range(len(puzzle)):
        puzzle[i] = puzzle[i].strip('\n').split(',')

    
    while "_" in pull_answer:
        # Requesting user to enter field and guess
        grid_entry = input("Your grid ref: \n")
        answer_entry = input("your guess: \n")

        print(f"Your entry is {answer_entry} in {grid_entry}")
        print("Checking if your answer is correct....")

        # Request system to check answers are valid options
        validate_entry(possible_answers, answer_entry)
        validate_entry(grid_locations, grid_entry.lower())

        # Check if entry matches answer
        if test_entry(answer, grid_entry, answer_entry, puzzle) is True:
            print("this has worked")
        else:
            print("Try again")


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


def test_entry(answer, grid_entry, answer_entry, puzzle):
    """
    checks if guess v answer is correct.
    """
    # To split guess location into single location identifiers
    grid = grid_entry
    grid_x = grid[0].lower()
    grid_y = grid[1]
    # guess_location = grid_x[grid_y]

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

    # print(f"grid_x = {grid_x}")
    # print(f"grid_y = {grid_y}")

    # print(puzzle[grid_x])
    # print(puzzle[int(grid_y)][int(grid_x)])
    if int(answer[int(grid_y)-1][int(grid_x)]) == int(answer_entry):
        print("Correct")
        puzzle[int(grid_y)-1][int(grid_x)] = answer_entry
        print(puzzle[int(grid_y)-1])
        return True
    else:
        return False

    # 'print(f"guess_place = {guess_location}")


def intro():
    """
    Greets the user and starts the Sudoku application
    """
    print("Welcome to my Sodoku Challenge application!\n")
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

# roadmap

# validation function to be added for play/rules, difficulty, grid reference
# and entry.
# main game body - to check if results == answer

# end game loop, if display contains "_", if no - game over.

# implement timestamp at starting of game
# implement timestamp at end of game
# including attempted guesses
# leaderboard to show time and guesses, selectable boards ?

# colouring of input and keywords.

# add validation to get_setting function

# LAST ADDED - MAPPING OF GUESS LOCATION IN TEST_ENTRY FIELD
# TO BE REVIEWED AS NOT DISPLAYING LIST VALUES