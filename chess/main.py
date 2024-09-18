from chess.field import Field
from chess.pieces import Rook, Knight, Bishop, Queen, King, Pawn, Piece


class Board:
    def __init__(self):
        self.grid = [
            # First row: Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook
            [Field(Rook()), Field(Knight()), Field(Bishop()), Field(Queen()),
             Field(King()), Field(Bishop()), Field(Knight()), Field(Rook())],
            # Second row: Pawns
            [Field(Pawn()) for _ in range(8)],
            # Rows 3 to 8: Empty fields
            [Field() for _ in range(8)],
            [Field() for _ in range(8)],
            [Field() for _ in range(8)],
            [Field() for _ in range(8)],
            [Field() for _ in range(8)],
            [Field() for _ in range(8)]
        ]

    def print_board(self):
        grid = self.grid
        grid.reverse()
        for index, row in enumerate(grid):
            print(7 - index + 1, end=" ")
            for field in row:
                print(field.get_piece_name(), end=" ")
            print()
        print("  ", end="")
        for i in range(8):
            print(chr(ord("A") + i), end="    ")

    def is_valid_move(self, pre_x: int, pre_y: int, post_x: int, post_y: int) -> bool:
        pre_field = self.get_field_for_pos(pre_x, pre_y)
        post_field = self.get_field_for_pos(post_x, post_y)
        if pre_field.piece is not Piece:
            return False
        if post_field.piece is not None:
            return False
        moves = pre_field.piece.get_moveset()
        if (post_x, post_y) not in moves:
            return False
        # TODO check for collisions

        return True


    def get_field_for_pos(self, x: int, y: int) -> Field:
        return self.grid[y][x]


board = Board()
board.print_board()
# print(board.get_field_for_pos(7, 6).piece)
