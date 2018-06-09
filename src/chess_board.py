class ChessBoard:
    MAX_BOARD_WIDTH = 8
    MAX_BOARD_HEIGHT = 8

    def __init__(self):
        self.board = [[None] * 8 for _ in range(8)]

    def add(self, pawn, x_coordinate, y_coordinate, piece_color):
        raise NotImplementedError()

    def is_legal_board_position(self, x_coordinate, y_coordinate):
        """Check passed coordinates are valid. Return bool."""
        try:
            if self.board[x_coordinate][y_coordinate] is None:
                return True
            return False
        except IndexError:  # Not on ChessBoard
            return False
