from enum import Enum

class CHESS_PIECES_ENUM(Enum):
    white_king = 'K'
    white_queen = 'Q'
    white_bishop = 'B'
    white_knight = 'N'
    white_rook = 'R'
    white_pawn = 'P'
    black_king = 'k'
    black_queen = 'q'
    black_bishop = 'b'
    black_knight = 'n'
    black_rook = 'r'
    black_pawn = 'p'

CHESS_PIECES_STARTING_POSITIONS = {
    'white_king': [(7, 4)],
    'white_queen': [(7, 3)],
    'white_bishop': [(7, 2), (7, 5)],
    'white_knight': [(7, 1), (7, 6)],
    'white_rook': [(7, 0), (7, 7)],
    'white_pawn': [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7)],
    'black_king': [(0, 4)],
    'black_queen': [(0, 3)],
    'black_bishop': [(0, 2), (0, 5)],
    'black_knight': [(0, 1), (0, 6)],
    'black_rook': [(0, 0), (0, 7)],
    'black_pawn': [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7)]
}
