# /* Gomoku
#name of program: Gomoku.py
#Official name: Louanges Takou-Ayaoh
#nickname: Marlene
#SU login id: letakoua */

# importing from the graphics and random library
from graphics import *
from random import randrange

# creates a class to display and update who is which color
##    (CLOD)    ##
class PlayerBoard:
    def __init__(self, name):
        self.name = name
        self.indicator= Text(Point(9.6, 5.6), name + " your color is")

    def Playersdisplay(self,win):
        display = Text(Point(9.6, 6.5),self.name+"   vs.   Comp").draw(win)
        display.setSize(18)
        display.setTextColor('DarkOliveGreen')
        display.setStyle('bold')

    def colorIndicator(self,color,win):
        self.indicator= Text(Point(9.6, 5.6), name + " your color is "+color).draw(win)
        self.indicator.setFill(color)


    # updates the score on the window as well as in the file
    def scoreUpdate(self,name,winner,playerScore,compScore,win):
        # opens the file of previous players to update the score
        infile = open("GomokuPlayers.txt", "r+")
        outfile = open("GomokuOutfile.txt", "w")

        # reads input file and pastes the name and score depending on who won
        for lines in infile:
            line = lines.split()
            if line[0] == name:
                if line[0] == winner[0]:
                    ##    (OFL)    ##
                    print("{0:<9} {1:<6} {2:<6}".format(name,(playerScore+1),compScore),file=outfile)
                else:
                    print("{0:<9} {1:<6} {2:<6}".format(name, playerScore, compScore + 1), file=outfile)
            else:
                print("{0:<9} {1:<6} {2:<6}".format(line[0], line[1] ,line[2]), file=outfile)

        outfile.close()
        infile.close()

        # rewriting the input with the new score of the outfile
        newinfile = open("GomokuPlayers.txt", "w")
        newoutfile = open("GomokuOutfile.txt", "r")
        newinfile.write(newoutfile.read())
        newinfile.close()
        newoutfile.close()

        # opens output file to display on graphics window
        outputfile = open("GomokuOutfile.txt", "r")

        Text(Point(9.4, 5.2), "Name 	Wins	Losses").draw(win)
        #
        line = []

        for lines in outputfile:
            info= lines.split()
            line.append(info)
        outputfile.close()
        print(line)
        for i in range(len(line)):
            for k in range(1):
                Text(Point(9.25, 5 - i/3), line[i][0]+"              "+line[i][1]+"                   "+line[i][2]).draw(win)

        Text(Point(9.5, 2.5), "Thank you for playing Gomoku!").draw(win)


#*********End of PlayerBoard class****************

#*************** setUpWindow **************
#Set up the GraphWin.
##   (GW)   ##
#returns the GraphWin
def setUpWindow():
    win=GraphWin("GOMOKU", 900,600)
    win.setBackground("burlywood3")
    win.setCoords(1, 1, 12, 8)
    ##  (OTXT)  ##
    gameName = Text(Point(9.5, 7.5), "GOMOKU").draw(win)
    gameName.setFill("brown")
    gameName.setSize(20)
    return win

#*************makeBoard********************

def makeBoard(win):

    #draws vertical lines
    for i in range(10, 65, 5):
        x = (float(i) / 10) + 0.5
        aLine = Line(Point(x, 7), Point(x, 2))
        aLine.setWidth(1)
        aLine.draw(win)

    # draws horizontal lines
    for i in range(10, 65, 5):
        y = ((float(i) / 10) + 1)
        aLine2 = Line(Point(1.5, y), Point(6.5, y))
        aLine2.setWidth(1)
        aLine2.draw(win)

    #draws the vertical outline
    for k in [1.3, 6.7]:
        aLine3 = Line(Point(k, 7.2), Point(k, 1.8))
        aLine3.setWidth(1.5)
        aLine3.draw(win)

    #draws the horizontal outline
    for l in [1.8, 7.2]:
        aLine4 = Line(Point(1.3, l), Point(6.7, l))
        aLine4.setWidth(1.5)
        aLine4.draw(win)

#*************End of makeBoard********************

