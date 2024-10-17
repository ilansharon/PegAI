# Depth-First Searching Algorithm

from game import Board, Move
from randomStrategy import getRandomStart
def DFS(board, path):
    if board.getNumFull() == 1:     # if reached goal
        return True, path

    moves = board.findAllValidMoves()

    if len(moves) == 0:    # if no possible moves
        return False, path
    for move in moves:
        move.executeMove(board)
        final, newPath = DFS(board, path + [move])   #recursion
        if final:
            return True, newPath
        move.undoMove(board)

    return False, path

def playDFS(size):
    board = Board(size)
    startLoc = getRandomStart(size)   #start randomly, starting move not implemented in DFS
    board.startingMove(startLoc)
    print("started at: ", startLoc)

    
    success, winPath = DFS(board, [])
    for move in winPath:
        move.executeMove(board)
        
    return success, board.getNumFull(), len(winPath), winPath


  


