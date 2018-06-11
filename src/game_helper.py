"""Module of helper functions for chess game.

   TODO Document functions.
"""
def move_direction(piece, to_coords):
    """Calculate direction from piece to coordinates. Return str."""
    if _diagonal_movement(piece, to_coords):
        direction = 'diagonal'
    elif piece.x_coord != to_coords.x and piece.y_coord == to_coords.y:
        direction = 'horizontal'
    elif piece.y_coord != to_coords.y and piece.x_coord == to_coords.x:
        direction = 'vertical'
    else:
        direction = 'non_linear'
    return direction


def _diagonal_movement(piece, coords):
    """Helper function fro move_direction. Return bool."""
    # TODO Last minute function re-write to fix bug. Can it be improved?
    min_x_coord = min(piece.x_coord, coords.x)
    min_y_coord = min(piece.y_coord, coords.y)
    max_x_coord = max(piece.x_coord, coords.x)
    max_y_coord = max(piece.y_coord, coords.y)
    x_coord_range = list(range(min_x_coord, max_x_coord))
    y_coord_range = list(range(min_y_coord, max_y_coord))
    return len(x_coord_range) == len(y_coord_range)
