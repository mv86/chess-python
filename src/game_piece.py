"""GamePiece Abstract Base Class."""
from abc import ABC, abstractmethod


class GamePiece(ABC):
    """Base class for game pieces.
       Two required methods:
            move()
            attack()
    """
    def __init__(self):
        self.type = self.__class__.__name__

    def __repr__(self):
        return f'{self.type}({self.color!r})'

    def __str__(self):
        return (f'{self.color.title()} {self.type}: '
                f'x_pos = {self.x_position}, y_pos = {self.y_position}')

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def capture(self):
        pass