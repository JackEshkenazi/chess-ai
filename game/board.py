import sys
import pygame

from sprite_sheet import SpriteSheet

class Settings:

    def __init__(self):
        self.screen_width, self.screen_height = 1200, 800
        self.bg_color = (225, 225, 225)

class ChessSet:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Chess")

        self.chess_set = ChessBoard(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)

        # Draw a row of black pieces.
        for index, piece in enumerate(self.chess_set.pieces[:6]):
            piece.x = index * 100
            piece.blitme()

        # Draw a row of white pieces.
        for index, piece in enumerate(self.chess_set.pieces[6:]):
            piece.x = index * 100
            piece.y = 100
            piece.blitme()

        pygame.display.flip()

class ChessBoard:
    """Represents a set of chess pieces.
    Each piece is an object of the Piece class.
    """

    def __init__(self, chess_game):
        """Initialize attributes to represent the overall set of pieces."""

        self.chess_game = chess_game
        self.pieces = []
        self._load_pieces()

    def _load_pieces(self):
        filename = 'chess_pieces.bmp'
        piece_ss = SpriteSheet(filename)

        # Load all piece images.
        piece_images = piece_ss.load_grid_images(2, 6, x_margin=64,
                x_padding=72, y_margin=68, y_padding=48)

        # Create a Piece for each image.
        colors = ['black', 'white']
        names = ['king', 'queen', 'rook', 'bishop', 'knight', 'pawn']

        piece_num = 0
        for color in colors:
            for name in names:
                piece = Piece(self.chess_game)
                piece.name = name
                piece.color = color
                piece.image = piece_images[piece_num]
                self.pieces.append(piece)

                piece_num += 1

class Piece:
    """Represents a chess piece."""

    def __init__(self, chess_game):
        """Initialize attributes to represent a ches piece."""
        self.image = None
        self.name = ''
        self.color = ''

        self.screen = chess_game.screen

        # Start each piece off at the top left corner.
        self.x, self.y = 0.0, 0.0

    def blitme(self):
        """Draw the piece at its current location."""
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
        self.screen.blit(self.image, self.rect)

if __name__ == '__main__':
    chess_game = ChessSet()
    chess_game.run_game()

# from pygame.locals import (
#     MOUSEBUTTONUP,
#     K_ESCAPE,
#     KEYDOWN,
#     QUIT,
# )
 
# pygame.init()
 
# SCREEN_WIDTH = 700
# SCREEN_HEIGHT = 700
 
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# def calculate_coordinates(x_array, y_array, is_white):
#     if SCREEN_WIDTH < SCREEN_HEIGHT or SCREEN_WIDTH == SCREEN_HEIGHT:
#         width_height = SCREEN_WIDTH / 8
#     else:
#         width_height = SCREEN_HEIGHT / 8
 
#     x_coordinate = x_array * width_height
#     y_coordinate = y_array * width_height
 
#     return BoardSquare(x_coordinate, y_coordinate, width_height, is_white, 'king')

# def get_square_for_position(pos):
#     for row in chess_board:
#         if row[0].y_start < pos[1] < row[0].y_start + row[0].width_height:
#             for square in row:
#                 if square.x_start < pos[0] < square.x_start + square.width_height:
#                     return square


# class BoardSquare:
#     def __init__(self, x_start, y_start, width_height, is_white, piece):
#         self.x_start = x_start
#         self.y_start = y_start
#         self.width_height = width_height
#         self.is_white = is_white
#         self.piece = piece


# chess_board = []
# is_white = False
# for y in range(8):
#     chess_row = []
#     is_white = not is_white
#     for x in range(8):
#         chess_row.append(calculate_coordinates(x, y, is_white))
#         is_white = not is_white
#     chess_board.append(chess_row)


# for row in chess_board:
#     for square in row:
#         surf = pygame.Surface((square.width_height, square.width_height))
 
#         if square.is_white:
#             surf.fill((255, 255, 255))
#         else:
#             surf.fill((0, 0, 0))
 
#         rect = surf.get_rect()
#         screen.blit(surf, (square.x_start, square.y_start))
#         pygame.display.flip()

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == KEYDOWN:
#             if event.key == K_ESCAPE:
#                 running = False
 
#         if event.type == MOUSEBUTTONUP:
#             pos = pygame.mouse.get_pos()
#             #highlight_selected_square(get_square_for_position(pos))
#         elif event.type == QUIT:
#             running = False