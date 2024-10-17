from game import Board, Move
from randomStrategy import playRandomly
from DFS import playDFS


# testBoard = Board(5)
# print(testBoard.getScore())
# print(testBoard.board)

# testBoard.startingMove((0,0))


# print(testBoard.board)

# testMove = Move((2,0), (0,0))
# print("start coordinate: ", testMove.start)
# print("middle coordinate: ", testMove.middle)
# print("end coordinate: ", testMove.end)
# print("move type: ", testMove.classifyMove())
# print("within range?: ", testMove.isWithinRange())
# print("is valid?: ", testMove.validateMove(testBoard))
# testMove.executeMove(testBoard)
# print(testBoard.board)
# allvalid = testBoard.findAllValidMoves()
# for i in allvalid:
#     print("move: , ", i.start, i.end)



#print("is start on board?: ", testBoard.isOnBoard(testMove.start))
#print("is end on board?", testBoard.isOnBoard(testMove.end))
#print("is middle on board?", testBoard.board[testMove.start[0]][testMove.start[1]])                               
#print(testBoard.board[testMove.middle[0]][testMove.middle[1]])
#print(testBoard.board[testMove.end[0]][testMove.end[1]])    


def testRandomGame(size):
    print("testing random game with size: ", size)
    score, numFull = playRandomly(size)
    print("your score is: ", score)
    print("number of pins remaining: ", numFull)
    return numFull

# bestScore = 10
# attempts = 0
# while bestScore > 1:
#     thisScore = testRandomGame(7)
#     if thisScore < bestScore:
#         bestScore = thisScore

#     attempts += 1
# print("number of attempts to best score: ", attempts)

success, numFull, numMoves, winPath= playDFS(7)
print(success, numFull, numMoves)
for i in winPath:
    print(i.start, i.end)

            


    


    
                 