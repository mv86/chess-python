class ChessBoard:
    MAX_BOARD_WIDTH = 8
    MAX_BOARD_HEIGHT = 8

    def __init__(self):
        self.pieces = [[None] * 8 for _ in range(8)]

    def add(self, pawn, x_coordinate, y_coordinate, piece_color):
        raise NotImplementedError()

    def is_legal_board_position(self, x_coordinate, y_coordinate):
        raise NotImplementedError()
