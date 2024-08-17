# writing some simple instructions for the computer to play the game by choosing random moves
# mostly for testing/experimentation purposes, to ensure that the computer can succesfully complete games
import random
from game import Board, Move

def playRandomly(boardSize):
    gameBoard = Board(boardSize)

    startLoc = getRandomStart(boardSize)
    print("starting location: ", startLoc)
    gameBoard.startingMove(startLoc)

    potentials = gameBoard.findAllValidMoves()

    while len(potentials) != 0:
        currentMove = chooseRandomMove(potentials)
        print("moving at: ", currentMove.start, currentMove.end)
        currentMove.executeMove(gameBoard)
        potentials = gameBoard.findAllValidMoves()

    #end of loop indicates end of game, no more potential moves

    score = gameBoard.getScore()
    numFull = gameBoard.getNumFull()

    return score, numFull


def chooseRandomMove(potentials):
    choice = random.randrange(0, len(potentials))
    move = potentials[choice]
    return move

def getRandomStart(size):
    row = random.randrange(0, size)
    col = random.randrange(0, row + 1)
    return (row, col)



