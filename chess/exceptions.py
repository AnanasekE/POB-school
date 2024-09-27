from chess.pieces import Piece


class InvalidMoveException(Exception):
    pass

# class PieceBeatenException(Exception):
#     def __init__(self, piece:Piece):
#         self.piece = piece