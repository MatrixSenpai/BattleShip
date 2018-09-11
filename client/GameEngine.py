from client.Board import *
from client.Player import Player
from client.Helpers import ShipLocation


class GameEngine:
    player_one: Player

    player_two: Player

    def __init__(self):
        self.player_one = Player("Matrix", 0, 0)
        self.player_two = Player("Computer", 0, 0)

    def game_main(self):
        print("%s vs %s! Let the game begin!" % (self.player_one.name, self.player_two.name))

        self.__begin_game()

        print("Let's play!")
        flag = True
        end_flag = True

        while end_flag:
            end_flag = self.__main_logic(flag)
            flag = not flag

    def __begin_game(self):
        print("Place your ships...")

        # self.player_one.place_ships()
        # self.player_two.place_ships()

    def __main_logic(self, turn: bool) -> bool:
        player = self.player_one if turn else self.player_two

        print(player)

    def __get_player(self):
        pass
