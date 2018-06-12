# Chess Python

## Python3.6


### Current State Of Project

**Changes to project so far documented in CHANGELOG.md.**

The project currently has a class ChessGame that acts as the public interface for the game with four public methods: new_game, restore_game, add and move. This class is responsible for checking if board positions are valid and raising any errors. The chess pieces inherit from a GamePiece Abstract Base Class and are responsible for knowing their own move/capture logic but not physically moving themselves. These are placed in a game_pieces package inside the main src package.


### Suggestions For Future Implementations

#### Short-term

* ChessGame is getting too unwieldy and could be refactored into two classes. Something like ChessGame for the public methods and higher level functionality and GameState for keeping track of pieces' board positions and the lower level move checking.
* The chess board could be refactored to a dict of lists, better representing a physical board.
```python
	board = {char: [None] * 8 for _ in range(8) for char in 'ABCDEFGH'}
```
