print("Welcome to my Sodoku Challenge application!\n")

def start_selection(mode):
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
run()