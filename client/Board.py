from typing import List, Dict
from client.Ships import *
from client.Helpers import LETTERS


class TargetBoard:

    __board: Dict[int, List[int]]

    def __init__(self):
        self.__board = {}

        for i in range(0, 10):
            self.__board.update({i: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]})

    def __str__(self):
        rtr = "x  1  2  3  4  5  6  7  8  9  10\n"

        i = 0
        for c in self.__board.items():
            rtr += LETTERS[i].upper() + " "
            for r in c[1]:
                if r == 0:
                    rtr += " o "
                elif r == 1:
                    rtr += " x "

            rtr += "\n"
            i += 1

        return rtr


class PlaceBoard:

    carrier: Carrier
    battleship: Battleship
    cruiser: Cruiser
    submarine: Submarine
    destroyer: Destroyer

    def __init__(self):
        self.carrier = Carrier()
        self.battleship = Battleship()
        self.cruiser = Cruiser()
        self.submarine = Submarine()
        self.destroyer = Destroyer()
