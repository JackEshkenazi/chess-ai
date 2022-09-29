import sys
import pygame
import os

from sprite_sheet import SpriteSheet
from pygame.locals import (
    MOUSEBUTTONUP,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

from constants import CHESS_PIECES_STARTING_POSITIONS
from sprite_sheet import CHESS_PIECES_SPRITES_ENUM

def get_starting_position(color, name):
    return CHESS_PIECES_STARTING_POSITIONS[str(color) + '_' + str(name)]

def get_piece_image(color, name):
    return CHESS_PIECES_SPRITES_ENUM[str(color) + '_' + str(name)]


class Settings:
    def __init__(self):
        self.screen_width, self.screen_height = 1200, 800
        self.bg_color = (225, 225, 225)
        self.black_square_color = (0,0,0)

class ChessGame:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Chess")

        self.chess_set = ChessBoard(self)

        self.board = [ [(i, j) for i in range(0,8)] for j in range(0,8) ]

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == pygame.K_q or event.key == K_ESCAPE:
                    sys.exit()
            elif event.type == MOUSEBUTTONUP:
                print(pygame.mouse.get_pos())

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)

        # Draw chess board
        for row in self.board:
            for square in row:
                surf = pygame.Surface((100,100))
        
                if square[0] % 2 == 0 and square[1] % 2 != 0:
                    surf.fill((0, 0, 0))
                elif square[1] % 2 == 0 and square[0] % 2 != 0:
                    surf.fill((0, 0, 0))
                else:
                    surf.fill((255, 255, 255))
        
                rect = surf.get_rect()
                self.screen.blit(surf, (square[0] * 100, square[1] * 100))

        # Draw all pieces
        for piece in self.chess_set.pieces:
            piece.blitme()

        pygame.display.update()

class ChessBoard:
    ''' 
    Represents a specific board configuration.
    Each piece is an object of the Piece class.
    '''

    def __init__(self, chess_game):
        """Initialize attributes to represent the overall set of pieces."""

        self.chess_game = chess_game
        self.pieces = []
        self._load_pieces()

    def _load_pieces(self):
        # Create a Piece for each image.
        colors = ['black', 'white']
        names = ['king', 'queen', 'rook', 'bishop', 'knight', 'pawn']

        piece_num = 0
        for color in colors:
            for name in names:
                starting_positions = get_starting_position(color, name)
                print(starting_positions)
                for starting_position in starting_positions:
                    piece = Piece(self.chess_game, color=color, name=name, position=starting_position)
                    piece.name = name
                    piece.color = color
                    self.pieces.append(piece)

                    piece_num += 1

class Piece:
    """Represents a chess piece."""

    def __init__(self, chess_game, name, color, position):
        """Initialize attributes to represent a chess piece."""
        self.image = self.image_from_name(color, name)
        self.name = name
        self.color = color
        self.position = position

        self.screen = chess_game.screen

        self.x, self.y = self.coordinates_from_position(position)

    def coordinates_from_position(self, position):
        return (55 + 100 * position[1], 50 + 100 * position[0])

    def image_from_name(self, color, name):
        sprite_sheet = SpriteSheet(get_piece_image(color, name))
        image = sprite_sheet.image_at([0,0,142,128])

        return pygame.transform.smoothscale(image, (80, 80))


    def blitme(self):
        """Draw the piece at its current location."""
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
        self.screen.blit(self.image, self.rect)

if __name__ == '__main__':
    chess_game = ChessGame()
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