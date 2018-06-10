from collections import defaultdict

# from src.piece_color import PieceColor


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
            'white': defaultdict(int),
            'black': defaultdict(int)
        }

    def add(self, piece, coords):
        """Add piece to board at given coordinates. Modify piece coordinates."""
        if (self.is_legal_board_position(coords)
                and not self.max_qunatity_reached(piece)):
            self.pieces[piece.color][piece.type] += 1
            self.place(piece, coords)
        else:
            piece.x_coordinate = -1
            piece.y_coordinate = -1

    def place(self, piece, coords):
        """Clear current postion and place piece on new coordinates."""
        self._clear_current_position(piece)
        self.board[coords.x][coords.y] = piece
        piece.x_coordinate = coords.x
        piece.y_coordinate = coords.y

    def is_legal_board_position(self, coords):
        """Check passed coordinates are valid. Return bool."""
        try:
            if self.board[coords.x][coords.y] is None:
                return True
            return False
        except IndexError:  # Not on ChessBoard
            return False

    def max_qunatity_reached(self, piece):
        """Check quantity of passed piece on board. Return bool."""
        return self.pieces[piece.color][piece.type] >= self.MAX_PIECES[piece.type]

    def _clear_current_position(self, piece):
        try:
            self.board[piece.x_coordinate][piece.y_coordinate] = None
        except TypeError:  # Piece not yet on game board
            pass
