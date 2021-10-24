from car import Car
from board import Board
import json
import sys
class Game:
    """
    Add class description here
    """

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        self.board = board

    def __single_turn(self):
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it. 

        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what 
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.


        Before and after every stage of a turn, you may print additional
        information for the user, e.g., printing the board. In particular,
        you may support additional features, (e.g., hints) as long as they
        don't interfere with the API.
        """
        user_input = input("enter car name and direction:")
        while len(user_input) != 3 or user_input[1] !="," or not self.board.move_car(user_input[0],user_input[2]):
            if user_input == "!":
                return False
            print("the car name or direction is invalid or ilegal move.. try again")
            user_input = input("enter car name and direction:")
        return True


    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        print(self.board)
        while True:
            if self.board.cell_content(self.board.target_location()) != None:
                break
            if not self.__single_turn():
                break
            print(self.board)
        return



VALID_CARS= ["Y","B","O","G","W","R"]



def load_json(filename):
    json_file = filename
    with open(json_file, 'r') as file:
        car_config = json.load(file)
    # now car_config is a dictionary equivalent to the JSON file
    return car_config


def check_car(key,key_value):
    if not key in VALID_CARS:
        return False
    if key_value[0] <= 0:
        return False
    if not key_value[2] in [0, 1]:
        return False
    return True











if __name__== "__main__":
    car_config = load_json(sys.argv[1])
    board = Board()
    game = Game(board)
    for key in car_config.keys():
        if check_car(key, car_config[key]):
            car = Car(key, *car_config[key])
            game.board.add_car(car)
    game.play()


