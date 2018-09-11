from client.Board import *
from client.Helpers import *


class Player:

    name: str
    wins: int
    losses: int

    target: TargetBoard
    place: PlaceBoard

    def __init__(self, name="", w=0, l=0):
        self.name = name
        self.wins = w
        self.losses = l

        self.target = TargetBoard()
        self.place = PlaceBoard()

    def __str__(self):
        rtr = self.target.__str__()

        return rtr

    def get_name(self):
        pass

    def place_ships(self):
        self.__get_location(self.place.carrier)
        self.__get_location(self.place.battleship)
        self.__get_location(self.place.cruiser)
        self.__get_location(self.place.submarine)
        self.__get_location(self.place.destroyer)

    def __get_location(self, s: Ship) -> Ship:
        # Format string should be columnrow(row)orientation (a9h)
        while True:
            location = input("Place your %s\n> " % s.name)

            try:
                (c, r, o) = self.__check_location(location)
                loc = ShipLocation(c, r, o)
                s.place_ship(loc)

                return s
            except ValueError:
                print("That location is invalid!")
                continue

    def __check_location(self, location: str):
        if not (len(location) == 3 or len(location) == 4):
            raise ValueError

        c = location[0]
        r = location[1] if len(location) == 3 else 9
        o = location[-1]

        c = c.lower()
        o = o.lower()

        if c not in LETTERS:
            raise ValueError
        else:
            c = LETTERS.index(c)

        r = int(r)
        if r not in range(0, 10):
            raise ValueError

        if o not in ["h", "v"]:
            raise ValueError

        return c, r, o
