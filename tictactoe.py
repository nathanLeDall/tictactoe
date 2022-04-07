"""
Tic Tac Toe Player
"""

import math
from queue import Empty
from shutil import move
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board==initial_state():
        return X
    tmp = sum(board,[])
    x = tmp.count(X)
    o = tmp.count(O)
    return X if x==o else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]==EMPTY:
                moves.add((i,j))
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    tmp = deepcopy(board)
    x,y = action
    if board[x][y] != EMPTY:
        raise OSError
    tmp[x][y] = X if player(board)==X else O
    return tmp
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    return (
        X if  board[0].count(X) == 3 else 
        X if  board[1].count(X) == 3 else
        X if  board[2].count(X) == 3 else
        O if  board[0].count(O) == 3 else 
        O if  board[1].count(O) == 3 else
        O if  board[2].count(O) == 3 else
        X if board[0][0] == X and board[1][1] == X and board[2][2] == X else
        X if board[2][0] == X and board[1][1] == X and board[0][2] == X else
        O if board[0][0] == O and board[1][1] == O and board[2][2] == O else
        O if board[2][0] == O and board[1][1] == O and board[0][2] == O else
        X if board[0][0] == X and board[1][0] == X and board[2][0] == X else
        O if board[0][0] == O and board[1][0] == O and board[2][0] == O else
        X if board[0][1] == X and board[1][1] == X and board[2][1] == X else
        O if board[0][1] == O and board[1][1] == O and board[2][1] == O else
        X if board[0][2] == X and board[1][2] == X and board[2][2] == X else
        O if board[0][2] == O and board[1][2] == O and board[2][2] == O else
        None
    )


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) or actions(board)==set():
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    return 1 if winner(board)==X else -1 if winner(board) == O else 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    best = 0
    move = None
    if player(board)==X:
        best=-1000000
        for moves in actions (board):
            #tmp = Min_Val(board)
            tmp =  Min_Val(result(board,moves))
            if tmp> best:
                best = tmp
                move = moves
    else:
        best = 1000000
        for moves in actions(board):
            #tmp = Max_Val(board)
            tmp = Max_Val(result(board, moves))
            if tmp < best:
                best = tmp
                move = moves
    return move

    
def Max_Val(board):
    if terminal(board):
        return utility(board)
    v = -999999999999999
    for action in actions(board):
        v = max(v,Min_Val(result(board,action)))
    return v

def Min_Val(board):
    if terminal(board):
        return utility(board)
    v = 999999999999999
    for action in actions(board):
        v = min(v,Max_Val(result(board,action)))
    return v
 