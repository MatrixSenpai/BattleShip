from typing import List
from client.Helpers import ShipLocation


class Ship:

    life: int
    name: str
    __location: ShipLocation

    def __init__(self, life=0, name=""):
        self.life = life
        self.name = name

    def place_ship(self, loc: ShipLocation):
        self.__location = loc


class Carrier(Ship):

    def __init__(self):
        super(Carrier, self).__init__(5, "Aircraft Carrier")


class Battleship(Ship):

    def __init__(self):
        super(Battleship, self).__init__(5, "Battleship")


class Cruiser(Ship):

    def __init__(self):
        super(Cruiser, self).__init__(3, "Cruiser")


class Submarine(Ship):

    def __init__(self):
        super(Submarine, self).__init__(3, "Submarine")


class Destroyer(Ship):

    def __init__(self):
        super(Destroyer, self).__init__(2, "Destroyer")