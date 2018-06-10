from src.game_piece import GamePiece


class Pawn(GamePiece):
    def __init__(self, *, color):
        super().__init__()
        self.color = color

    def move(self, new_coords, chess_board):
        if self._valid_move(new_coords, chess_board.board):
            chess_board._place(self, new_coords)
            # self.x_coordinate = new_x_coord
            # self.y_coordinate = new_y_coord

    def capture(self):
        pass

    def _valid_move(self, new_coords, board):
        """Check if move is valid. Return bool."""
        if self.color == 'white':
            valid_y_coord = self.y_coordinate + 1
        elif self.color == 'black':
            valid_y_coord = self.y_coordinate - 1

        if new_coords.x == self.x_coordinate and new_coords.y == valid_y_coord:
            if board[new_coords.x][new_coords.y] is None:
                return True
        return False
