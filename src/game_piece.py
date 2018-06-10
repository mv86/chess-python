"""GamePiece Abstract Base Class."""
from abc import ABC, abstractmethod


class GamePiece(ABC):
    """Base class for game pieces.
       Two required methods:
            move()
            capture()
    """
    def __init__(self):
        self.type = self.__class__.__name__
        self.color = None
        self.x_coordinate = None
        self.y_coordinate = None

    def __repr__(self):
        return f'{self.type}({self.color!r})'

    def __str__(self):
        return (f'{self.color.title()} {self.type}: '
                f'x_coord = {self.x_coordinate}, y_coord = {self.y_coordinate}')

    @abstractmethod
    def valid_move(self):
        pass

    @abstractmethod
    def valid_capture(self):
        pass