from classes import person, board, tile, item
from functions import shop, display

def init_contestents(number_of_players: int) -> list:
    players = []
    for i in range(number_of_players):
        name = input("Enter player name: ")
        User = person.Player(name)
        players.append(User)

    return players

def rules() -> None:
    with open("rules.txt", "r") as file:
        for line in file:
            print(line, end='')

def welcome_message() -> None:
    print("Welcome to the Hide and Seek!")
    
def start_game() -> None:
    try:
        players = init_contestents(int(input("Enter number of players: ")))
    except ValueError:
        print("Invalid input, try again.")

def main():
    menu = {
        "Play":{
            "Start": lambda: start_game(),
            "Rules": lambda: rules(),
            "Back": exit
            #TODO: add continue game
            }, 
        # "Add API": lambda: add_api(api_classes_list),
        "Exit": exit
    }
    display.display(menu)

if __name__ == "__main__":
    main()