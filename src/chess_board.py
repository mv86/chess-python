from collections import defaultdict

from src.piece_color import PieceColor


class ChessBoard:
    MAX_BOARD_WIDTH = 8
    MAX_BOARD_HEIGHT = 8
    MAX_PIECES = {
        'Pawn': 8,
        'Knight': 2,
        'Bishop': 2,
        'Rook': 2,
        'Queen': 1,
        'King': 1
    }

    def __init__(self):
        self.board = [[None] * 8 for _ in range(8)]
        self.pieces = {
            PieceColor.WHITE: defaultdict(int),
            PieceColor.BLACK: defaultdict(int)
        }

    def add(self, piece, x_coordinate, y_coordinate):
        """Add piece to board at given coordinates. Modify piece coordinates."""
        if (self.is_legal_board_position(x_coordinate, y_coordinate)
                and not self.max_qunatity_reached(piece)):
            self.board[x_coordinate][y_coordinate] = piece
            self.pieces[piece.color][piece.type] += 1
            piece.x_coordinate = x_coordinate
            piece.y_coordinate = y_coordinate
        else:
            piece.x_coordinate = -1
            piece.y_coordinate = -1

    def is_legal_board_position(self, x_coordinate, y_coordinate):
        """Check passed coordinates are valid. Return bool."""
        try:
            if self.board[x_coordinate][y_coordinate] is None:
                return True
            return False
        except IndexError:  # Not on ChessBoard
            return False


    def max_qunatity_reached(self, piece):
        """Check quantity of passed piece on board. Return bool."""
        return self.pieces[piece.color][piece.type] < self.MAX_PIECES[piece.type]