# Collects data from the player needed to play as well
# Removes the input data page
def inputData(win):
    # making an entry box go receive the name
    entryName = Entry(Point(9.5, 6.5), 9).draw(win)
    enterNameLabel = Text(Point(8, 6.5), "Enter Name:").draw(win)
    buttonEN = Rectangle(Point(7, 6.3), Point(8.9, 6.7)).draw(win)
    submit1 = Text(Point(10.8, 6.5), "Submit").draw(win)
    buttonS1 = Rectangle(Point(10.2, 6.3), Point(11.4, 6.7)).draw(win)

    # gets mouse to "enter" the data for name
    # then check if name was given
    win.getMouse()
    name= entryName.getText()

    noName= Text(Point(9.4, 5.8), "Submit a name ")
    while name== '':
        noName.draw(win)
        noName.setFill('red')
        noName.setSize(15)
        win.getMouse()
        name=entryName.getText()

    noName.undraw()
    # gets the name given in the entry box for the name
    ##  (IEB)  ##
    name = entryName.getText()

    checkName = False

    playerScores=[]

    # opens the list of previous players to see if the player is a returning player
    ##    (IFL)   ##
    infile = open("GomokuPlayers.txt","r")
    for lines in infile:
        line = lines.split()
        if line[0] == name.strip():
            checkName = True
            playerScores.append(int(line[1]))
            playerScores.append(int(line[2]))


            # appends a new score for new players of 0
    if checkName==False:
        playerScores.append(0)
        playerScores.append(0)
        ##appends the new player to the file
        ##    (OFL)    ##
        outfile = open("GomokuPlayers.txt", "a+")
        outfile.write("\n"+name+"     0       0")
        outfile.close()
    #closing the file
    infile.close()

    # makes an entry box to receive the difficulty of the game
    entryDif = Entry(Point(9.5, 5.4), 6).draw(win)
    entryDif.setText("E or M")
    enterDifLabel = Text(Point(8, 5.5), "Difficulty:\n Add E for easy mode \nand M for medium mode").draw(win)
    submit2 = Text(Point(10.8, 5.5), "Submit").draw(win)
    buttonS2 = Rectangle(Point(10.2, 5.3), Point(11.4, 5.7)).draw(win)

    # gets mouse to "enter" the data for difficulty
    win.getMouse()
    difficulty = []

    # gets the difficulty given in the entry box
    gameDifficulty = entryDif.getText()
    wrongData = Text(Point(9.4, 4.8), "Wrong data!\n Try again ")
    # checks whether difficulty is either E or M
    while gameDifficulty != 'E' and gameDifficulty != 'M':
        wrongData.draw(win)
        wrongData.setFill('red')
        win.getMouse()
        gameDifficulty = entryDif.getText()

    wrongData.undraw()

    # appends the difficulty chosen by the player in an empty list
    difficulty.append(gameDifficulty)

    # gets mouse before removing entry boxes
    click2remove = Text(Point(9.4, 4.5), "Click anywhere to start playing").draw(win)
    click2remove.setFace("helvetica")
    click2remove.setSize(19)

    # waits for click to start un-drawing
    win.getMouse()
    click2remove.undraw()

    # removes all the entry boxes and label currently on the window
    entryName.undraw()
    enterNameLabel.undraw()
    buttonEN.undraw()
    submit1.undraw()
    buttonS1.undraw()
    entryDif.undraw()
    entryDif.undraw()
    enterDifLabel.undraw()
    submit2.undraw()
    buttonS2.undraw()

    # returns name, playerScores and difficulty
    return name, difficulty, playerScores

# list of moves for computer
def movesForComp():
    movesList = []

    for a in range(20,65,5):
        x = (float(a) / 10)
        p1 = movesList.append("("+str(x)+","+str(2.5)+")")
        p2 = movesList.append("("+str(x)+","+str(3.0)+")")
        p3 = movesList.append("("+str(x)+","+str(3.5)+")")
        p4 = movesList.append("("+str(x)+","+str(4.0)+")")
        p5 = movesList.append("("+str(x)+","+str(4.5)+")")
        p6 = movesList.append("("+str(x)+","+str(5.0)+")")
        p7 = movesList.append("("+str(x)+","+str(5.5)+")")
        p8 = movesList.append("("+str(x)+","+str(6.0)+")")
        p9 = movesList.append("("+str(x)+","+str(6.5)+")")

    return movesList # list of all the possible points to occupy on the board

