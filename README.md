# Chess Python

## Python 3.6


### Current State Of Project

**Changes to project so far are documented in CHANGELOG.md.**

The project currently has a class ChessGame that acts as the public interface for the game with four public methods: new_game, restore_game, add and move that call various internal protected methods. This class is responsible for checking if board positions are valid and raising any errors. The chess pieces inherit from a GamePiece abstract base class and are responsible for knowing their own move/capture logic but not physically moving themselves. These are located in a game_pieces package inside the main src package.


### Suggestions For Future Implementations

#### Short-Term

* ChessGame is getting too unwieldy and could be refactored into two classes. Something like ChessGame for the public methods and higher level functionality and GameState for keeping track of pieces' board positions and the lower level move checking.
* Game pieces currently have two methods valid_move & valid_capture but, apart from the Pawn, the other pieces will have the same logic. These could be refactored into a valid_move method. Alternatively it could be left that these methods call an internal protected _valid method as in the Queen. This would keep the code more extensible to other games i.e. checkers.
* The tests should be refactored to be better in line with the code. More edge cases need to be tested.
* The chess board could be refactored to a dict of lists, better representing a physical board and what the user sees in, for example, the final Flask app. It would also be clearer in method calls (but would need to be (y_coord -1) for the list index). 
```python
# Example board
board = {char: [None] * 8 for _ in range(8) for char in 'ABCDEFGH'}

# Example usage
game.move(from_coords=('A', 1), to_coords=('B', 3))
```
* ChessGame add method should be changed to a protected method called by new_game() and restore_game().

#### Medium-Term

* With the project growing, switching to Pytest for testing could help keep the tests readable and maintainable. Functionality such as using the @pytest.mark.parametrize decorator would help with testing each method with multiple board postions for the edge cases mentioned earlier.
* Type hinting could be used better clarity, reducing the need for documenting method values and helping IDEs' type checkers.
```python
import typing

Coords = typing.NamedTuple("Coords", [('x', int), ('y', int)])

def _coords_on_board(self, coords: Coords) -> bool:
    if (coords.x not in range(self.MAX_BOARD_WIDTH) 
            or coords.y not in range(self.MAX_BOARD_HEIGHT)):
        return False
    return True
```
* Functionality needs to be added for all chess rules. Examples include the fact that no move can lead to putting your own King being in check, Pawn being promoted to new piece, castling the King and Rook etc.
* Functionality needs to be implemented to create new games and restore games. Data needs to be persisted, database, pickling etc.
* Create project loggers that log errors, game movements, player stats etc.
* Need more classes for game functionality, Players?, all other pieces, King, Rook etc.


#### Long-Term

* Finalise game API 
* Create Flask app
* Add integration testing