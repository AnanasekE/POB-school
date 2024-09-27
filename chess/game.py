# from chess.exceptions import PieceBeatenException
from chess.main import Board
from chess.pieces import Color


class Game:
    def __init__(self):
        self.board = Board()
        self.next_player = Color.WHITE

    def next_turn(self):
        if self.next_player == Color.WHITE:
            self.next_player = Color.BLACK
        else:
            self.next_player = Color.WHITE

    def handle_move(self):
        from_notation = input()
        to_notation = input()
        from_pos = self.board.get_better_tuple_notation(from_notation)
        to_pos = self.board.get_better_tuple_notation(to_notation)
        # try:
        self.board.make_move(*from_pos, *to_pos)
        # except PieceBeatenException as pbe:
        #     print(f"{pbe.piece.__str__()} has been beaten")
        #     pass
        self.board.print_board()


game = Game()
game.board.print_board()
while True:
    # game.board.print_board()
    if game.next_player == Color.WHITE:
        print("White Player Time")
    else:
        print("Black Player Time")

    game.handle_move()
    game.next_turn()
