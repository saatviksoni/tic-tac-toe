"""
Tic Tac Toe Player
"""

import copy
import math

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
    num_moves = 0
    for row in board:
        for move in row:
            if move is not EMPTY:
                num_moves += 1
    if terminal(board):
        return None
    elif num_moves % 2 == 0:
        return X
    else:
        return O
    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    set_actions = set()
    index_row = 0
    index_column = 1
    for row in board:
        index_column = 0
        for column in row:
            if column is EMPTY:
                set_actions.add((index_row, index_column))
            index_column += 1
        index_row += 1
    return set_actions
            

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_cpy = copy.deepcopy(board)
    move = player(board)
    i, j = action
    if board_cpy[i][j] is not EMPTY:
        raise NotImplementedError
    board_cpy[i][j] = move
    return board_cpy



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winner = None
    for row in range(0, 3):
        if (board[row][0] == board[row][1] == board[row][2]) and board[row][0] is not EMPTY: # Check for winner in rows
            winner = board[row][0]
            
    for col in range(0,3):
         if (board[0][col] == board[1][col] == board[2][col]) and board[0][col] is not EMPTY: # Check for winner in columns
            winner = board[0][col]
            
    if (board[0][0] == board[1][1] == board[2][2]) and board[0][0] is not EMPTY: # Check for winner in left to right diagnol
        winner = board[0][0]
    
    if (board[0][2] == board[1][1] == board[2][0]) and board[0][2] is not EMPTY: # Check for winner in right to left diagnol
        winner = board[0][2]
    return winner


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None: # If winner exits board is terminal
        return True
    for row in board:    #   Returns True if board is fully filled with no winners
        for col in row:
            if col is None:
                return False
    return True
def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            trash_value, action = max_value(board)
            return action
        else:
            trash_value, action = min_value(board)
            return action
        

def max_value(board):
    if terminal(board):
        return utility(board), None
    v = -math.inf
    move = None
    for action in actions(board):
        value, trash_action = min_value(result(board, action))
        if value > v:
            v = value
            move = action
            if v == 1:
                return v, move
    return v, move


def min_value(board):
    if terminal(board):
        return utility(board), None
    v = math.inf
    move = None
    for action in actions(board):
        value, trash_action = max_value(result(board, action))
        if value < v:
            v = value
            move = action
            if v == -1:
                return v, move
    return v, move
        
    


