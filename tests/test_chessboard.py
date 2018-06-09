import unittest

from src.chess_board import ChessBoard
from src.pawn import Pawn
from src.piece_color import PieceColor


class ChessBoardTest(unittest.TestCase):
    def setUp(self):
        super().setUp()

        self.chess_board = ChessBoard()

    def test_has_max_board_width_of_8(self):
        assert self.chess_board.MAX_BOARD_HEIGHT == 8

    def test_has_max_board_height_of_8(self):
        assert self.chess_board.MAX_BOARD_WIDTH == 8

    def test_lower_left_corner_is_valid_position(self):
        is_valid = self.chess_board.is_legal_board_position(0, 0)
        assert is_valid == True

    def test_upper_right_corner_is_valid_position(self):
        is_valid = self.chess_board.is_legal_board_position(7, 7)
        assert is_valid == True

    def test_position_out_of_bounds_east_is_invalid(self):
        is_valid = self.chess_board.is_legal_board_position(11, 5)
        assert is_valid == False

    def test_position_out_of_bounds_north_is_invalid(self):
        is_valid = self.chess_board.is_legal_board_position(5, 9)
        assert is_valid == False

    def test_that_avoids_duplicate_positioning(self):
        first_pawn = Pawn(PieceColor.BLACK)
        second_pawn = Pawn(PieceColor.BLACK)
        self.chess_board.add(first_pawn, 6, 3, PieceColor.BLACK)
        self.chess_board.add(second_pawn, 6, 3, PieceColor.BLACK)

        assert first_pawn.x_coordinate == 6
        assert first_pawn.y_coordinate == 3
        assert second_pawn.x_coordinate == -1
        assert second_pawn.y_coordinate == -1

    def test_limits_the_number_of_pawns(self):
        for count in range(10):
            pawn = Pawn(PieceColor.BLACK)
            row = count / self.chess_board.MAX_BOARD_WIDTH
            self.chess_board.add(
                pawn,
                count,
                count % self.chess_board.MAX_BOARD_WIDTH,
                PieceColor.BLACK,
            )

            if row < 1:
                assert pawn.x_coordinate == count
                assert pawn.y_coordinate == count % self.chess_board.MAX_BOARD_WIDTH
            else:
                assert pawn.x_coordinate == -1
                assert pawn.y_coordinate == -1