# checks whether the player placed the stone within the limits of the board
def validMoves(x,y,recordedMoves_Player1,recordedMoves_Player2):
    # values on the Board should be True if it is inbetween
    onBoard = (2 <= x <= 6.0 and 2.5 <= y <= 6.5)

    pt = "(" + str(x) + "," + str(y) + ")"  # makes the string (x,y)

    # occupied should be true if the point is already occupied
    occupied = (pt in recordedMoves_Player1) or (pt in recordedMoves_Player2)

    # valid should be true only for valid moves
    # Want the move on the board, but not already occupied
    valid = onBoard and not occupied

    return valid  # true only for valid move

# reads the point played of human
def readHumanPoints(point):
    # gets the (x,y) the player clicked on the board
    xPt = point.getX()
    yPt = point.getY()
    # setting (x,y) as 0
    x = 0
    y = 0

    # makes the points clicked by th player to land exactly on the intersection
    # for point x
    for i in range(20, 65, 5):
        pt = i / 10
        if (pt - 0.25) < xPt < (pt + 0.25):
            x += pt

    # for point y
    for k in range(25, 70, 5):
        pt = k / 10
        if (pt - 0.25) < yPt < (pt + 0.25):
            y += pt

    return x, y

# reads computers play
def readComputerPoints(movesList):
    # random range of 82
    r = randrange(81)
    # it picks a random point in the list given in moveList
    findPoint = movesList[r]
    # then it strips it to then change the points in floats to use
    stripPoint = findPoint.strip()
    x = float(stripPoint[1:4])
    y = float(stripPoint[5:8])

    return x, y # returns point that will be used by computer

# recreates the points on the board of each row in a list
def therows():
    row1 = ['(2.0,2.5)','(2.5,2.5)','(3.0,2.5)','(3.5,2.5)','(4.0,2.5)','(4.5,2.5)','(5.0,2.5)','(5.5,2.5)','(6.0,2.5)']
    row2 = ['(2.0,3.0)','(2.5,3.0)','(3.0,3.0)','(3.5,3.0)','(4.0,3.0)','(4.5,3.0)','(5.0,3.0)','(5.5,3.0)','(6.0,3.0)']
    row3 = ['(2.0,3.5)','(2.5,3.5)','(3.0,3.5)','(3.5,3.5)','(4.0,3.5)','(4.5,3.5)','(5.0,3.5)','(5.5,3.5)','(6.0,3.5)']
    row4 = ['(2.0,4.0)','(2.5,4.0)','(3.0,4.0)','(3.5,4.0)','(4.0,4.0)','(4.5,4.0)','(5.0,4.0)','(5.5,4.0)','(6.0,4.0)']
    row5 = ['(2.0,4.5)','(2.5,4.5)','(3.0,4.5)','(3.5,4.5)','(4.0,4.5)','(4.5,4.5)','(5.0,4.5)','(5.5,4.5)','(6.0,4.5)']
    row6 = ['(2.0,5.0)','(2.5,5.0)','(3.0,5.0)','(3.5,5.0)','(4.0,5.0)','(4.5,5.0)','(5.0,5.0)','(5.5,5.0)','(6.0,5.0)']
    row7 = ['(2.0,5.5)','(2.5,5.5)','(3.0,5.5)','(3.5,5.5)','(4.0,5.5)','(4.5,5.5)','(5.0,5.5)','(5.5,5.5)','(6.0,5.5)']
    row8 = ['(2.0,6.0)','(2.5,6.0)','(3.0,6.0)','(3.5,6.0)','(4.0,6.0)','(4.5,6.0)','(5.0,6.0)','(5.5,6.0)','(6.0,6.0)']
    row9 = ['(2.0,6.5)','(2.5,6.5)','(3.0,6.5)','(3.5,6.5)','(4.0,6.5)','(4.5,6.5)','(5.0,6.5)','(5.5,6.5)','(6.0,6.5)']

    return row1,row2,row3,row4,row5,row6,row7,row8,row9

