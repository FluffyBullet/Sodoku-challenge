print("Welcome to my Sodoku Challenge application!\n")

def intro():
    print("Before we start, let us know your name:")
    user = input("Please enter your name ")

    print(f"Welcome {user}, lets get started!\n Please select your difficulty: 1. Easy, 2. Medium, 3. Hard")
    setting = input("type selection number here: \n")

def run():
    intro()
run()