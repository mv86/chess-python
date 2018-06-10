from collections import namedtuple
import unittest

from src.chess_board import ChessBoard
from src.pawn import Pawn
from src.game_errors import InvalidMoveError, NotOnBoardError, PieceNotFoundError
# from src.piece_color import PieceColor


class ChessBoardTest(unittest.TestCase):
    def setUp(self):
        super().setUp()

        self.chess_board = ChessBoard()
        self.coords = namedtuple('Coords', 'x y')
        self.move = self.chess_board.move
        self.piece = Pawn(color='black')
        self.blocking_piece = Pawn(color='black')

    def test_has_max_board_width_of_8(self):
        assert self.chess_board.MAX_BOARD_HEIGHT == 8

    def test_has_max_board_height_of_8(self):
        assert self.chess_board.MAX_BOARD_WIDTH == 8

    def test_lower_left_corner_is_valid_position(self):
        coords = self.coords(x=0, y=0)
        assert self.chess_board._legal_board_position(coords)

    def test_upper_right_corner_is_valid_position(self):
        coords = self.coords(x=7, y=7)
        assert self.chess_board._legal_board_position(coords)

    def test_position_out_of_bounds_east_is_invalid(self):
        coords = self.coords(x=11, y=5)
        assert not self.chess_board._legal_board_position(coords)

    def test_position_out_of_bounds_north_is_invalid(self):
        coords = self.coords(x=5, y=9)
        assert not self.chess_board._legal_board_position(coords)

    def test_that_avoids_duplicate_positioning(self):
        first_pawn = Pawn(color='black')
        second_pawn = Pawn(color='black')
        coords = self.coords(x=6, y=3)
        self.chess_board.add(first_pawn, coords)
        self.chess_board.add(second_pawn, coords)

        assert first_pawn.x_coord == 6
        assert first_pawn.y_coord == 3
        assert not second_pawn.x_coord
        assert not second_pawn.y_coord

    def test_limits_the_number_of_pawns(self):
        for count in range(10):
            pawn = Pawn(color='black')
            row = count / self.chess_board.MAX_BOARD_WIDTH
            x_coord = count
            y_coord = count % self.chess_board.MAX_BOARD_WIDTH
            self.chess_board.add(
                pawn,
                self.coords(x=x_coord, y=y_coord)
            )

            if row < 1:
                assert pawn.x_coord == count
                assert pawn.y_coord == count % self.chess_board.MAX_BOARD_WIDTH
            else:
                assert not pawn.x_coord
                assert not pawn.y_coord

    # def test_piece_moved_on_board(self):
    #     pawn = Pawn(color='black')
    #     self.chess_board.add(pawn, self.coords(x=6, y=6))
    #     pawn.move(self.coords(x=6, y=5), self.chess_board)

    #     assert self.chess_board.board[6][6] is None
    #     assert self.chess_board.board[6][5] == pawn
    #     assert pawn.x_coord == 6
    #     assert pawn.y_coord == 5

    #     pawn.move(self.coords(x=6, y=4), self.chess_board)

    #     assert self.chess_board.board[6][5] is None
    #     assert self.chess_board.board[6][4] == pawn
    #     assert pawn.x_coord == 6
    #     assert pawn.y_coord == 4

    def test_invalid_from_coords_raises_exception(self):
        from_coords = self.coords(x=1, y=50)
        to_coords = self.coords(x=1, y=6)
        self.assertRaises(NotOnBoardError, self.move, from_coords, to_coords)

    def test_invalid_to_coords_raises_exception(self):
        from_coords = self.coords(x=1, y=6)
        to_coords = self.coords(x=50, y=7)
        self.assertRaises(NotOnBoardError, self.move, from_coords, to_coords)

    def test_empty_from_coords_raises_exception(self):
        from_coords = self.coords(x=1, y=6)
        to_coords = self.coords(x=1, y=5)
        self.assertRaises(PieceNotFoundError, self.move, from_coords, to_coords)

    def test_same_from_and_to_coords_raise_exception(self):
        self.chess_board.add(self.piece, self.coords(1, 2))
        from_coords = self.coords(x=1, y=2)
        to_coords = self.coords(x=1, y=2)
        self.assertRaises(InvalidMoveError, self.move, from_coords, to_coords)       

    def test_piece_blocking_vertical_move_raises_exception(self):
        self.chess_board.add(self.piece, self.coords(2, 2))
        self.chess_board.add(self.blocking_piece, self.coords(2, 3))
        from_coords = self.coords(2, 2)
        to_coords = self.coords(2, 4)
        self.assertRaises(InvalidMoveError, self.move, from_coords, to_coords)

    def test_piece_blocking_horizontal_move_raises_exception(self):
        # Pretend Pawn is Rook for horizontal test
        self.chess_board.add(self.piece, self.coords(2, 2))
        self.chess_board.add(self.blocking_piece, self.coords(4, 2))
        from_coords = self.coords(2, 2)
        to_coords = self.coords(5, 2)
        self.assertRaises(InvalidMoveError, self.move, from_coords, to_coords)
    
    def test_piece_blocking_diagonal_move_raises_exception(self):
        # Pretend Pawn is Bishop for diagonal test
        self.chess_board.add(self.piece, self.coords(2, 2))
        self.chess_board.add(self.blocking_piece, self.coords(4, 4))
        from_coords = self.coords(2, 2)
        to_coords = self.coords(6, 6)
        self.assertRaises(InvalidMoveError, self.move, from_coords, to_coords)
  
    # def test_invalid_move_for_piece_raises_exception(self):
    #     move = self.chess_board.move
    #     from_coords = self.coords(x=1, y=6)
    #     to_coords = self.coords(x=1, y=5)
    #     self.assertRaises(PieceNotFoundError, move, from_coords, to_coords)

    # def test_invalid_attack_for_piece_raises_exception(self):
    #     move = self.chess_board.move
    #     from_coords = self.coords(x=1, y=6)
    #     to_coords = self.coords(x=1, y=5)
    #     self.assertRaises(PieceNotFoundError, move, from_coords, to_coords)
