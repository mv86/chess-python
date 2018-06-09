import unittest

from src.chess_board import ChessBoard
# from src.movement_type import MovementType
from src.pawn import Pawn
from src.piece_color import PieceColor


class TestPawn(unittest.TestCase):
    def setUp(self):
        super().setUp()

        self.chess_board = ChessBoard()
        self.black_pawn = Pawn(color='black')
        self.white_pawn = Pawn(color='white')

    def test_that_add_sets_x_coordinates(self):
        self.chess_board.add(self.black_pawn, 6, 3)

        assert self.black_pawn.x_coordinate == 6

    def test_that_add_Sets_y_coordinate(self):
        self.chess_board.add(self.black_pawn, 6, 3)

        assert self.black_pawn.y_coordinate == 3

    def test_that_move_illegal_coords_right_does_not_move(self):
        self.chess_board.add(self.black_pawn, 6, 3)
        self.black_pawn.move(7, 3, self.chess_board)

        assert self.black_pawn.x_coordinate == 6
        assert self.black_pawn.y_coordinate == 3

    def test_that_move_illegal_coords_left_does_not_move(self):
        self.chess_board.add(self.black_pawn, 6, 3)
        self.black_pawn.move(4, 3, self.chess_board)

        assert self.black_pawn.x_coordinate == 6
        assert self.black_pawn.y_coordinate == 3

    def test_that_black_move_to_legal_coords_forward_does_move(self):
        self.chess_board.add(self.black_pawn, 6, 3)
        self.black_pawn.move(6, 2, self.chess_board)

        assert self.black_pawn.x_coordinate == 6
        assert self.black_pawn.y_coordinate == 2

    def test_that_white_move_to_legal_coords_forward_does_move(self):
        self.chess_board.add(self.white_pawn, 6, 4)
        self.white_pawn.move(6, 4, self.chess_board)

        assert self.white_pawn.x_coordinate == 6
        assert self.white_pawn.y_coordinate == 4