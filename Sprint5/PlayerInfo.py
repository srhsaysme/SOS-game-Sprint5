import random

class PlayerInfo:
    """
    Contains information regarding one player's status in the game.

    Contains variables for a single player for a game.  Used by GameLogic for two players.  The way
    that a new letter is placed by a player is handled by child classes.

    Attributes:
        color: color of the player, used for creating lines GameLogic.findPatternForS and GameLogic.findPatternForO
        score: int that keeps track of player's current score. Upon creating a new game, it defaults to 0.
        letter: the letter that will be placed in array when GameLogic.placeLetter is called. Assigned
        a value in child classes.

        addScore(self): adds one to the score. Called whenever the player forms an SOS pattern.
    """

    def __init__(self, color):
        self.color = color
        self.score = 0
        self.letter = ""

    def addScore(self):
        self.score += 1

class HumanPlayer(PlayerInfo):
    """
    Variant of PlayerInfo that allows a human to select the letter and placement of an "Add Letter" command.

    Attributes:
        letter: takes current value of a player's letter from GameWindow.
        isComputer: tells program that this is a human (not computer) player.

        changeLetter(self, newLetter): changes letter variable to newLetter.
        newLetterInfo(self, xInput, yInput, max): returns a tuple containing information for placing
        a letter.
    """

    def __init__(self, color, letter):
        PlayerInfo.__init__(self, color)
        self.letter = letter
        self.isComputer = False

    def changeLetter(self, newLetter):
        self.letter = newLetter

    def newLetterInfo(self, xInput, yInput, max):
        return (xInput, yInput, self.letter)

class ComputerPlayer(PlayerInfo):
    """
    Variant of PlayerInfo that provides random grid coordinates and random choice between "S" and "O"
    for "Add Letter" command.

    changeLetter(self, newLetter): does nothing since user input is not used for computer player. Exists 
    purely to prevent errors.
    newLetterInfo(self, xInput, yInput, max): returns a tuple containing a random x and y coordinate 
    (that will not lie outside of the grid's size) and a random choice between "S" and "O".
    """
    
    def __init__(self, color):
        PlayerInfo.__init__(self, color)
        self.isComputer = True

    def changeLetter(self, newLetter):
        pass

    def newLetterInfo(self, xInput, yInput, max):
        letters = ("S", "O")
        randX = random.randint(0,max - 1)
        randY = random.randint(0,max - 1)
        letterInt = random.randint(0,1)
        return (randX, randY, letters[letterInt])