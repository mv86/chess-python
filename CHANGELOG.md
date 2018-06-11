# Project Changelog

### 09/06/2018

**Removed PieceColor from add() function parameters.**

*Reason:* Redundant as piece_color already included with passed piece.


**Renamed ChessBoard.pieces to board, created a dict of defaultdicts for pieces.**

*Reason:* Board better represented what it was. The defaultdicts of pieces helped with the 'not adding too many pieces' logic.


**Created GamePiece abstract base class.**

*Reason:* Keeps boilerplate for instantiating piece classes in one place. Enforces that all child classes use both abstract methods.


**Replaced PieceColor enum when instantiating piece objects with enforced color keyword argument.**

*Reason:* Felt that color name is better utilised for later logic, using enforced keyword argument keeps it obvious what color piece is being instantiated.


**Removed reference to board and @property getters and setters from Pawn class.**

*Reason:* Felt wrong that the Pawn would know about the board when it was instantiated. Felt unpythonic to have the @property getters and setters without them adding anything. Can be added back later if the need arises. 


### 10/06/2018

**Changed all function calls to expect a Coords(x, y) namedtuple rather than seperate coordinates.**

*Reason:* Felt coords represented one place on the board and should be passed around together. Namedtuple enforces readability: coords.x == 1 better than coords[0] == 1.


**Piece coordinates now revert back to None (replacing -1) if they are taken or not placed on the board because of an error.**

*Reason:* Didn't add any functionality and helps keep the code cleaner.


**Created three game exceptions: NotOnBoardError, PieceNotFoundError, InvalidMoveError**

*Reason:* Express the infomation I want to return from the GameBoard interface if any exceptions raised.


**Created game_pieces package to hold all the game_piece modules.**

*Reason:* Will improve project organisation when all pieces have been implemented.


### 11/06/2018

**Removed MovementType enum and module.**

*Reason:* Have used following logic: If to_coordinates is occupied then move is capture, else move is move. MovementType not required.


**Renamed ChessBoard class to ChessGame.**

*Reason:* Better represents what it is. Has more responsibilities than just a board.
