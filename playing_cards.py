# We need to be able to shuffle our deck of playing cards
from random import shuffle

# When we make our actual deck of playing cards,
# each card in the deck will be an instance of this class.
class Card():

    # A dictionary that contains our symbols
    symbols_dict = {"Spades": "♠", "Hearts": "♥", "Clubs": "♣", "Diamonds": "♦"}

    # Defining our Card constructor method
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.assign_symbol()
        self.assign_int()

    # Assigns an integer to each instance of Card
    def assign_int(self):

        # If the card is a number card, the assigned integer is the number the card is
        if self.value.isnumeric():
            self.assigned_int = int(self.value)

        # If the card is an 'Ace', the assigned integer is 1
        elif self.value == "A":
            self.assigned_int = 1

        # If the card is a face card, the assigned integer is 10
        else:
            self.assigned_int = 10

    # Assigns a symbol to each instance of Card by referencing the symbols dictionary
    def assign_symbol(self):
        self.symbol = self.symbols_dict[self.suit]

    # Returns a string formatting the card for printing
    def get_printed_card(self):
        return f"|{self.value} {self.symbol}|"
        
# Class for creating a shuffled deck of playing cards
# Made up of instances of class Cards
class Deck():

    # Initializing Deck with an empty list that will be filled with cards when new_deck is called
    def __init__(self):
        self.cards = []

    # Creates our deck of playing cards which is a list of Card objects
    # and shuffles the deck
    def new_deck(self):

        # Tuple with card values
        values = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

        # Tuple with card suits
        suits = ("Spades", "Hearts", "Clubs", "Diamonds")

        # Creates an ordered list of Card objects
        cards = [Card(value, suit) for value in values for suit in suits]

        # Shuffles the list
        shuffle(cards)

        # Assigned the shuffled list of Card objects to self.cards
        self.cards = cards

    # Deals a card from the top of the deck 
    # and removes it from the deck
    def deal_cards(self, number_of_cards, hand):
        dealt_cards = []

        # If you only want to deal 1 card
        if number_of_cards == 1:
            dealt_cards.append(self.cards.pop())

        # If it's more than 1 card
        else:
            for _ in range(number_of_cards):
                card = self.cards.pop()
                dealt_cards.append(card)
        
        # Extend our hand list with the cards that were dealt
        hand.hand_list.extend(dealt_cards)

        # Update the number of Aces that are in the player or dealer's hand
        hand.get_number_of_aces()

        # Update the sum of all the cards in the hand
        hand.update_hand_sum()