import chess
import chess.engine
import chess.svg

import pygame
import numpy
import random

import io

from board import ChessGame

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
    print("WORK IN PROGRESS")



if __name__ == '__main__':
    board = random_board()
    listed_board = [[s.strip() for s in line.split(' ') if s] for line in str(board).split('\n') if line]
    print(board)
    print(listed_board)
    print('________')
    print('SCORE:  ')
    print(stockfish_analysis(board,10))

    chess_game = ChessGame(listed_board)
    chess_game.run_game()

    # app = QApplication([])
    # render_board(chess.svg.board(board, size=350))
    # app.exec()