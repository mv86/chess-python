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
        self.x_coord = None
        self.y_coord = None

    def __repr__(self):
        return f'{self.type}({self.color!r})'

    def __str__(self):
        return (f'{self.color.title()} {self.type}: '
                f'x_coord = {self.x_coord}, y_coord = {self.y_coord}')

    @abstractmethod
    def valid_move(self, coords):
        """Confirm if move supported by this piece. Return bool."""
        raise NotImplementedError() 

    @abstractmethod
    def valid_capture(self, coords):
        """Confirm if capture supported by this piece. Return bool."""
        raise NotImplementedError() 