# replaces the point of the stone with the first letter of the stones color
# in order to use it to check for wins
def putpointsRow(pt,color,row1,row2,row3,row4,row5,row6,row7,row8,row9):
    for i in range(9):
        if pt == row1[i]:
            row1[i] = color
        elif pt == row2[i]:
            row2[i] = color
        elif pt == row3[i]:
            row3[i] = color
        elif pt == row4[i]:
            row4[i] = color
        elif pt == row5[i]:
            row5[i] = color
        elif pt == row6[i]:
            row6[i] = color
        elif pt == row7[i]:
            row7[i] = color
        elif pt == row8[i]:
            row8[i] = color
        elif pt == row9[i]:
            row9[i] = color

# checks for horizontal wins
def check_horizontal(player,c,row1,row2,row3,row4,row5,row6,row7,row8,row9):
     board=[row1,row2,row3,row4,row5,row6,row7,row8,row9]

     for i in range(9):
         for k in range(5):
             if board[i][k]==c and board[i][k+1]==c and board[i][k+2]==c and board[i][k+3]==c and board[i][k+4]==c:
                     winFound= Text(Point(4, 7.5), player + " WON.").draw(win)
                     winFound.setFill('brown')
                     winFound.setSize(18)
                     winner.append(player)
                     break

# checks for vertical win
def check_vertical(player,c,row1,row2,row3,row4,row5,row6,row7,row8,row9):
    board = [row1, row2, row3, row4, row5, row6, row7, row8, row9]

    for i in range(5):
        for k in range(9):
            if board[i][k]==c and board[i+1][k]==c and board[i+2][k]==c and board[i+3][k]==c and board[i+4][k]==c:
                winFound = Text(Point(4, 7.5), player + " WON.").draw(win)
                winFound.setFill('brown')
                winFound.setSize(18)
                winner.append(player)
                break

# checks for climbing diagonal win
def checkL_diagonal(player,c,row1,row2,row3,row4,row5,row6,row7,row8,row9):
    board = [row1, row2, row3, row4, row5, row6, row7, row8, row9]

    for i in range(5):
        for k in range(5):
            if board[i][k]==c and board[i+1][k+1]==c and board[i+2][k+2]==c and board[i+3][k+3]==c and board[i+4][k+4]==c:
                winFound = Text(Point(4, 7.5), player + " WON.").draw(win)
                winFound.setFill('brown')
                winFound.setSize(18)
                winner.append(player)
                break

# checks for downwards diagonal win
def checkR_diagonal(player,c,row1,row2,row3,row4,row5,row6,row7,row8,row9):
    board = [row1, row2, row3, row4, row5, row6, row7, row8, row9]

    for i in range(8,-1,-1):
        for k in range(4,-1,-1):
            if board[i][k]==c and board[i-1][k+1]==c and board[i-2][k+2]==c and board[i-3][k+3]==c and board[i-4][k+4]==c:
                winFound = Text(Point(4, 7.5), player + " WON.").draw(win)
                winFound.setFill('brown')
                winFound.setSize(18)
                winner.append(player)
                break

