from random import shuffle, choice

playerStartAmount = 7
computerStartAmount = 7
autoReplenishDeck = True
turn = 0 # 1 if whoStarts == "computer" else 0

class Deck:
    def __init__(self): # Creates all variables needed.
        self.currentCard = ""
        self.customColor = False
        self.playerDeck = []
        self.computerDeck = []
        
        self.deckAvailable = { # Deck storage variable
            "total": 108, # Total amount of cards left
            "cards": [ # Cards left
                "red 0", "red 1", "red 1", "red 2", "red 2", "red 3", "red 3", "red 4", "red 4", "red 5", "red 5", "red 6", "red 6", "red 7", "red 7", "red 8", "red 8", "red 9", "red 9", "red skip", "red skip", "red reverse ", "red reverse ", "red draw 2", "red draw 2",
                "yellow 0", "yellow 1", "yellow 1", "yellow 2", "yellow 2", "yellow 3", "yellow 3", "yellow 4", "yellow 4", "yellow 5", "yellow 5", "yellow 6", "yellow 6", "yellow 7", "yellow 7", "yellow 8", "yellow 8", "yellow 9", "yellow 9", "yellow skip", "yellow skip", "yellow reverse", "yellow reverse", "yellow draw 2", "yellow draw 2",
                "green 0", "green 1", "green 1", "green 2", "green 2", "green 3", "green 3", "green 4", "green 4", "green 5", "green 5", "green 6", "green 6", "green 7", "green 7", "green 8", "green 8", "green 9", "green 9", "green skip", "green skip", "green reverse", "green reverse", "green draw 2", "green draw 2",
                "blue 0", "blue 1", "blue 1", "blue 2", "blue 2", "blue 3", "blue 3", "blue 4", "blue 4", "blue 5", "blue 5", "blue 6", "blue 6", "blue 7", "blue 7", "blue 8", "blue 8", "blue 9", "blue 9", "blue skip", "blue skip", "blue reverse", "blue reverse", "blue draw 2", "blue draw 2",
                "any draw 4", "any draw 4", "any draw 4", "any draw 4", "any wild", "any wild", "any wild", "any wild"
            ],
            "colors": ("red", "yellow", "green", "blue") # Colors to use for wilds and draw 4s
        }

    def setupNewGame(self, playerCards, computerCards): # Setup game
        self.deckAvailable = { # Resets variable at start of game
            "total": 108,
            "cards": [
                "red 0", "red 1", "red 1", "red 2", "red 2", "red 3", "red 3", "red 4", "red 4", "red 5", "red 5", "red 6", "red 6", "red 7", "red 7", "red 8", "red 8", "red 9", "red 9", "red skip", "red skip", "red reverse ", "red reverse ", "red draw 2", "red draw 2",
                "yellow 0", "yellow 1", "yellow 1", "yellow 2", "yellow 2", "yellow 3", "yellow 3", "yellow 4", "yellow 4", "yellow 5", "yellow 5", "yellow 6", "yellow 6", "yellow 7", "yellow 7", "yellow 8", "yellow 8", "yellow 9", "yellow 9", "yellow skip", "yellow skip", "yellow reverse", "yellow reverse", "yellow draw 2", "yellow draw 2",
                "green 0", "green 1", "green 1", "green 2", "green 2", "green 3", "green 3", "green 4", "green 4", "green 5", "green 5", "green 6", "green 6", "green 7", "green 7", "green 8", "green 8", "green 9", "green 9", "green skip", "green skip", "green reverse", "green reverse", "green draw 2", "green draw 2",
                "blue 0", "blue 1", "blue 1", "blue 2", "blue 2", "blue 3", "blue 3", "blue 4", "blue 4", "blue 5", "blue 5", "blue 6", "blue 6", "blue 7", "blue 7", "blue 8", "blue 8", "blue 9", "blue 9", "blue skip", "blue skip", "blue reverse", "blue reverse", "blue draw 2", "blue draw 2",
                "any draw 4", "any draw 4", "any draw 4", "any draw 4", "any wild", "any wild", "any wild", "any wild"
            ],
            "colors": ("red", "yellow", "green", "blue")
        }
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
                self.customColor = choice(self.deckAvailable["colors"])
    
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
    
    def updateVisibleDeck(self): # Prints out the deck and your cards
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
                        card = int(input("Enter which card you want to play! (0 to draw)")) - 1
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

deck = Deck()

deck.startGame(turn, autoReplenishDeck, playerStartAmount, computerStartAmount)

input("Press enter to close.\n")
