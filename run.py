def get_difficulty():
    """
    Allows the user to select the difficulty of the game they are starting.
    """
    print("Enter your difficulty setting, \n 1 for Easy \n 2 for Medium \n 3 for Hard \n")
    while True:
        setting = input()
        difficulty = ""
        try:
            if int(setting) == 1:
                difficulty = "easy"
            elif int(setting) == 2:
                difficulty = "medium"
            elif int(setting) == 3:
                difficulty = "hard"
            elif int(setting) != 1 or 2 or 3:
                raise AttributeError
            return difficulty
        except AttributeError as e:
            print(f"{e} invalid reference, please enter play/rules/exit")
            return False


def start_selection(mode):
    """
    request for user to select either rules to play the game, or to star the the game.
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
        print("Value entered not recognised, please type either 'play','rules' or 'exit'")
        return False


def intro():
    """
    Greets the user and starts the Sudoku application
    """
    print("Welcome to my Sodoku Challenge application!\n")
    user = input("Enter your name\n")
    print(f"Thank you {user},\n"
          f"Type 'rules' if you wish for me to explain how to play\n"
          f"Or type 'play' if you wish to start playing")
    

    while True:
        mode = input()
        start_selection(mode)

        if start_selection(mode):
            print("Starting the game now...")
            break

def run():
    intro()
    get_difficulty()
run()