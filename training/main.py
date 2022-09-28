import chess
import chess.engine
import chess.svg

import pygame
import numpy
import random

import io
#import cairosvg

from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication, QWidget

def random_board(max_depth = 200):
    board = chess.Board()
    depth = random.randrange(0, max_depth)

    for search in range(depth):
        all_legal_moves = list(board.legal_moves)
        random_move = random.choice(all_legal_moves)
        board.push(random_move)
        if board.is_game_over():
            break

    return board

def stockfish_analysis(board, depth):
    with chess.engine.SimpleEngine.popen_uci('./content/stockfish') as sf:
        result = sf.analyse(board, chess.engine.Limit(depth=depth))
        score = result['score'].white().score()

        return score

def render_board(svg):
    # svg = cairosvg.svg2svg(svg, dpi = (DPI / scale))
    # bytes = cairosvg.svg2png(svg)
    # byte_io = io.BytesIO(bytes)
    # return pygame.image.load(byte_io)

    widgetSvg = QSvgWidget()
    widgetSvg.setGeometry(10, 10, 1080, 1080)
    widgetSvg.load(svg)



if __name__ == '__main__':
    board = random_board()
    print(board)
    print('________')
    print('SCORE:  ')
    print(stockfish_analysis(board,10))

    # app = QApplication([])
    # render_board(chess.svg.board(board, size=350))
    # app.exec()