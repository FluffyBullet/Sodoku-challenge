print("Welcome to my Sodoku Challenge application!\n")

def start_selection(mode):

def intro():
    """
    Greets the user and starts the Sudoku application
    """
    print("Welcome to my Sodoku Challenge application!\n")
    user = input("Enter your name\n")
    print(f"Thank you {user},\n"
          f"Type 'rules' if you wish for me to explain how to play\n"
          f"Or type 'play' if you wish to continue playing")
    mode = input()

    while True:
        start_selection(mode)

        if start_selection(mode):
            print("Starting the game now...")
            break

def run():
    intro()
run()