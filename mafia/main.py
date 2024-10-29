import random
from argparse import ArgumentError
from enum import Enum
from random import random


class Status(Enum):
    DEAD = False
    ALIVE = True


class Player:
    def __init__(self, nickname: str | None = None):
        self.nickname: str = nickname
        self.status: Status = Status.ALIVE

    def __repr__(self):
        return f"Name: {self.nickname}, Status: {self.status}"


class Citizen(Player):
    pass


class Mafioso(Player):
    pass


class Police(Player):
    pass


class Medic(Citizen):
    pass


class Game:
    def __init__(self, logins: list[str]):
        self.player_count: int = len(logins)

        if self.player_count < 3:
            raise ArgumentError(None, "Too few players")

        self.mafioso_count: int = self.player_count // 3
        self.citizen_count: int = self.player_count - self.mafioso_count

        self.players: list[Player] = [
            Police(),
            Medic(),
            *[Mafioso() for _ in range(self.mafioso_count)],
            *[Citizen() for _ in range(self.citizen_count - 2)]
        ]

        random.shuffle(logins)

        for i in range(len(self.players)):
            self.players[i].nickname = logins[i]

    def start(self):

        def is_game_finished() -> bool:
            return True if self.mafioso_count >= self.citizen_count else False

        def print_round_info(round_num: int):
            print(f"""Round: {round_num}
            Citizens: {self.citizen_count}
            Mafiosos: {self.mafioso_count}
            Doctor: {self.players[1].status.name.lower().capitalize()}]
            """)

        round_counter: int = 0
        while not is_game_finished():
            round_counter += 1
