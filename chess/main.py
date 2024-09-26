from tempfile import gettempdir

import colorama

from chess.exceptions import InvalidMoveException
from chess.field import Field
from chess.pieces import Rook, Knight, Bishop, Queen, King, Pawn, Piece, Color


class Board:
    def __init__(self):
        self.grid = [
            [Field(Rook(Color.BLACK)), Field(Knight(Color.BLACK)), Field(Bishop(Color.BLACK)),
             Field(Queen(Color.BLACK)),
             Field(King(Color.BLACK)), Field(Bishop(Color.BLACK)), Field(Knight(Color.BLACK)),
             Field(Rook(Color.BLACK))],
            [Field(Pawn(Color.BLACK)) for _ in range(8)],
            [Field() for _ in range(8)],
            [Field() for _ in range(8)],
            [Field() for _ in range(8)],
            [Field() for _ in range(8)],
            [Field(Pawn(Color.WHITE)) for _ in range(8)],
            [Field(Rook(Color.WHITE)), Field(Knight(Color.WHITE)), Field(Bishop(Color.WHITE)),
             Field(Queen(Color.WHITE)),
             Field(King(Color.WHITE)), Field(Bishop(Color.WHITE)), Field(Knight(Color.WHITE)),
             Field(Rook(Color.WHITE))],
        ]

    def print_board(self):
        grid = self.grid
        print("  ", end="")
        for i in range(8):
            print(chr(ord("A") + i), end="    ")
        print()
        for index, row in enumerate(grid):
            print(index + 1, end=" ")
            for field in row:
                print(field.get_piece_name(), end=" ")
            print()
        print("  ", end="")

    def is_valid_move(self, pre_x: int, pre_y: int, post_x: int, post_y: int) -> bool:
        pre_field = self.get_field(pre_x, pre_y)
        # print(f"Start piece: {pre_field.piece}")
        post_field = self.get_field(post_x, post_y)
        # print(f"End piece: {post_field.piece}")

        if pre_field.piece is None:
            # print("pre piece not exists")
            raise InvalidMoveException()
        if post_field.piece is not None:
            # print("end has a piece already")
            raise InvalidMoveException()

        moves = pre_field.piece.get_moveset(pre_x, pre_y)
        # print(moves)
        # print(pre_field.piece.color)
        if (post_x, post_y) not in moves:
            # print("move is not in piece moves")
            raise InvalidMoveException()

        moves_between = self.get_field(pre_x, pre_y).piece.get_moves_between(pre_x, pre_y, post_x, post_y)
        for x_move, y_move in moves_between:
            if self.get_field(x_move, y_move) is not None:
                # print("a field is occupied")
                raise InvalidMoveException()

        return True

    def make_move(self, pre_x, pre_y, post_x, post_y):
        if not board.is_valid_move(pre_x, pre_y, post_x, post_y): return
        # TODO: make a capture notification
        board.get_field(post_x, post_y).piece = board.get_field(pre_x, pre_y).piece
        board.get_field(pre_x, pre_y).piece = None

    def get_field(self, x: int, y: int) -> Field:
        return self.grid[y][x]

    def get_field_from_notation(self, x, y):
        return self.grid[y - 1][x - 1]  # this will work for player interaction

    def get_tuple_notaion(self, letter, number):
        x = ord(letter) - ord("A")
        y = number - 1
        return x, y

    def get_better_tuple_notation(self, notation: str):
        letter = notation[0]
        number = int(notation[1])
        return self.get_tuple_notaion(letter, number)


board = Board()
board.print_board()
board.make_move(*board.get_tuple_notaion("D", 7), *board.get_tuple_notaion("D", 6))
board.print_board()
