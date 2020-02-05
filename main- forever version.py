#!/usr/bin/env python3
import sys, os, json
# Check to make sure we are running the correct version of Python
assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

# The game and item description files (in the same folder as this script)
game_file = 'game_forever.json'


# Load the contents of the files into the game and items dictionaries. You can largely ignore this
# Sorry it's messy, I'm trying to account for any potential craziness with the file location
def load_files():
    try:
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        with open(os.path.join(__location__, game_file)) as json_file: game = json.load(json_file)
        return game
    except:
        print("There was a problem reading either the game or item file.")
        os._exit(1)


def render(game,current):
    c = game[current]
    print(c["desc"])

def get_input():
    response = input(" ")
    response = response.upper().strip()
    return response

def update(game,current,response):
    c = game[current]
    for e in c["exits"]:
        if response == e["exit"]:
            return e["target"]
    return current
# variable for counter?
# num_death = 0
    

# The main function for the game
def main():
    current = 'START'  # The starting location
    #end_game = ['JUMP1', 'SPEAK1', 'APPRAOCH1', 'LISTEN1', 'WALK1', 'CLIMB1', 'RIGHT2', 'LEFT2', 'FORWARD1', 'LOOK2', 'RIGHT3', 'LEFT3','IRON1', 'SILVER1', 'ORANGE1', 'BLUE1' ]  # Any of the end-game locations

    game = load_files()

    while True:
        render(game,current)

      
        response = get_input()

        if response == "QUIT" or response == "Q":
            break #break out of the while loop

        current = update(game,current,response)

    print("Goodbye.")

# run the main function
if __name__ == '__main__':
	main()