# Calls this function if player chooses easy mode
def easyMode(player1color,player1,player2,recordedMoves_Player1,recordedMoves_Player2,compMoves, win):

    if player1color == "white":
        # indicates which color the player is
        cip.colorIndicator('white',win)
        # waits for click and checks if it is valid
        placement = win.getMouse()
        x, y = readHumanPoints(placement)
        while not validMoves(x,y,recordedMoves_Player1,recordedMoves_Player2):
            placement = win.getMouse()
            x, y = readHumanPoints(placement)

        ptW = "(" + str(x) + "," + str(y) + ")"
        recordedMoves_Player1.append(ptW)

        #checks for win
        putpointsRow(ptW,'W',row1,row2,row3,row4,row5,row6,row7,row8,row9)
        check_horizontal(player1,'W', row1, row2, row3, row4, row5, row6, row7, row8, row9)
        check_vertical(player1,'W', row1, row2, row3, row4, row5, row6, row7, row8, row9)
        checkL_diagonal(player1,'W', row1, row2, row3, row4, row5, row6, row7, row8, row9)
        checkR_diagonal(player1,'W', row1, row2, row3, row4, row5, row6, row7, row8, row9)

        # constructs a white circle centered at point with x,y coords, radius .25
        whiteStone = Circle(Point(x, y), .25).draw(win)
        whiteStone.setFill("white")

        # blacks turns (computer)
        x2, y2 = readComputerPoints(compMoves)
        while not validMoves(x2, y2, recordedMoves_Player1, recordedMoves_Player2):
            x2, y2 = readComputerPoints(compMoves)

        ptB = "(" + str(x2) + "," + str(y2) + ")"
        recordedMoves_Player2.append(ptB)

        # checks for win
        putpointsRow(ptB, 'B', row1, row2, row3, row4, row5, row6, row7, row8, row9)
        check_horizontal(player2,'B', row1, row2, row3, row4, row5, row6, row7, row8, row9)
        check_vertical(player2, 'B', row1, row2, row3, row4, row5, row6, row7, row8, row9)
        checkL_diagonal(player2, 'B', row1, row2, row3, row4, row5, row6, row7, row8, row9)
        checkR_diagonal(player2, 'B', row1, row2, row3, row4, row5, row6, row7, row8, row9)

        # constructs a black circle centered at point with x,y coords, radius .25
        blackStone = Circle(Point(x2, y2), .25).draw(win)
        blackStone.setFill("black")

    else:
        # computer is white and goes first
        x3,y3 = readComputerPoints(compMoves)
        while not validMoves(x3, y3, recordedMoves_Player1, recordedMoves_Player2):
            x3,y3 = readComputerPoints(compMoves)

        ptW= "(" + str(x3) + "," + str(y3) + ")"
        recordedMoves_Player2.append(ptW)
        # constructs a white circle centered at point with x,y coords, radius .25
        whiteStone = Circle(Point(x3, y3), .25).draw(win)
        whiteStone.setFill("white")

        # checks for win
        putpointsRow(ptW, 'W', row1, row2, row3, row4, row5, row6, row7, row8, row9)
        check_horizontal(player2,'W', row1, row2, row3, row4, row5, row6, row7, row8, row9)
        check_vertical(player2, 'W', row1, row2, row3, row4, row5, row6, row7, row8, row9)
        checkL_diagonal(player2, 'W', row1, row2, row3, row4, row5, row6, row7, row8, row9)
        checkR_diagonal(player2, 'W', row1, row2, row3, row4, row5, row6, row7, row8, row9)

        # blacks turn
        cip.colorIndicator('black',win) # indicates player's color

        placement = win.getMouse()
        x4, y4 = readHumanPoints(placement)
        while not validMoves(x4, y4, recordedMoves_Player1, recordedMoves_Player2):
            placement = win.getMouse()
            x4, y4 = readHumanPoints(placement)

        ptB= "(" + str(x4) + "," + str(y4) + ")"
        recordedMoves_Player1.append(ptB)
        # constructs a black circle centered at point with x,y coords, radius .25
        blackStone = Circle(Point(x4, y4), .25).draw(win)
        blackStone.setFill("black")

        #checks for win
        putpointsRow(ptB, 'B', row1, row2, row3, row4, row5, row6, row7, row8, row9)
        check_horizontal(player1,'B', row1, row2, row3, row4, row5, row6, row7, row8, row9)
        check_vertical(player1, 'B', row1, row2, row3, row4, row5, row6, row7, row8, row9)
        checkL_diagonal(player1, 'B', row1, row2, row3, row4, row5, row6, row7, row8, row9)
        checkR_diagonal(player1,'B', row1, row2, row3, row4, row5, row6, row7, row8, row9)
