from src.game_piece import GamePiece


class Pawn(GamePiece):
    def __init__(self, *, color):
        super().__init__()
        self.color = color

    def valid_move(self, coords):
        # TODO Add first move functionality for two spaces
        if self.color == 'white':
            valid_y_coord = self.y_coord + 1
        elif self.color == 'black':
            valid_y_coord = self.y_coord - 1

        if coords.x == self.x_coord and coords.y == valid_y_coord:
            return True
        return False

    def valid_capture(self, coords):
        pass
