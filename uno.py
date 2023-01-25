# Todo - add an option to try to play a drawed card the turn you draw it
# Bugs - none known

from random import shuffle, choice

useGraphics = True
playerStartAmount = 7
computerStartAmount = 7
autoReplenishDeck = True
turn = 0 # 1 if whoStarts == "computer" else 0q

class Deck:
    def __init__(self, ug): # Creates all variables needed.
        if ug:
            from turtle import Screen, Turtle
            class Card:
                def __init__(self, deckObject, image = "blank", posx = 0, posy = 0): # Takes 1 required arguments, 3 optional arguments
                    # deckObject -> class
                    # this should be a Deck() class. This is used to send the registered clicks to the deck.
                    
                    # image -> str
                    # sets the image to use

                    # posx -> int, float
                    # posy -> int, float
                    # sets x and y coordinates
                    self.turtle = Turtle()
                    self.turtle.pu()
                    self.turtle.speed(0)
                    self.deck = deckObject

                    self.gotoNewLocation(posx, posy)
                    self.updateImage(image)

                def gotoNewLocation(self, posx, posy):
                    self.turtle.goto(posx, posy)

                def updateImage(self, image = "uno back"):
                    if image == "blank":
                        self.turtle.ht()
                    else:
                        self.turtle.st()
                        self.turtle.shape("unoSprites/" + image + ".gif") # Updates visible image
        
        images = [ # Images used for sprites
            "red 0.gif", "red 1.gif", "red 2.gif", "red 3.gif", "red 4.gif", "red 5.gif", "red 6.gif", "red 7.gif", "red 8.gif", "red 9.gif", "red skip.gif", "red reverse.gif", "red draw 2.gif",
            "yellow 0.gif", "yellow 1.gif", "yellow 2.gif", "yellow 3.gif", "yellow 4.gif", "yellow 5.gif", "yellow 6.gif", "yellow 7.gif", "yellow 8.gif", "yellow 9.gif", "yellow skip.gif", "yellow reverse.gif", "yellow draw 2.gif",
            "green 0.gif", "green 1.gif", "green 2.gif", "green 3.gif", "green 4.gif", "green 5.gif", "green 6.gif", "green 7.gif", "green 8.gif", "green 9.gif", "green skip.gif", "green reverse.gif", "green draw 2.gif",
            "blue 0.gif", "blue 1.gif", "blue 2.gif", "blue 3.gif", "blue 4.gif", "blue 5.gif", "blue 6.gif", "blue 7.gif", "blue 8.gif", "blue 9.gif", "blue skip.gif", "blue reverse.gif", "blue draw 2.gif",
            "any draw 4.gif", "any wild.gif", "uno back.gif"
        ]
        self.useGraphics = ug
        self.currentCard = ""
        self.customColor = False
        self.playerDeck = []
        self.computerDeck = []
        self.deckAvailable = {}
        
        if self.useGraphics:
            self.cardsOnScreen = []
            self.screen = Screen()
            self.screen.setup(1024, 576)
            self.screen.tracer(0)
            self.screen.bgcolor("#443344")
            
            for o in range(2):
                for i in range(107):
                    self.cardsOnScreen.append(Card(self, "blank", 55 * (i % 18) - 485, 0 - (80 * (i // 18) - 248) if o == 1 else 95 * (i // 18) - 240))
            
            for i in images:
                self.screen.addshape("unoSprites/" + i)
            
            self.numberer = Turtle()
            self.numberer.pu()
            self.numberer.ht()
            self.numberer.color("white")
            
            self.deckDisplay = Card(self, "blank", 30, 0)
            self.deckBackDisplay = Card(self, "uno back", -30, 0)
            
            self.screen.update()
    
    def setupNewGame(self, playerCards, computerCards): # Setup game
        self.deckAvailable = { # Resets variable at start of game
            "total": 108,
            "cards": [
                "red 0", "red 1", "red 1", "red 2", "red 2", "red 3", "red 3", "red 4", "red 4", "red 5", "red 5", "red 6", "red 6", "red 7", "red 7", "red 8", "red 8", "red 9", "red 9", "red skip", "red skip", "red reverse", "red reverse", "red draw 2", "red draw 2",
                "yellow 0", "yellow 1", "yellow 1", "yellow 2", "yellow 2", "yellow 3", "yellow 3", "yellow 4", "yellow 4", "yellow 5", "yellow 5", "yellow 6", "yellow 6", "yellow 7", "yellow 7", "yellow 8", "yellow 8", "yellow 9", "yellow 9", "yellow skip", "yellow skip", "yellow reverse", "yellow reverse", "yellow draw 2", "yellow draw 2",
                "green 0", "green 1", "green 1", "green 2", "green 2", "green 3", "green 3", "green 4", "green 4", "green 5", "green 5", "green 6", "green 6", "green 7", "green 7", "green 8", "green 8", "green 9", "green 9", "green skip", "green skip", "green reverse", "green reverse", "green draw 2", "green draw 2",
                "blue 0", "blue 1", "blue 1", "blue 2", "blue 2", "blue 3", "blue 3", "blue 4", "blue 4", "blue 5", "blue 5", "blue 6", "blue 6", "blue 7", "blue 7", "blue 8", "blue 8", "blue 9", "blue 9", "blue skip", "blue skip", "blue reverse", "blue reverse", "blue draw 2", "blue draw 2",
                "any draw 4", "any draw 4", "any draw 4", "any draw 4", "any wild", "any wild", "any wild", "any wild"
            ],
            "colors": ("red", "yellow", "green", "blue")
        }
        conputerDeck = ["any wild", "any wild", "any wild", "blue 1", "green 4"]
        shuffle(self.deckAvailable["cards"]) # Shuffles the deck
        
        self.currentCard = self.drawCard() # Sets the first card on the deck at the start of the game
        
        if self.currentCard.split(" ")[0] == "any": # If its a wild or draw 4, it chooses a random color
            self.customColor = choice(self.deckAvailable["colors"])

        else: # If its not, the custom color is set to False
            self.customColor = False
        
        # Generates the deck of cards for both players
        self.playerDeck = self.getNewDeck(playerCards)[0]
        self.computerDeck = self.getNewDeck(computerCards)[0]
    
    def insertIntoDeck(self, card): # Inserts a card into the deck and shuffles it.
        self.deckAvailable["cards"].append(card) # Appends card to deck
        self.deckAvailable["total"] += 1         # Adds one to total in deck
        shuffle(self.deckAvailable["cards"])     # Shuffles deck
    
    def playCard(self, newCard, turn, replenishDeck = True): # Plays a card on the deck.
                                                             # Handles color changes if needed.
        newColor = ""
        
        if self.customColor: # If there is a custom color set, it gets reset
            self.customColor = False
        
        if replenishDeck: # If replenishDeck is True, it will insert the old card back into the deck
            self.insertIntoDeck(self.currentCard)
        
        self.currentCard = newCard # Updates current card
        if self.currentCard.split(" ")[0] == "any": # If its a draw 4 or wild, chooose a sub-color
            if turn == 0:
                while newColor not in ["1", "2", "3", "4"]:
                    newColor = input("Enter a number, 1-4, of which color you want to make it.\n(1 = red, 2 = yellow, 3 = green, 4 = blue)\n")
                self.customColor = self.deckAvailable["colors"][int(newColor) - 1]
            else:
                self.customColor = choice(self.deckAvailable["colors"]) # Chooses a color for the computer when it plays a wild or draw 4
                                                                        # It first starts as a random color but it goes through
                                                                        # the conputer's deck and if there is a colored card in it
                                                                        # it will choose that color. Because of how it is made, it chooses
                                                                        # the last colored card in the deck to be the color.
                
                for i in self.computerDeck: # Picks a random color from the computer's deck
                    if i.split(" ")[0] in self.deckAvailable["colors"]:
                        self.customColor = i.split(" ")[0]
    
    def getNewDeck(self, amount): # Returns a new deck with x amount of cards
        shuffle(self.deckAvailable["cards"])
        newDeck = []
        for i in range(amount):
            if self.deckAvailable["total"]:
                newDeck.append(self.deckAvailable["cards"][0])
                self.deckAvailable["cards"].pop(0)
                self.deckAvailable["total"] -= 1
            else:
                return [newDeck, i]
        return [newDeck, amount]
    
    def drawCard(self): # Takes a card out of the deck and returns it.
        if self.deckAvailable["total"]:
            self.deckAvailable["total"] -= 1
            out = self.deckAvailable["cards"][0]
            self.deckAvailable["cards"].pop(0)
            return out
        return False
    
    def checkIfValidPlay(self, placedCard): # Checks if a play is valid on the current top card
        if placedCard.split(" ")[0] == "any" or self.currentCard.split(" ")[0] == placedCard.split(" ")[0] or self.currentCard.split(" ")[1] == placedCard.split(" ")[1] or (self.currentCard.split(" ")[0] == "any" and placedCard.split(" ")[0] == self.customColor):
            return True
        return False
    
    def handIntoString(self, deck): # Returns a hand as a string to print
        out = ""
        for i in range(len(deck)):
            out += str(i + 1) + ": " + deck[i].replace("any ", "") + "\n"
        return out[:-1]
    
    def updateVisibleDeck(self): # Prints/displays the deck and both the computer's and player's cards
        if self.useGraphics: # Makes the screen update if graphics are on
            self.deckDisplay.updateImage(self.currentCard)
            
            self.numberer.clear()
            
            for i in self.cardsOnScreen:
                i.updateImage("blank")
            
            for i in range(len(self.playerDeck)): # Render the player's cards on screen
                self.cardsOnScreen[i].updateImage(self.playerDeck[i])
                self.numberer.goto(55 * (i % 18) - 485, 95 * (i // 18) - 203)
                self.numberer.write(str(i + 1), False, "center", ("Arial", 12, "normal"))
            self.numberer.goto(-30, 35)
            self.numberer.write(str(self.deckAvailable["total"]), False, "center", ("Arial", 12, "normal"))
            
            for i in range(len(self.computerDeck)): # Render the computer's cards
                self.cardsOnScreen[i + 107].updateImage("uno back")
            
            if self.customColor == "red":
                self.screen.bgcolor("#552222")
            elif self.customColor == "yellow":
                self.screen.bgcolor("#555522")
            elif self.customColor == "green":
                self.screen.bgcolor("#225522")
            elif self.customColor == "blue":
                self.screen.bgcolor("#333355")
            else:
                self.screen.bgcolor("#443344")
            
            self.screen.update() # Update the display
        else: # This print statement prints the deck and stuff
            print("\n\nComputer's cards: " + str(len(self.computerDeck)) + ("\nUNO!!!!!" if len(self.computerDeck) == 1 else "") + "\n\n+---+ +" + "-" * len(self.currentCard.replace("any ", "")) + "+\n|UNO| |" + self.currentCard.replace("any ", "") + "|\n+---+ +" + "-" * len(self.currentCard.replace("any ", "")) + "+" + ("\n\nColor: " + self.customColor if self.customColor else "") + "\n\nYour cards:\n" + self.handIntoString(self.playerDeck))
  
    def changeTeamAgain(self, card, turn): # Handles draw 2/4 cards and skips
        if card.split(" ")[1] == "draw":
            return [(turn + 1) % 2, int(card.split(" ")[2])]
        elif card.split(" ")[1] == "skip":
            return [(turn + 1) % 2, 0]
        else:
            return [turn, 0]
    
    def startGame(self, turn, replenishDeck, playerStart, computerStart): # Controls the entire game. Call this function
                                                   # after you define the variable.
        self.setupNewGame(playerStart, computerStart)
        
        self.updateVisibleDeck() # Draws the deck when the game starts
        
        while True:
            checkIfTeamModify = False # This variable tells the game wheither or not
                                      # to check if any particular team should draw cards
                                      # or get their turn skipped.
            
            if self.deckAvailable["total"]: # Makes sure there are cards left in the deck to draw from
                while not turn: # This loop makes it so that if the player inputs a bad input,
                                # it stays their turn until they input a valid number.
                    try:
                        card = int(input("Enter which card you want to play! (0 to draw)\n")) - 1
                        if card == -1: # If input is 0, draw card
                            self.playerDeck.append(self.drawCard())
                            turn = 1
                            checkIfTeamModify = False
                            self.updateVisibleDeck()
                        
                        elif self.checkIfValidPlay(self.playerDeck[card]): # If the play is valid, play card
                            self.playCard(self.playerDeck[card], turn, replenishDeck)
                            self.playerDeck.pop(card)
                            turn = 1
                            checkIfTeamModify = True
                        else:
                            print("That was not a valid play. Please try again.")
                    except:
                        print("Bad input :(")
            else:
                print("There aren't any cards left in the deck!")
                break
            
            if self.checkIfWin(): # Checks if player wins
                self.updateVisibleDeck()
                print("You win, yay.")
                break
            
            if checkIfTeamModify: # Handles the draw 2/4 cards and skips
                teamModifier = self.changeTeamAgain(self.currentCard, turn)
                for i in range(teamModifier[1]):
                    if not turn:
                        self.playerDeck.append(self.drawCard())
                    else:
                        self.computerDeck.append(self.drawCard())
                self.updateVisibleDeck()
                turn = teamModifier[0]
            
            checkIfTeamModify = False # Reset variable
            
            if self.deckAvailable["total"]: # Makes sure there are cards left in the deck to draw from
                for i in range(len(self.computerDeck)): # Checks if any of the comptuters cards
                                                        # are valid, and plays it if so
                    if turn == 1 and self.checkIfValidPlay(self.computerDeck[i]):
                        self.playCard(self.computerDeck[i], turn, replenishDeck)
                        self.computerDeck.pop(i)
                        turn = 0
                        checkIfTeamModify = True
                
                if turn: # If no valid plays, it draws a card.
                    self.computerDeck.append(self.drawCard())
                    turn = 0
                    checkIfTeamModify = False
                    self.updateVisibleDeck()
            else:
                print("There aren't any cards left in the deck!")
                break
            
            if self.checkIfWin(): # Checks if computer wins
                self.updateVisibleDeck()
                print("Nooo, the computer wins.")
                break
            
            if checkIfTeamModify: # Handles the draw 2/4 cards and skips
                teamModifier = self.changeTeamAgain(self.currentCard, turn)
                for i in range(teamModifier[1]):
                    if not turn:
                        self.playerDeck.append(self.drawCard())
                    else:
                        self.computerDeck.append(self.drawCard())
                self.updateVisibleDeck()
                turn = teamModifier[0]
                if turn == 1:
                  input("Press enter to continue...\n")
    
    def checkIfWin(self): # Checks if someone has won.
        return True if not len(self.playerDeck) or not len(self.computerDeck) else False

deck = Deck(useGraphics)

deck.startGame(turn, autoReplenishDeck, playerStartAmount, computerStartAmount)

input("Press enter to close.\n")
