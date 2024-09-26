import colorama

from chess.pieces import Color


class Field:
    def __init__(self, piece=None):
        self.piece = piece

    def get_piece_name(self):
        if not self.piece:
            return "____"
        # return colorama.Fore.BLACK if self.piece.color == Color.BLACK else colorama.Fore.WHITE + str(self.piece) + colorama.Fore.RESET
        return str(self.piece)
