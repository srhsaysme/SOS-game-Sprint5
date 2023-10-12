from GameWindow import *
import pytest

class gameTesting:
    def testStartUp():
        testW = GameWindow()
        assert testW.currentGame.bluePlayer.score == 0
        assert testW.blueScoreLabel.cget("text") == "0"
        assert testW.currentGame.redPlayer.score == 0
        assert testW.redScoreLabel.cget("text") == "0"
        assert testW.currentGame.currentTurn
        assert testW.turnLabel.cget("text") == "Red's turn"
        assert testW.currentGame.gameRunning
        assert len(testW.currentGame.letterArray) == 8
        for y in range(0,8):
            assert len(testW.currentGame.letterArray[y]) == 8
        for x in range(0,8):
            for y in range(0,8):
                assert testW.currentGame.letterArray[y][x] == " "
        assert testW.currentGame.currentAnnounce == "New Simple Game!"
        assert testW.announceLabel.cget("text") == ""
        testW.window.destroy()
 
    def testPlaceLetter():
        testW = GameWindow()
        testW.currentX.set(4)
        testW.currentY.set(4)
        testW.blueOButton.invoke()
        testW.addCharButton.invoke()
        assert testW.currentGame.letterArray[3][3] == "S"
        #Closest object in gridCanvas to (70,70), coresponding to [3][3], is the text for S.
        assert testW.gridCanvas.itemcget(testW.gridCanvas.find_closest(70,70), "text") == "S"
        assert testW.currentGame.currentAnnounce == "Placed S at (4, 4)"
        assert testW.announceLabel.cget("text") == "Placed S at (4, 4)"
        testW.currentX.set(5)
        testW.addCharButton.invoke()
        assert testW.currentGame.letterArray[3][4] == "O"
        #Closest object in gridCanvas to (90,70), coresponding to [3][4], is the text for O.
        assert testW.gridCanvas.itemcget(testW.gridCanvas.find_closest(90,70), "text") == "O"
        #Item [0][0] of letterArray is unchanged.
        assert testW.currentGame.letterArray[0][0] == " "
        assert testW.currentGame.currentAnnounce == "Placed O at (5, 4)"
        assert testW.announceLabel.cget("text") == "Placed O at (5, 4)"
        assert testW.currentGame.gameRunning == True
        testW.window.destroy()

    def testOccupiedSpace():
        testW = GameWindow()
        testW.currentX.set(4)
        testW.currentY.set(4)
        testW.blueOButton.invoke()
        testW.addCharButton.invoke()
        testW.addCharButton.invoke()
        assert testW.currentGame.letterArray[3][3] == "S"
        assert testW.gridCanvas.itemcget(testW.gridCanvas.find_closest(70,70), "text") == "S"
        assert testW.currentGame.currentAnnounce == "Entered position is occupied"
        assert testW.announceLabel.cget("text") == "Entered position is occupied"
        assert testW.currentGame.currentTurn == False
        assert testW.turnLabel.cget("text") == "Blue's turn"
        testW.window.destroy()

    def testInvalidIntegers():
        testW = GameWindow()
        testW.currentX.set(-9)
        testW.currentY.set(4)
        testW.addCharButton.invoke()
        assert testW.announceLabel.cget("text") == "Invalid grid position"
        assert testW.currentGame.currentAnnounce == "Invalid grid position"
        for x in range(0,8):
            for y in range(0,8):
                assert testW.currentGame.letterArray[y][x] == " "
        assert testW.currentGame.currentTurn == True
        assert testW.turnLabel.cget("text") == "Red's turn"
        assert testW.currentGame.gameRunning == True
        testW.currentX.set(2)
        testW.currentY.set(20)
        testW.addCharButton.invoke()
        assert testW.announceLabel.cget("text") == "Invalid grid position"
        assert testW.currentGame.currentAnnounce == "Invalid grid position"
        for x in range(0,8):
            for y in range(0,8):
                assert testW.currentGame.letterArray[y][x] == " "
        assert testW.currentGame.currentTurn == True
        assert testW.turnLabel.cget("text") == "Red's turn"
        assert testW.currentGame.gameRunning == True
        testW.window.destroy()

    def testInvalidEntries():
        testW = GameWindow()
        testW.addCharButton.invoke()
        assert testW.announceLabel.cget("text") == "Invalid entry"
        assert testW.currentGame.currentAnnounce == "Invalid entry"
        for x in range(0,8):
            for y in range(0,8):
                assert testW.currentGame.letterArray[y][x] == " "
        assert testW.currentGame.currentTurn == True
        assert testW.turnLabel.cget("text") == "Red's turn"
        assert testW.currentGame.gameRunning == True
        testW.window.destroy()

    def testTurnSwitch():
        testW = GameWindow()
        testW.currentX.set(1)
        testW.currentY.set(1)
        assert testW.currentGame.currentTurn
        assert testW.turnLabel.cget("text") == "Red's turn"
        while (int(testW.currentY.get()) <= 8):
            testW.addCharButton.invoke()
            if (int(testW.currentY.get()) % 2 == 1):
                assert not testW.currentGame.currentTurn
                assert testW.turnLabel.cget("text") == "Blue's turn"
            else:
                assert testW.currentGame.currentTurn
                assert testW.turnLabel.cget("text") == "Red's turn"
            testW.currentY.set(int(testW.currentY.get()) + 1)
        testW.window.destroy()

    def testLetterSwitch():
        testW = GameWindow()
        testW.redOButton.invoke()
        testW.blueOButton.invoke()
        testW.currentX.set(1)
        testW.currentY.set(1)
        testW.addCharButton.invoke()
        assert testW.currentGame.letterArray[0][0] == "O"
        assert testW.gridCanvas.itemcget(testW.gridCanvas.find_closest(10,10), "text") == "O"
        testW.currentY.set(2)
        testW.addCharButton.invoke()
        assert testW.currentGame.letterArray[1][0] == "O"
        assert testW.gridCanvas.itemcget(testW.gridCanvas.find_closest(10,30), "text") == "O"
        testW.redSButton.invoke()
        testW.blueSButton.invoke()
        testW.currentY.set(3)
        testW.addCharButton.invoke()
        assert testW.currentGame.letterArray[2][0] == "S"
        assert testW.gridCanvas.itemcget(testW.gridCanvas.find_closest(10,50), "text") == "S"
        testW.currentY.set(4)
        testW.addCharButton.invoke()
        assert testW.currentGame.letterArray[3][0] == "S"
        assert testW.gridCanvas.itemcget(testW.gridCanvas.find_closest(10,70), "text") == "S"
        testW.window.destroy()

    def testBoardIsFull():
        testW = GameWindow()
        for x in range(1,9):
            for y in range(1,9):
                testW.currentX.set(x)
                testW.currentY.set(y)
                testW.addCharButton.invoke()
                if (x == 8 and y == 8):
                    assert not testW.currentGame.gameRunning
                else:
                    assert testW.currentGame.gameRunning
        testW.window.destroy()

    def testInsertWhenGameOver():
        testW = GameWindow()
        testW.currentGame.gameRunning = False
        testW.currentX.set(5)
        testW.currentY.set(4)
        testW.addCharButton.invoke()
        assert testW.currentGame.currentAnnounce == "Game is over."
        assert testW.announceLabel.cget("text") == "Game is over."
        assert not testW.currentGame.gameRunning
        assert testW.currentGame.letterArray[3][4] == " "
        assert testW.currentGame.currentTurn
        assert testW.turnLabel.cget("text") == "Red's turn"
        testW.window.destroy()

    def testNewSimpleGame():
        testW = GameWindow()
        for x in range(1,9):
            for y in range(1,9):
                testW.currentX.set(x)
                testW.currentY.set(y)
                testW.addCharButton.invoke()
        testW.nextGridSizeVar.set(6)
        testW.newGameButton.invoke()
        assert testW.currentGame.currentTurn
        assert testW.turnLabel.cget("text") == "Red's turn"
        assert testW.currentGame.currentAnnounce == "New Simple Game!"
        assert testW.announceLabel.cget("text") == "New Simple Game!"
        assert testW.currentGame.bluePlayer.score == 0
        assert testW.blueScoreLabel.cget("text") == "0"
        assert testW.currentGame.redPlayer.score == 0
        assert testW.redScoreLabel.cget("text") == "0"
        for x in range(0, 6):
            for y in range(0, 6):
                assert testW.currentGame.letterArray[y][x] == " "
        testW.window.destroy()

    def testNewComplexGame():
        testW = GameWindow()
        for x in range(1,9):
            for y in range(1,9):
                testW.currentX.set(x)
                testW.currentY.set(y)
                testW.addCharButton.invoke()
        testW.nextGridSizeVar.set(9)
        testW.complexButton.invoke()
        testW.newGameButton.invoke()
        assert testW.currentGame.currentTurn
        assert testW.turnLabel.cget("text") == "Red's turn"
        assert testW.currentGame.currentAnnounce == "New Complex Game!"
        assert testW.announceLabel.cget("text") == "New Complex Game!"
        assert testW.currentGame.bluePlayer.score == 0
        assert testW.blueScoreLabel.cget("text") == "0"
        assert testW.currentGame.redPlayer.score == 0
        assert testW.redScoreLabel.cget("text") == "0"
        for x in range(0, 9):
            for y in range(0, 9):
                assert testW.currentGame.letterArray[y][x] == " "
        testW.window.destroy()

    def testPatternFromS():
        testW = GameWindow()
        testW.complexButton.invoke()
        testW.newGameButton.invoke()
        testW.blueOButton.invoke()
        for x in [-1,0,1]:
            for y in [-1,0,1]:
                if (x != 0 or y != 0):
                    testW.currentX.set(4 + (2*x))
                    testW.currentY.set(4 + (2*y))
                    testW.addCharButton.invoke()
                    testW.currentX.set(4 + x)
                    testW.currentY.set(4 + y)
                    testW.addCharButton.invoke()
        testW.currentX.set(4)
        testW.currentY.set(4)
        testW.addCharButton.invoke()
        assert testW.currentGame.redPlayer.score == 11
        assert int(testW.redScoreLabel.cget("text")) == 11
        assert testW.currentGame.bluePlayer.score == 1
        assert int(testW.blueScoreLabel.cget("text")) == 1
        testW.window.destroy()

    def testPatternFromO():
        testW = GameWindow()
        testW.complexButton.invoke()
        testW.newGameButton.invoke()
        for x in [-1,0,1]:
            for y in [-1,0,1]:
                if (x != 0 or y != 0):
                    testW.currentX.set(4 + x)
                    testW.currentY.set(4 + y)
                    testW.addCharButton.invoke()
        testW.redOButton.invoke()
        testW.currentX.set(4)
        testW.currentY.set(4)
        testW.addCharButton.invoke()
        assert testW.currentGame.redPlayer.score == 4
        assert int(testW.redScoreLabel.cget("text")) == 4
        testW.window.destroy()

    def testSinglePatterns():
        testW = GameWindow()
        testW.complexButton.invoke()
        testW.newGameButton.invoke()
        testW.blueOButton.invoke()
        for x in [1,2,3]:
            testW.currentX.set(x)
            testW.currentY.set(1)
            testW.addCharButton.invoke()
        assert testW.currentGame.redPlayer.score == 1
        assert int(testW.redScoreLabel.cget("text")) == 1
        testW.currentX.set(2)
        testW.currentY.set(2)
        testW.addCharButton.invoke()
        testW.currentX.set(1)
        testW.currentY.set(3)
        testW.addCharButton.invoke()
        assert testW.currentGame.redPlayer.score == 2
        assert int(testW.redScoreLabel.cget("text")) == 2
        assert testW.currentGame.bluePlayer.score == 0
        assert int(testW.blueScoreLabel.cget("text")) == 0
        testW.redOButton.invoke()
        testW.blueSButton.invoke()
        for x in [1,2,3]:
            testW.currentX.set(x)
            testW.currentY.set(5)
            testW.addCharButton.invoke()
        assert testW.currentGame.redPlayer.score == 2
        assert int(testW.redScoreLabel.cget("text")) == 2
        assert testW.currentGame.bluePlayer.score == 1
        assert int(testW.blueScoreLabel.cget("text")) == 1
        testW.window.destroy()

    def testSimpleGameWin():
        testW = GameWindow()
        testW.blueOButton.invoke()
        for x in [1,2,3]:
            testW.currentX.set(x)
            testW.currentY.set(1)
            testW.addCharButton.invoke()
        assert testW.currentGame.redPlayer.score == 1
        assert int(testW.redScoreLabel.cget("text")) == 1
        assert testW.announceLabel.cget("text") == "Red wins!"
        assert testW.currentGame.gameRunning == False
        testW.currentY.set(3)
        testW.addCharButton.invoke()
        assert testW.currentGame.letterArray[2][2] == " "
        assert testW.announceLabel.cget("text") == "Game is over."
        testW.window.destroy()

    def testSimpleGameDraw():
        testW = GameWindow()
        testW.nextGridSizeVar.set(6)
        testW.newGameButton.invoke()
        for x in range(1,7):
            for y in range(1,7):
                testW.currentX.set(x)
                testW.currentY.set(y)
                testW.addCharButton.invoke()
        assert testW.currentGame.redPlayer.score == 0
        assert int(testW.redScoreLabel.cget("text")) == 0
        assert testW.currentGame.bluePlayer.score == 0
        assert int(testW.blueScoreLabel.cget("text")) == 0
        assert testW.announceLabel.cget("text") == "Game is a draw."
        assert testW.currentGame.gameRunning == False
        testW.window.destroy()

    def testComplexGameWin():
        testW = GameWindow()
        testW.complexButton.invoke()
        testW.newGameButton.invoke()
        testW.blueOButton.invoke()
        for x in range(1,8,2):
            for y in range(1,9):
                testW.currentX.set(x)
                testW.currentY.set(y)
                testW.addCharButton.invoke()
                testW.currentX.set(x+1)
                testW.addCharButton.invoke()
        assert testW.currentGame.redPlayer.score == 60
        assert int(testW.redScoreLabel.cget("text")) == 60
        assert testW.currentGame.bluePlayer.score == 0
        assert int(testW.blueScoreLabel.cget("text")) == 0
        assert testW.announceLabel.cget("text") == "Red wins!"
        assert testW.currentGame.gameRunning == False
        testW.window.destroy()

    def testComplexGameDraw():
        testW = GameWindow()
        testW.complexButton.invoke()
        testW.newGameButton.invoke()
        for x in range(1,8,2):
            for y in range(1,9):
                testW.currentX.set(x)
                testW.currentY.set(y)
                testW.addCharButton.invoke()
                assert testW.currentGame.gameRunning == True
                testW.currentX.set(x+1)
                testW.addCharButton.invoke()
        assert testW.currentGame.redPlayer.score == 0
        assert int(testW.redScoreLabel.cget("text")) == 0
        assert testW.currentGame.bluePlayer.score == 0
        assert int(testW.blueScoreLabel.cget("text")) == 0
        assert testW.announceLabel.cget("text") == "Game is a draw."
        assert testW.currentGame.gameRunning == False
        testW.window.destroy()

    def testNewComputerPlayer():
        testW = GameWindow()
        assert not testW.currentGame.redPlayer.isComputer
        assert not testW.currentGame.bluePlayer.isComputer
        testW.blueComputerBox.invoke()
        testW.nextGridSizeVar.set(6)
        testW.newGameButton.invoke()
        assert not testW.currentGame.redPlayer.isComputer
        assert testW.currentGame.bluePlayer.isComputer
        testW.redComputerBox.invoke()
        testW.newGameButton.invoke()
        assert testW.currentGame.redPlayer.isComputer
        assert testW.currentGame.bluePlayer.isComputer
        testW.window.destroy()

    def testComputerPlayerPlacing():
        testW = GameWindow()
        testW.blueComputerBox.invoke()
        testW.nextGridSizeVar.set(5)
        testW.newGameButton.invoke()
        emptySlots = 0
        for x in range(0,5):
            for y in range(0,5):
                if (testW.currentGame.letterArray[y][x] == " "):
                    emptySlots += 1
        assert emptySlots == 25
        testW.currentX.set(2)
        testW.currentY.set(2)
        testW.addCharButton.invoke()
        emptySlots = 0
        for x in range(0,5):
            for y in range(0,5):
                if (testW.currentGame.letterArray[y][x] == " "):
                    emptySlots += 1
        assert emptySlots == 23
        testW.redComputerBox.invoke()
        testW.blueComputerBox.invoke()
        testW.newGameButton.invoke()
        emptySlots = 0
        for x in range(0,5):
            for y in range(0,5):
                if (testW.currentGame.letterArray[y][x] == " "):
                    emptySlots += 1
        assert emptySlots == 24
        if testW.currentGame.letterArray[1][1] == " ":
            testW.addCharButton.invoke()
        else:
            testW.currentX.set(5)
            testW.currentY.set(5)
            testW.addCharButton.invoke()
        emptySlots = 0
        for x in range(0,5):
            for y in range(0,5):
                if (testW.currentGame.letterArray[y][x] == " "):
                    emptySlots += 1
        assert emptySlots == 22

    def testNewHumanPlayer():
        testW = GameWindow()
        testW.redComputerBox.invoke()
        testW.blueComputerBox.invoke()
        testW.newGameButton.invoke()
        assert testW.currentGame.redPlayer.isComputer
        assert testW.currentGame.bluePlayer.isComputer
        testW.redComputerBox.invoke()
        testW.newGameButton.invoke()
        assert not testW.currentGame.redPlayer.isComputer
        assert testW.currentGame.bluePlayer.isComputer
        testW.redComputerBox.invoke()
        testW.blueComputerBox.invoke()
        testW.newGameButton.invoke()
        assert testW.currentGame.redPlayer.isComputer
        assert not testW.currentGame.bluePlayer.isComputer

    def testComputerOnlyGame():
        testW = GameWindow()
        testW.redComputerBox.invoke()
        testW.blueComputerBox.invoke()
        #testW.complexButton.invoke()
        testW.newGameButton.invoke()
        assert not testW.currentGame.gameRunning
        if (testW.currentGame.redPlayer.score > testW.currentGame.bluePlayer.score):
            assert testW.currentGame.currentAnnounce == "Red wins!"
            assert testW.announceLabel.cget("text") == "Red wins!"
        elif (testW.currentGame.bluePlayer.score > testW.currentGame.redPlayer.score):
            assert testW.currentGame.currentAnnounce == "Blue wins!"
            assert testW.announceLabel.cget("text") == "Blue wins!"
        else:
            assert testW.currentGame.currentAnnounce == "Game is a draw."
            assert testW.announceLabel.cget("text") == "Game is a draw."