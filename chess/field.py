import colorama

from chess.pieces import Color


class Field:
    def __init__(self, piece=None):
        self.piece = piece

    def get_piece_name(self):
        if not self.piece:
            return "____"
        # print(f"Piece: {colorama.Fore.GREEN}{self.piece}{colorama.Fore.RESET}")
        # return colorama.Fore.BLACK if self.piece.color == Color.BLACK else colorama.Fore.WHITE + str(self.piece)
        if self.piece.color == Color.BLACK:
            return colorama.Fore.BLACK + str(self.piece) + colorama.Fore.RESET
        if self.piece.color == Color.WHITE:
            return colorama.Fore.WHITE + str(self.piece) + colorama.Fore.RESET
        return str(self.piece)
