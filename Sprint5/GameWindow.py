from GameLogic import *

#Inherits from GameLogic.
class GameWindow:
    """
    Class that creates window and displays the state of the game in the GUI.
    Inherits all of the variables and methods from GameLogic. Creates the window and frames that
    will contain UI widgets, then creates labels, buttons, and entry boxes and places them in 
    the frames. The playing grid canvas takes up the middle space, options for each player rest 
    on the sides of the grid, and the bottom holds the buttons for controlling the game and 
    entry boxes for inputting x and y values.
    Important Attributes:
        currentGame: an instance of either SimpleGame or ComplexGame that keeps track of the rules
        and state of the current game.
        xEntry and yEntry: entry boxes that receive coordinates from the user.
        redSButton and redOButton: buttons that control whether Red will enter an S or an O.
        blueSButton and blueObutton: buttons that do the same thing for Blue.
        addCharButton: adds a letter to GameLogic.letterArray and gridCanvas IF inputs from xEntry
        and yEntry are a valid, unoccupied space.
        simpleButton and complexButton: radiobuttons that control whether the next game will be a 
        simple or complex game.
        gridSizeEntry: entry box that determines the dimensions of the next game created by newGameButton.
        newGameButton: restarts game by creating new SimpleGame or ComplexGame, then resetting 
        gridCanvas with the appropriate height and width.
        gridCanvas: a canvas that displays a grid and shows the player the status of the current game.
        Visible attributes include the game's size, the S and O placements, and any SOS patterns that
        have been formed with colored lines.
        f: text file "gameRecord.txt" that is written to keep track of recorded games.
        gameNumber: int that keeps track of what number game is being recorded. Only iterates for recorded
        games and ignores unrecorded games.
        recordingGame: bool that holds whether the current game is being recorded in "gameRecord.txt".

        gridLetter(self): method connected to addCharButton. Finds appropriate letter and coordinates,
        then places letter in GameLogic.letterArray and gridCanvas OR displays error message in
        announceLabel. Also checks for created SOS patterns and if game is over.
        newGameCommand(self): method connected to newGameButton. Creates new GameLogic derivative
        based on nextGameType and gridSizeEntry.
    """

    def __init__(self):
        #Initializes first game, a simple game with grid size of 8 and two human players.
        self.currentGame = SimpleGame(8, False, False, "S", "S")
        random.seed()
        #Sets up text file for recording games.
        self.f = open("gameRecord.txt", "w")
        self.f.write("Game Log:\n")
        self.gameNumber = 0

        #Window setup.
        self.window = tk.Tk()
        self.window.title("SOS Game")
        self.window.geometry("600x400")

        #Sets up frames within window.
        self.headerFrame = tk.Frame(self.window)
        self.redFrame = tk.Frame(self.window)
        self.blueFrame = tk.Frame(self.window)
        self.gridFrame = tk.Frame(self.window)
        self.scoreFrame = tk.Frame(self.window)
        self.charEntryFrame = tk.Frame(self.window)

        #Labels that will be edited during the game.
        self.redScoreLabel = tk.Label(self.scoreFrame, width = 3, text = "0")
        self.blueScoreLabel = tk.Label(self.scoreFrame, width = 3, text = "0")
        self.turnLabel = tk.Label(self.scoreFrame, text = "Red's turn")
        self.announceLabel = tk.Label(self.scoreFrame)

        #String variables and radio buttons that control what letter each player will insert.
        self.redSV = tk.StringVar(self.window, "S")
        self.blueSV = tk.StringVar(self.window, "S")
        self.redSButton = tk.Radiobutton(self.redFrame, pady = 3, text = "S", variable = self.redSV, value = "S", command = self.changeRedLetter)
        self.redOButton = tk.Radiobutton(self.redFrame, pady = 3, text = "O", variable = self.redSV, value = "O", command = self.changeRedLetter)
        self.blueSButton = tk.Radiobutton(self.blueFrame, pady = 3, text = "S", variable = self.blueSV, value = "S", command = self.changeBlueLetter)
        self.blueOButton = tk.Radiobutton(self.blueFrame, pady = 3, text = "O", variable = self.blueSV, value = "O", command = self.changeBlueLetter)

        #Boolean variable and radio buttons that will control the next game's ruleset.
        self.nextGameType = tk.BooleanVar(self.window, True)
        self.simpleButton = tk.Radiobutton(self.charEntryFrame, text = "Simple Game", variable = self.nextGameType, value = True)
        self.complexButton = tk.Radiobutton(self.charEntryFrame, text = "Complex Game", variable = self.nextGameType, value = False)

        #String variables and entry boxes that obtain coordinates for entered letter or the size of
        #the grid for the next game.
        self.currentX = tk.StringVar(self.window)
        self.currentY = tk.StringVar(self.window)
        self.nextGridSizeVar = tk.StringVar(self.window, value = "8")
        self.xEntry = tk.Entry(self.charEntryFrame, width = 10, textvariable = self.currentX)
        self.yEntry = tk.Entry(self.charEntryFrame, width = 10, textvariable = self.currentY)
        self.gridSizeEntry = tk.Entry(self.charEntryFrame, width = 5, textvariable = self.nextGridSizeVar)

        #Checkboxes that control whether a player is controlled by a human or computer.
        self.nextRedPlayer = tk.BooleanVar(self.window, False)
        self.nextBluePlayer = tk.BooleanVar(self.window, False)
        self.redComputerBox = tk.Checkbutton(self.redFrame, text = "Computer", variable = self.nextRedPlayer)
        self.blueComputerBox = tk.Checkbutton(self.blueFrame, text = "Computer", variable = self.nextBluePlayer)

        #Buttons that add S or O to board and starts new game.
        self.addCharButton = tk.Button(self.charEntryFrame, text = "Add character", command = self.gridLetter)
        self.newGameButton = tk.Button(self.charEntryFrame, text = "New Game", command = self.newGameCommand)

        #Label placements.
        tk.Label(self.headerFrame, text = "SOS Game").pack(fill = 'x')
        tk.Label(self.headerFrame, text = "By Stephen Holman").pack(fill = 'x')

        tk.Label(self.redFrame, text = "Red Player", pady = 15).pack()
        self.redSButton.pack()
        self.redOButton.pack()
        self.redComputerBox.pack(pady = 10)

        tk.Label(self.blueFrame, text = "Blue Player", pady = 15).pack()
        self.blueSButton.pack()
        self.blueOButton.pack()
        self.blueComputerBox.pack(pady = 10)

        tk.Label(self.scoreFrame, text = "Red Score: ").pack(side = 'left')
        self.redScoreLabel.pack(side = 'left')
        self.blueScoreLabel.pack(side = 'right')
        tk.Label(self.scoreFrame, text = "Blue Score: ").pack(side = 'right')
        self.announceLabel.pack()
        self.turnLabel.pack()

        tk.Label(self.charEntryFrame, text = "X value:").grid(row = 0, column = 0)
        self.xEntry.grid(row = 0, column = 1)
        tk.Label(self.charEntryFrame, text = "Y value:").grid(row = 0, column = 2)
        self.yEntry.grid(row = 0, column = 3)
        self.addCharButton.grid(row = 1, column = 0, columnspan = 4, pady = 10)
        tk.Label(self.charEntryFrame, text = "Game Type:").grid(row = 2, column = 0)
        self.simpleButton.grid(row = 2, column = 1)
        self.complexButton.grid(row = 2, column = 2)
        self.newGameButton.grid(row = 2, column = 3)
        tk.Label(self.charEntryFrame, text = "New Game Grid Size: (From 5 to 10)").grid(row = 3, column = 0, columnspan = 3)
        self.gridSizeEntry.grid(row = 3, column = 3)

        #Playing grid canvas creation and placements. Default size is 8.
        self.gridCanvas = tk.Canvas(self.window, height = 160, width = 160)
        for y in range(0, 8):
            for x in range(0, 8):
                self.gridCanvas.create_rectangle(y*20, x*20, (y*20) + 20, (x*20) + 20, outline = "#000", fill = "#fff")
                x += 20
            y += 20

        #Variables and checkbox for determining whether game will be recorded.
        self.recordingGame = False
        self.recordNextGame = tk.BooleanVar(self.window, False)
        self.recordBox = tk.Checkbutton(self.window, text = "Record Game", variable = self.recordNextGame)

        #Places frames and gridCanvas within window.
        self.headerFrame.grid(row = 0, column = 1)
        self.redFrame.grid(row = 1, column = 0)
        self.gridCanvas.grid(row = 1, column = 1, sticky = "")
        self.blueFrame.grid(row = 1, column = 2)
        self.scoreFrame.grid(row = 2, column = 1)
        self.charEntryFrame.grid(row = 3, column = 1)
        self.recordBox.grid(row = 3, column = 0)

    #Method for adding letter to the grid in the GUI and finding new SOS patterns.
    def gridLetter(self):
        try:   
            selectedX = int(self.currentX.get()) - 1
            selectedY = int(self.currentY.get()) - 1
        #If the coordinates are not valid integers, edits announcement to reflect this and skips the
        #rest of the code in else section.
        except (TypeError, ValueError):
            self.currentGame.currentAnnounce = "Invalid entry"
        else:
            #Decides which letter to enter and where based on whose turn it is. Also retrieves correct
            #color from player's information.
            selectedColor = ""
            currentPlayer = True
            if (self.currentGame.currentTurn):
                selectedInfo = self.currentGame.redPlayer.newLetterInfo(selectedX, selectedY, len(self.currentGame.letterArray))
                selectedColor = self.currentGame.redPlayer.color
                currentPlayer = True
            else:
                selectedInfo = self.currentGame.bluePlayer.newLetterInfo(selectedX, selectedY, len(self.currentGame.letterArray))
                selectedColor = self.currentGame.bluePlayer.color
                currentPlayer = False
            success = self.currentGame.placeLetter(selectedInfo)
            #Only places letter in labelGrid if GameLogic.placeLetter was successful.
            if (success):
                self.gridCanvas.create_text(selectedInfo[0]*20 + 10, selectedInfo[1]*20 + 10, text = selectedInfo[2])
                player = "Red" if currentPlayer else "Blue"
                #Writes information in text file if game is being recorded.
                if self.recordingGame:
                    self.f.write(player + " placed " + selectedInfo[2] + " at (" + str(selectedInfo[0]) + ", " + str(selectedInfo[1]) + ").\n")
                scoreChange = False
                #Tests if SOS was formed in any direction if new letter was an S.
                if (selectedInfo[2] == "S"):
                    for searchX in [-1,0,1]:
                        for searchY in [-1,0,1]:
                            scored = self.currentGame.findPatternForS(currentPlayer, selectedInfo[0] + (2*searchX), selectedInfo[1] + (2*searchY), selectedInfo[0] + searchX, selectedInfo[1] + searchY)
                            #If successful, draws line in correct color.
                            if (scored):
                                self.gridCanvas.create_line((selectedInfo[0] * 20) + (searchX * 40) + 10, (selectedInfo[1] * 20) + (searchY * 40) + 10, (selectedInfo[0] * 20) + 10, (selectedInfo[1] * 20) + 10, fill = selectedColor, width = 2)
                                scoreChange = True
                #Tests if SOS was formed in any direction if new letter was an O.
                elif (selectedInfo[2] == "O"):
                    for searchX in [-1,0,1]:
                        scored = self.currentGame.findPatternForO(currentPlayer, selectedInfo[0] + searchX, selectedInfo[1] + 1, selectedInfo[0] - searchX, selectedInfo[1] - 1)
                        #If successful, draws line in correct color.
                        if (scored):
                            self.gridCanvas.create_line((selectedInfo[0] * 20) + (searchX * 20) + 10, (selectedInfo[1] * 20) + 30, (selectedInfo[0] * 20) - (searchX * 20) + 10,(selectedInfo[1] * 20) - 10, fill = selectedColor, width = 2)
                            scoreChange = True
                    scored = self.currentGame.findPatternForO(currentPlayer, selectedInfo[0] + 1, selectedInfo[1], selectedInfo[0] - 1, selectedInfo[1])
                    if (scored):
                        self.gridCanvas.create_line((selectedInfo[0] * 20) - 10, (selectedInfo[1] * 20) + 10, (selectedInfo[0] * 20) + 30, (selectedInfo[1] * 20) + 10, fill = selectedColor, width = 2)
                        scoreChange = True
                else:
                    #Error has occured if letter is not "S" or "O".
                    raise ValueError
                #If game is being recorded and score for the player has changed, writes new scores in text file.
                if scoreChange == True and self.recordingGame:
                    self.f.write("Score is now: Red " + str(self.currentGame.redPlayer.score) + " vs. Blue " + str(self.currentGame.bluePlayer.score) + "\n")
                #Tests if the game is over using method distinct to SimpleGame or ComplexGame.
                self.currentGame.gameOver()
                #If the game is over and being recorded, writes who won (or if draw occured) in text file.
                if self.currentGame.gameRunning == False and self.recordingGame:
                    if self.currentGame.redPlayer.score > self.currentGame.bluePlayer.score:
                        self.f.write("Red wins.\n")
                    elif self.currentGame.bluePlayer.score > self.currentGame.redPlayer.score:
                        self.f.write("Blue wins.\n")
                    else:
                        self.f.write("Game is a draw.\n")
            
            #If next player is computer, automatically calls function again regardless if letter was placed.
            if (self.currentGame.currentTurn):
                nextPlayerIsComputer = self.currentGame.redPlayer.isComputer
            else:
                nextPlayerIsComputer = self.currentGame.bluePlayer.isComputer
            if (self.currentGame.gameRunning == True and nextPlayerIsComputer == True):
                self.gridLetter()
        finally:
            #Updates announcement and current turn.
            self.announceLabel.config(text = self.currentGame.currentAnnounce)
            self.redScoreLabel.config(text = self.currentGame.redPlayer.score)
            self.blueScoreLabel.config(text = self.currentGame.bluePlayer.score)
            self.turnLabel.config(text = self.currentGame.getTurnString())

    #Method for restarting game and resetting gridCanvas.
    def newGameCommand(self):
        try:
            nextGameSize = int(self.nextGridSizeVar.get())
        #If the nextGameSize is not a valid integer, announces failure and does not start new game.
        except (TypeError, ValueError):
            self.currentGame.currentAnnounce = "Invalid entry for grid size"
        else:
            if (nextGameSize >= 5 and nextGameSize <= 10):
                #Deletes currentGame and creates new one with ruleset and grid size from inputs.
                #New game also includes new redPlayer and bluePlayer.
                del self.currentGame
                if (self.nextGameType.get()):
                    self.currentGame = SimpleGame(nextGameSize, self.nextRedPlayer.get(), self.nextBluePlayer.get(), self.redSV.get(), self.blueSV.get())
                else:
                    self.currentGame = ComplexGame(nextGameSize, self.nextRedPlayer.get(), self.nextBluePlayer.get(), self.redSV.get(), self.blueSV.get())
                self.redScoreLabel.config(text = "0")
                self.blueScoreLabel.config(text = "0")
                #Resets gridCanvas.
                self.gridCanvas.delete("all")
                self.gridCanvas.config(width = nextGameSize * 20, height = nextGameSize * 20)
                for y in range(0, nextGameSize):
                    for x in range(0, nextGameSize):
                        self.gridCanvas.create_rectangle(y*20, x*20, (y*20) + 20, (x*20) + 20, outline = "#000", fill = "#fff")
                        x += 20
                    y += 20

                #If game is going to be recorded, writes the game number and ruleset in text file.
                self.recordingGame = self.recordNextGame.get()
                if (self.recordingGame):
                    self.gameNumber += 1
                    gameType = "Simple" if self.nextGameType.get() else "Complex"
                    redType = "Computer" if self.currentGame.redPlayer.isComputer else "Human"
                    blueType = "Computer" if self.currentGame.bluePlayer.isComputer else "Human"
                    self.f.write("\nGame " + str(self.gameNumber) + ": " + gameType + " game with " + redType + " Red and " + blueType + " Blue.\n")
                
                #If redPlayer is a computer, automatically calls gridLetter. Sets currentX and currentY
                #to 1 to avoid failing that method.
                if (self.currentGame.redPlayer.isComputer == True):
                    self.currentX.set(1)
                    self.currentY.set(1)
                    self.gridLetter()
            #If nextGameSize is outside of acceptable range, does not create new game.
            else:
                self.currentGame.currentAnnounce = "Grid size outside acceptable range"
        finally:
            self.announceLabel.config(text = self.currentGame.currentAnnounce)
            self.turnLabel.config(text = self.currentGame.getTurnString())

    #Changes letter for each player (only does something when player is a human).
    def changeRedLetter(self):
        self.currentGame.redPlayer.changeLetter(self.redSV.get())

    def changeBlueLetter(self):
        self.currentGame.bluePlayer.changeLetter(self.blueSV.get())