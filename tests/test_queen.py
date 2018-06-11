"""Test module for Queen game piece."""
from collections import namedtuple
import unittest

from src.chess_game import ChessGame
from src.game_pieces.queen import Queen

class TestQueen(unittest.TestCase):
    """docstring for TestQueen"""
    def setUp(self):
        super().setUp()

        self.chess_game = ChessGame()
        self.queen = Queen(color='black')
        self.coords = namedtuple('Coords', 'x y')
        self.start_coords = self.coords(x=7, y=4)
        self.chess_game.add(self.queen, self.start_coords)

    def test_horizontal_move_valid(self):
        assert self.queen.valid_move(self.coords(x=1, y=4))

    def test_vertical_capture_valid(self):
        assert self.queen.valid_capture(self.coords(x=7, y=6))

    def test_diagonal_move_valid(self):
        assert self.queen.valid_move(self.coords(x=5, y=2))

    def test_nonlinear_move_not_valid(self):
        assert not self.queen.valid_move(self.coords(x=1, y=5))

    def test_nonlinear_capture_not_valid(self):
        assert self.queen.valid_move(self.coords(x=5, y=2))
