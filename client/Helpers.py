from typing import List, Dict


LETTERS = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]


class ShipLocation:
    x: int
    y: int
    o: int

    def __init__(self, x, y, o):
        self.x = x
        self.y = y
        self.o = o

    def in_location(self, x, y):
        pass

    def calculate_location(self):
        pass
