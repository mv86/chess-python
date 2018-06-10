from collections import defaultdict

from src.game_errors import InvalidMoveError, NotOnBoardError, PieceNotFoundError

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
        """Add piece to board at given coordinates. Update piece to have same coordinates."""
        if self._legal_board_position(coords) and not self._max_quantity(piece):
            self.pieces[piece.color][piece.type] += 1
            self._place(piece, coords)

    def move(self, from_coords, to_coords):
        """TODO"""
        if not self._coords_on_board(from_coords):
            raise NotOnBoardError(from_coords, 'From coordinates not valid board coordinates')

        if not self._coords_on_board(to_coords):
            raise NotOnBoardError(to_coords, 'To coordinates not valid board coordinates')

        piece = self.board[from_coords.x][from_coords.y]
        if not piece:
            raise PieceNotFoundError(from_coords, 'No piece found at from coordinates')

        if from_coords == to_coords:
            raise InvalidMoveError(from_coords, to_coords, 'Move to same square invalid')

        if self._pieces_blocking_move(piece, to_coords):
            raise InvalidMoveError(from_coords, to_coords, 'Piece blocking this move')

        if not self._valid_piece_move(piece, to_coords):
            raise InvalidMoveError(from_coords, to_coords, 'Invalid move for this piece')
        
        # No exceptions raised, safe to move piece
        self._move(piece, to_coords)

    def _move(self, piece, coords):
        """Clear current postion and place piece on new coordinates."""
        # Empty piece current square
        self.board[piece.x_coord][piece.y_coord] = None

        # If move is capture, remove captured piece
        board_postion = self.board[coords.x][coords.y]
        if board_postion is not None:
            captured_piece = board_postion
            captured_piece.x_coord = None
            captured_piece.y_coord = None
            board_postion = None

        # Place piece at new coordinates
        self._place(piece, coords)

    def _place(self, piece, coords):
        self.board[coords.x][coords.y] = piece
        piece.x_coord = coords.x
        piece.y_coord = coords.y

    def _coords_on_board(self, coords):
        if (coords.x not in range(self.MAX_BOARD_WIDTH) 
                or coords.y not in range(self.MAX_BOARD_HEIGHT)):
            return False
        return True

    def _pieces_blocking_move(self, piece, coords):
        if piece.type == 'Knight': # Knight can jump over pieces
            return False

        direction = self._move_direction(piece, coords)

        if direction == 'vertical':
            for num in range(piece.y_coord + 1, coords.y):
                if self.board[piece.x_coord][num] is not None:
                    return True
        elif direction == 'horizontal':
            for num in range(piece.x_coord + 1, coords.x):
                if self.board[num][piece.y_coord] is not None:
                    return True
        elif direction == 'diagonal':
            for num in range(piece.x_coord + 1, coords.x):
                if self.board[num][num] is not None:
                    return True          
        return False

    @staticmethod
    def _move_direction(piece, coords):
        if piece.x_coord != coords.x and piece.y_coord != coords.y:
            direction = 'diagonal'
        elif piece.x_coord != coords.x:
            direction = 'horizontal'
        else:  # piece.y_coord != coords.y
            direction = 'vertical'
        return direction

    def _valid_piece_move(self, piece, coords):
        if self.board[coords.x][coords.y] is None:  # Empty square so move
            return piece.valid_move(coords)
        # Occupied square so capture
        return piece.valid_capture(coords)

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
