import unittest

from src.chess_board import ChessBoard
from src.movement_type import MovementType
from src.pawn import Pawn
from src.piece_color import PieceColor


class TestPawn(unittest.TestCase):
    def setUp(self):
        super().setUp()

        self.chess_board = ChessBoard()
        self.pawn = Pawn(PieceColor.BLACK)

    def test_that_add_sets_x_coordinates(self):
        self.chess_board.add(self.pawn, 6, 3, PieceColor.BLACK)

        assert self.pawn.x_coordinate == 6

    def test_that_add_Sets_y_coordinate(self):
        self.chess_board.add(self.pawn, 6, 3, PieceColor.BLACK)

        assert self.pawn.y_coordinate == 3

    def test_that_move_illegal_coords_right_does_not_move(self):
        self.chess_board.add(self.pawn, 6, 3, PieceColor.BLACK)
        self.pawn.move(MovementType.MOVE, 7, 3)

        assert self.pawn.x_coordinate == 6
        assert self.pawn.y_coordinate == 3

    def test_that_move_illegal_coords_left_does_not_move(self):
        self.chess_board.add(self.pawn, 6, 3, PieceColor.BLACK)
        self.pawn.move(MovementType.MOVE, 4, 3)

        assert self.pawn.x_coordinate == 6
        assert self.pawn.y_coordinate == 3

    def test_that_move_to_legal_coords_forward_does_move(self):
        self.chess_board.add(self.pawn, 6, 3, PieceColor.BLACK)
        self.pawn.move(MovementType.MOVE, 6, 2)

        assert self.pawn.x_coordinate == 6
        assert self.pawn.y_coordinate == 2