# Medium mode
def mediumMode(player1color,player1,player2,recordedMoves_Player1,recordedMoves_Player2,win):

    if player1color == "white":
        # indicates which color the player is
        cip.colorIndicator('white',win)
        # waits for click and then checks if valid
        placement = win.getMouse()
        x, y = readHumanPoints(placement)
        while not validMoves(x,y,recordedMoves_Player1,recordedMoves_Player2):
            placement = win.getMouse()
            x, y = readHumanPoints(placement)

        ptW = "(" + str(x) + "," + str(y) + ")"
        recordedMoves_Player1.append(ptW)
        # checks for win
        putpointsRow(ptW, 'W', row1, row2, row3, row4, row5, row6, row7, row8, row9)
        check_horizontal(player1, 'W', row1, row2, row3, row4, row5, row6, row7, row8, row9)
        check_vertical(player1, 'W', row1, row2, row3, row4, row5, row6, row7, row8, row9)
        checkL_diagonal(player1, 'W', row1, row2, row3, row4, row5, row6, row7, row8, row9)
        checkR_diagonal(player1, 'W', row1, row2, row3, row4, row5, row6, row7, row8, row9)

        # constructs a white circle centered at point with x,y coords, radius .25
        whiteStone = Circle(Point(x, y), .25).draw(win)
        whiteStone.setFill("white")

        # blacks turns (computer)
        ##    (RND)    ##
        place = [0,0.5,-0.5]
        r = randrange(3)

        # comp chooses points based on the choice of the human
        x2 = x + place[r]
        y2 = y + place[r]

        while not validMoves(x2, y2, recordedMoves_Player1, recordedMoves_Player2):
            place = [0, 0.5, -0.5,1,-1]
            r = randrange(5)
            x2 = x + place[r]
            y2 = y + place[r]

        ptB = "(" + str(x2) + "," + str(y2) + ")"
        recordedMoves_Player2.append(ptB)

        # checks for win
        putpointsRow(ptB, 'B', row1, row2, row3, row4, row5, row6, row7, row8, row9)
        check_horizontal(player2, 'B', row1, row2, row3, row4, row5, row6, row7, row8, row9)
        check_vertical(player2, 'B', row1, row2, row3, row4, row5, row6, row7, row8, row9)
        checkL_diagonal(player2, 'B', row1, row2, row3, row4, row5, row6, row7, row8, row9)
        checkR_diagonal(player2, 'B', row1, row2, row3, row4, row5, row6, row7, row8, row9)
        # constructs a black circle centered at point with x,y coords, radius .25
        blackStone = Circle(Point(x2, y2), .25).draw(win)
        blackStone.setFill("black")

    else:
        cip.colorIndicator('black',win)
        # waits for click and then checks if valid
        placement = win.getMouse()
        x, y = readHumanPoints(placement)
        while not validMoves(x, y, recordedMoves_Player1, recordedMoves_Player2):
            placement = win.getMouse()
            x, y = readHumanPoints(placement)

        ptB = "(" + str(x) + "," + str(y) + ")"
        recordedMoves_Player1.append(ptB)

        # checks for win
        putpointsRow(ptB,'B', row1, row2, row3, row4, row5, row6, row7, row8, row9)
        check_horizontal(player1, 'B', row1, row2, row3, row4, row5, row6, row7, row8, row9)
        check_vertical(player1, 'B', row1, row2, row3, row4, row5, row6, row7, row8, row9)
        checkL_diagonal(player1, 'B', row1, row2, row3, row4, row5, row6, row7, row8, row9)
        checkR_diagonal(player1, 'B', row1, row2, row3, row4, row5, row6, row7, row8, row9)
        # constructs a white circle centered at point with x,y coords, radius .25
        whiteStone = Circle(Point(x, y), .25).draw(win)
        whiteStone.setFill("black")

        # blacks turns (computer)
        place = [0, 0.5, -0.5]
        r = randrange(3)

        # comp chooses points based on the choice of the human
        x2 = x + place[r]
        y2 = y + place[r]

        while not validMoves(x2, y2, recordedMoves_Player1, recordedMoves_Player2):
            place = [0, 0.5, -0.5,1,-1]
            r = randrange(5)
            x2 = x + place[r]
            y2 = y + place[r]

        #append point
        ptW = "(" + str(x2) + "," + str(y2) + ")"
        recordedMoves_Player2.append(ptW)

        # checks for win
        putpointsRow(ptW, 'W', row1, row2, row3, row4, row5, row6, row7, row8, row9)
        check_horizontal(player2, 'W', row1, row2, row3, row4, row5, row6, row7, row8, row9)
        check_vertical(player2, 'W', row1, row2, row3, row4, row5, row6, row7, row8, row9)
        checkL_diagonal(player2, 'W', row1, row2, row3, row4, row5, row6, row7, row8, row9)
        checkR_diagonal(player2, 'W', row1, row2, row3, row4, row5, row6, row7, row8, row9)
        # constructs a black circle centered at point with x,y coords, radius .25
        blackStone = Circle(Point(x2, y2), .25).draw(win)
        blackStone.setFill("white")


