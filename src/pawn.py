from src.game_piece import GamePiece


class Pawn(GamePiece):
    def __init__(self, color):
        super().__init__()
        self._color = color
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
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self.color = value

    def move(self, movement_type, new_x, new_y):
        raise NotImplementedError()

    def capture(self):
        pass
