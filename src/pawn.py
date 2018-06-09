from src.game_piece import GamePiece


class Pawn(GamePiece):
    def __init__(self, piece_color):
        super().__init__()
        self._piece_color = piece_color
        self._chess_board = None
        self._x_coordinate = None
        self._y_coordinate = None

    @property
    def chess_board(self):
        return self._chess_board

    @chess_board.setter
    def chess_board(self, value):
        self._chess_board = value

    @property
    def x_coordinate(self):
        return self._x_coordinate

    @x_coordinate.setter
    def x_coordinate(self, value):
        self._x_coordinate = value

    @property
    def y_coordinate(self):
        return self._y_coordinate

    @y_coordinate.setter
    def y_coordinate(self, value):
        self._y_coordinate = value

    @property
    def piece_color(self):
        return self._piece_color

    @piece_color.setter
    def piece_color(self, value):
        self.piece_color = value

    def move(self, movement_type, new_x, new_y):
        raise NotImplementedError()

    def capture(self):
        pass
