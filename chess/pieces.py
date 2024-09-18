from abc import abstractmethod


class Piece:

    @abstractmethod
    def get_moveset(self, x: int, y: int) -> list[tuple[int, int]]:
        pass

    @abstractmethod
    def get_moves_between(self, x1: int, y1: int, x2: int, y2: int) -> list[tuple[int, int]]:
        pass


class King(Piece):
    def get_moveset(self, x: int, y: int) -> list[tuple[int, int]]:
        out: list[tuple[int, int]] = []
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                if x == 0 and y == 0: continue
                out.append((x, y))
        return out

    def __str__(self):
        return "King"

    def get_moves_between(self, x1: int, y1: int, x2: int, y2: int) -> list[tuple[int, int]]:
        return []


class Queen(Piece):
    def get_moveset(self, x: int, y: int) -> list[tuple[int, int]]:
        out: list[tuple[int, int]] = []
        out.extend(Bishop().get_moveset(0, 0))
        out.extend(Rook().get_moveset(0, 0))
        return out

    def __str__(self):
        return "Quee"

    def get_moves_between(self, x1: int, y1: int, x2: int, y2: int) -> list[tuple[int, int]]:
        return []


class Knight(Piece):
    def get_moveset(self, x: int, y: int) -> list[tuple[int, int]]:
        return [(x + 1, y + 2),
                (x + 2, y + 1),
                (x + 2, y - 1),
                (x + 1, y - 2),
                (x - 1, y - 2),
                (x - 2, y - 1),
                (x - 2, y + 1),
                (x - 2, y + 2)]

    def __str__(self):
        return "Knig"

    def get_moves_between(self, x1: int, y1: int, x2: int, y2: int) -> list[tuple[int, int]]:
        return []


class Pawn(Piece):
    def __init__(self):
        self.has_moved: bool = False

    def get_moveset(self, x: int, y: int) -> list[tuple[int, int]]:
        out = [(x, y + 1), (x + 1, y + 1), (x - 1, y + 1)]
        if not self.has_moved:
            out.append((x, y + 2))
        return out

    def __str__(self):
        return "Pawn"

    def get_moves_between(self, x1: int, y1: int, x2: int, y2: int) -> list[tuple[int, int]]:
        return []


class Rook(Piece):
    def get_moveset(self, x: int, y: int) -> list[tuple[int, int]]:
        out: list[tuple[int, int]] = []
        for mod in range(-7, 8):
            if mod == 0: continue
            out.append((x + mod, y))
            out.append((x, y + mod))
        return out

    def __str__(self):
        return "Rook"

    def get_moves_between(self, x1: int, y1: int, x2: int, y2: int) -> list[tuple[int, int]]:
        pass
class Bishop(Piece):
    def get_moveset(self, x: int, y: int) -> list[tuple[int, int]]:
        out: list[tuple[int, int]] = []
        for mod in range(-7, 8):
            if mod == 0: continue
            out.append((x + mod, y + mod))
            out.append((x - mod, y + mod))
            out.append((x + mod, y - mod))
            out.append((x - mod, y - mod))
        return out

    def __str__(self):
        return "Bish"

    def get_moves_between(self, x1: int, y1: int, x2: int, y2: int) -> list[tuple[int, int]]:
        return []
