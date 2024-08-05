"""
base functionality, handles board and move validity

"""


class Board:
    def __init__(self, size):
        self.size = size
        self.board = self.createFull()

    #creates a full board
    def createFull(self):
        board = []
        for i in range(self.size):
            row = []
            for _ in range(i+1):
                row.append(True)
            board.append(row)
        return board
    
    # function to check if a coordinate falls within the board
    # assumes location is row,col tuple
    def isOnBoard(self, location):
        row, col = location
        return 0 <= row < self.size and 0 <= col <= row
    
    # gets the score of the board
    def getScore(self):
        score = 0
        for row in self.board:
            for spot in row:
                score +=1
                if spot:
                    score -= 1
        return score
    
    def startingMove(self, location):
        if self.isOnBoard(location) and self.board[location[0]][location[1]]:
            self.board[location[0]][location[1]] = False
        else:
            print("ERROR - false starting move")



class Move:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.type = self.classifyMove()
        self.middle = self.getMiddle()

    #changes the board in accordance with move if valid, if not, error
    def executeMove(self, board):
        if self.validateMove(board):
            board.board[self.start[0]][self.start[1]] = False
            board.board[self.middle[0]][self.middle[1]] = False
            board.board[self.end[0]][self.end[1]] = True
        else:
            print("ERROR - invalid move")



        # if valid move:
            # set start to false
            # set middle to false
            # set end to true        

    
    #function to check if a move is possible
    def validateMove(self, board):
        return (self.isWithinRange() and              # valid range
                board.isOnBoard(self.start) and 
                board.isOnBoard(self.end) and       # start and end on board
                board.board[self.start[0]][self.start[1]] and               # start is full
                board.board[self.middle[0]][self.middle[1]] and not          # middle is full
                board.board[self.end[0]][self.end[1]]                     # end is empty
        )

        

    
    def isWithinRange(self):
        distance = (((self.start[0] - self.end[0])**2) + ((self.start[1] - self.end[1])**2))
        if self.type == "diagonal":
            return distance == 8
        elif self.type in ["horizontal", "vertical"]:
            return distance == 4
        return False
    
    #returns the type of move (horizontal, vertical, diagonal)
    def classifyMove(self):
        if self.start[0] == self.end[0]:
            return "horizontal"
        elif self.start[1] == self.end[1]:
            return "vertical"
        else:
            return "diagonal"

    #assumes valid range
    def getMiddle(self):
        if self.type == "vertical":
            return (self.end[0] - 1, self.end[1])
        elif self.type == "horizontal":
            return (self.end[0], self.end[1] - 1)
        else:
            return(self.end[0] - 1, self.end[1] - 1)

    