# generates a number from 0 to 1 to see which player goes first by being the white stone
# it is assigned to player 1 because if player one is white they go first else they go second
def colorChooser():
    colors = ["white","black"]
    r = randrange(2)
    player1color = colors[r]

    return player1color

# this displays the option to see score
##   (OTXT)   ##
def viewingOption(win):
    option = Text(Point(9.6, 3.5), "Click Yes or No to see your score against the computer").draw(win)
    yes = Text(Point(8.5, 2.7), "Yes").draw(win)
    yesBox = Rectangle(Point(8.1, 2.5), Point(8.9, 2.9)).draw(win)
    no = Text(Point(10.5, 2.7), "No").draw(win)
    noBox = Rectangle(Point(10.1, 2.5), Point(10.9, 2.9)).draw(win)

    return option,yes,yesBox,no,noBox # return in order to undraw

# undraws the text and boxes asking player to choose an option
def undrawViewOption(option,yes,yesBox,no,noBox):
    option.undraw()
    yes.undraw()
    yesBox.undraw()
    no.undraw()
    noBox.undraw()

# this function checks which box is picked and either shows score or not
##   (IMS)   ##
def choice(click):
    if (8.1 <= click.getX() <= 8.9) and (2.5 <= click.getY() <= 2.9):
        cip.scoreUpdate(player1,winner,playerScore,compScore,win)
    elif (10.1 <= click.getX() <= 10.9) and (2.5 <= click.getY() <= 2.9):
        Text(Point(9.5, 3.2), "Thank you for playing Gomoku!").draw(win)

# ******************** main ************************
if __name__ == '__main__':
    ##   (GW)    ##
    ##   (FNC)   ##
    win = setUpWindow()
    board = makeBoard(win)

    # # input data collected
    name, difficultyPlay, playerScores = inputData(win)
    # # gets the scores of player and computer
    difficulty = difficultyPlay[0]
    playerScore= playerScores[0]
    compScore= playerScores[1]

    # # calls score board class
    ##   (CLOD)   ##
    scoreBoard = PlayerBoard(name)
    scoreBoard.Playersdisplay(win)

    # player order
    player1 = name
    player2 = "Comp."

    # using class to indicate which colore the player is
    ##   (CLOD)   ##
    cip = PlayerBoard(player1)

    # calls the functions with the possible moves for the computer to read
    compMoves = movesForComp()

    # records the moves of
    ##    (LOOD)   ##
    recordedMoves_Player1 = []
    recordedMoves_Player2 = []

    row1,row2,row3,row4,row5,row6,row7,row8,row9 = therows()

    # randomly selecting which player goes first
    # white goes first
    player1color = colorChooser()
    winner = [] # waiting to append winner

    # depending on the mode chosen by the player the game starts
    if difficulty == 'E':
        while (len(recordedMoves_Player1)<46):
            easyMode(player1color, player1, player2, recordedMoves_Player1,recordedMoves_Player2, compMoves, win)
            if winner !=[]:
                break

    else:
        while (len(recordedMoves_Player1)<46):
            mediumMode(player1color,player1, player2, recordedMoves_Player1,recordedMoves_Player2,win)
            if winner !=[]:
                break

    if winner==[]: # if there is a draw
        playerIndicator = Text(Point(9.6, 3.5),"DRAW NO WINNER").draw(win)
    else:
        option, yes, yesBox, no, noBox = viewingOption(win)
        click = win.getMouse()
        undrawViewOption(option, yes, yesBox, no, noBox)
        choice(click)
        Text(Point(9.5, 2.9), "Click anywhere to exit").draw(win)

    # gets mouse and closes
    win.getMouse()
    win.close()

##************* end of main ***************