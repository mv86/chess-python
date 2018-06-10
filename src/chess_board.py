from collections import defaultdict

# from src.piece_color import PieceColor


class ChessBoard():
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
        if self._legal_board_position(coords) and not self._max_quantity(piece):
            self.pieces[piece.color][piece.type] += 1
            self._place(piece, coords)


    # def move(self, from_coords, to_coords):
    #     if not self._coords_on_board(from_coords):
    #         # TODO raise NotOnBoardError('From coordinates not valid board coordinates')
    #         return False
        
    #     if not self._coords_on_board(from_coords):
    #         # TODO raise NotOnBoardError('To coordinates not valid board coordinates')
    #         return False

    #     piece = self.board[from_coords.x][from_coords.y]
    #     if not piece:
    #         # TODO raise PieceNotFoundError('No piece found at from coordinates')
    #         return False

    #     if self._pieces_blocking_move(piece, to_coords):
    #         #TODO raise InvalidMoveError('Piece blocking this move')
    #         return False

    #     if not self._valid_piece_move(piece, to_coords):
    #         #TODO raise InvalidMoveError('Invalid move for this piece')
    #         return False
        
    #     self._place(piece, to_coords)
    #     return True

    def _coords_on_board(self, coords):
        if (coords.x not in range(self.MAX_BOARD_WIDTH) 
                or coords.y not in range(self.MAX_BOARD_HEIGHT)):
            return False
        return True

    def _pieces_blocking_move(self, piece, coords):
        if piece.type == 'Knight': 
            return False  # Knight can jump over pieces
        # TODO Implement
        return False


    def _valid_piece_move(self, piece, coords):
        if self.board[coords.x][coords.y] is None:
            return piece.valid_move()
        return piece.valid_capture()

    def _place(self, piece, coords):
        """Clear current postion and place piece on new coordinates."""
        self._clear_current_position(piece)
        self.board[coords.x][coords.y] = piece
        piece.x_coordinate = coords.x
        piece.y_coordinate = coords.y

    def _legal_board_position(self, coords):
        """Check passed coordinates are valid. Return bool."""
        try:
            if self.board[coords.x][coords.y] is None:
                return True
            return False
        except IndexError:  # Not on ChessBoard
            return False

    def _max_quantity(self, piece):
        """Check quantity of passed piece on board. Return bool."""
        return self.pieces[piece.color][piece.type] >= self.MAX_PIECES[piece.type]

    def _clear_current_position(self, piece):
        try:
            self.board[piece.x_coordinate][piece.y_coordinate] = None
        except TypeError:  # Piece not yet on game board
            pass
