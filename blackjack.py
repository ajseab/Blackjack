#!/usr/bin/env python3

"""A Blackjack terminal game built for MacOS.
"""

import os
import getpass
import platform
from random import shuffle

class Card():
    
    """When we make our actual deck of playing cards,
       each card in the deck will be an instance of this class.
    """

    # A dictionary that contains our symbols
    symbols = {"Spades": "♠", "Hearts": "♥", "Clubs": "♣", "Diamonds": "♦"}

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
        self.symbol = self.symbols[self.suit]

    # Returns a string formatting the card for printing
    def get_printed_card(self):
        return f"|{self.value} {self.symbol}|"
        
class Deck():

    """Class for creating a shuffled deck of playing cards of Card objects
    """

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
        
class Rules():
    
    """We can use this class to change rules in our Blackjack game.
    """
    
    def __init__(self):
        # Changes the minumum bet the player can bet.
        self.minbet = 10

        # Changes the starting $ amount in a player's wallet.
        self.starting_amount = 100

        # This is the ratio of increased payout you receive
        # if you have Blackjack at the beginning of the round.
        self.blackjack_payout = 1.5
        
class Hand():
    
    """The player and the dealer each have an instance of the Hand class
       in their respective objects
    """

    # Initialize with an empty hand and a hand sum of 0
    def __init__(self):
        self.hand_list = []
        self.hand_sum = 0

    # Calculates the number of Aces in the hand
    def get_number_of_aces(self):
        aces = 0
        # For each card in the hand
        for card in self.hand_list:
            # If it's an Ace
            if card.value == "A":
                # Increment aces
                aces += 1
        self.number_of_aces = aces
        return self.number_of_aces
    
    # Updates the hand's sum using the assigned 
    # integers of the cards in the hand
    def update_hand_sum(self):
        li = []

        # For  each card in the hand
        # Add it to li and get the sum of li
        for card in self.hand_list:
            li.append(card.assigned_int)
        hand_sum = sum(li)

        # If there's more than 1 Ace and the hand's sum
        # is less than 11, add 10 to the hand's sum
        if self.number_of_aces > 0 and hand_sum < 12:
            hand_sum += 10

        # Updates self.hand_sum with calculated integer 
        # and returns the integer
        self.hand_sum = hand_sum
        return self.hand_sum
    
    # Resets the hand's list and hand's sum
    # Called at the beginning of a round
    def reset_hand(self):
        self.hand_list = []
        self.hand_sum = 0

    # Checks to see if the hand's sum is equal to 21 (Blackjack)
    # and returns True if it is
    def is_blackjack(self):
        return self.hand_sum == 21
    
    # Checks to see if the hand's sum is greater than 21 (Bust)
    # and returns True if it is
    def is_bust(self):
        return self.hand_sum > 21
    
    # Returns a formatted, printable string of 
    # the whole hand by formatting each card in the hand
    def get_printed_hand(self):
        printed_hand = ""
        for card in self.hand_list:
            printed_hand += f"|{card.value} {card.symbol}| "
        return printed_hand
        
class Dealer():
    # Initialize Dealer class with an instance of a Hand object
    def __init__(self):
        self.hand = Hand()
        
class Player():
    def __init__(self, rules):
        self.rules = rules
        self.wallet = self.rules.starting_amount
        self.hand = Hand()

class Blackjack():
    
    """This is the main class for all functions of the game
    """
    
    def __init__(self):
        self.rules = Rules()
        self.deck = Deck()
        self.player = Player(self.rules)
        self.dealer = Dealer()
        self.play_again = True
        self.print_game_start()

    # Clears terminal based on OS
    def clear_terminal(self):
        i = platform.system()
        if i == "Darwin" or i == "Linux":
            os.system("printf '\\33c\\e[3J'")
        if i == "Windows":
            os.system("cls")

    # Method that prints the starting game dialogue
    def print_game_start(self):
        # Clear macOS terminal
        self.clear_terminal()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nBLACKJACK by AVERY SEABOLT\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"BLACKJACK PAYS {self.rules.blackjack_payout}x\n")
        print(f"WALLET: ${self.player.wallet}")
        print(f"MIN BET: ${self.rules.minbet}\n")
        getpass.getpass("Press (ENTER) to begin ~ ")

    # Deals two cards to the Dealer and two cards to the Player
    def deal_new_hand(self):
        # Initialize and reset Dealer and Player hands
        self.dealer.hand.reset_hand()
        self.player.hand.reset_hand()
        # Create a new deck
        self.deck.new_deck()
        # Deal 2 cards to each dealer and player
        self.deck.deal_cards(2, self.dealer.hand)
        self.deck.deal_cards(2, self.player.hand)

    # Checks if the player has enough money in their
    # wallet to place a bet, otherwise quits the game
    def check_if_cant_bet(self):
        # If the players wallet is less than the minimum bet, return True
        if self.player.wallet < self.rules.minbet:
            print("\nYou ran out of money to bet. Better luck next time!\n")
            getpass.getpass("Press (ENTER) to exit ~ ")
            return True

    # Goes to next round or quits program based on user input
    def go_to_next_round(self):
        i = input("Press (Enter) to place your next bet, Type 'Stop' to stop playing ~ ")
        i = i.lower().strip()
        # If player enters "stop"
        if i == "stop":
            # Quit game
            self.play_again = False
        # If player hits 'enter'
        if i == "":
            # Start another round
            self.play_again = True
        # Validates user input
        while i != "stop" and i != "":
            i = input("Invalid input. Press (Enter) to place your next bet, Type 'Stop' to stop playing ~ ")
            i = i.lower().strip()
            # If player enters "stop": Quit game. Else start another round
            self.play_again = False if i == "stop" else True

    # Get player bet and validate user input to be a number that is 
    # between rules.min_bet and player.wallet
    def get_player_bet(self):
        print("\n--------------------------------")
        while True:
            try:
                i = float(input("Place your bet! ~ $"))
                # If i is not a valid bet amount
                if i < self.rules.minbet or i > self.player.wallet:
                    print("Invalid bet amount. Please enter a number within the valid range.")
                # If i is a valid bet amount
                else:
                    self.bet_amount = i
                    # Exit the loop
                    return i  
            # If a ValueError is given
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    # Check if Dealer and Player both have Blackjack
    def check_if_both_blackjack(self):
        # If both Dealer and Player have blackjack before betting occurs return True
        if self.dealer.hand.is_blackjack() and self.player.hand.is_blackjack():
            print("\nYou both have Blackjack... Push\n")
            return True
        
    # Checks if either the dealer or the player have blackjack
    def check_if_either_blackjack(self):
        # If the Dealer has Blackjack return True
        if self.dealer.hand.is_blackjack():
            self.player.wallet -= self.bet_amount
            print(f"\nDEALER\n{self.dealer.hand.get_printed_hand()}\n\nThe dealer has Blackjack! You lost ${self.bet_amount} to the house (WALLET= ${self.player.wallet})\n")
            return True
        # If the Player has Blackjack return True
        if self.player.hand.is_blackjack():
            win_amount = self.bet_amount * self.rules.blackjack_payout
            self.player.wallet += win_amount
            print(f"\nCONGRATS!\n{self.player.hand.get_printed_hand()}\n\nYou have Blackjack! You won ${win_amount} against the house (WALLET= ${self.player.wallet})\n")
            return True
        # If neither have Blackjack return False
        else:
            return False
        
    # This is the (Hit) or (Stay) method
    def player_turn(self):
        while True:
            hit_or_stay = input(f"{self.player.hand.get_printed_hand()}\nHit (H) / Stay (S) ~ ").upper()
            print("\n")
            # If the player wants to hit, deal one card to the player's hand
            if hit_or_stay == "H":
                self.deck.deal_cards(1, self.player.hand)
                # If the player busted, they lose, return True
                if self.player.hand.is_bust():
                    self.player.wallet -= self.bet_amount
                    print(f"{self.player.hand.get_printed_hand()}\nBust! You lost ${self.bet_amount} to the house (WALLET= ${self.player.wallet})\n")
                    return True
                # If they haven't busted, continue the loop
                else:
                    continue
            # If the player wants to stay, end the loop (return False)
            elif hit_or_stay == "S":
                return False
            # If the player entered an invalid input, print error statement
            # and continue the loop
            else:
                print("Invalid input. Please enter 'H' to hit or 'S' to stay.")

    # Checks if the dealer busts
    def check_if_dealer_busts(self):
        # If the dealer busts, print winning statement and return True
        if self.dealer.hand.is_bust():
            self.player.wallet += self.bet_amount
            print(f"Dealer has busted! You won ${self.bet_amount} from the house (WALLET= ${self.player.wallet})\n")
            return True
        
    # Checks if there is a tie
    def check_if_push(self):
        # If the hand sums are the same, print tie statement and return True
        if self.dealer.hand.hand_sum == self.player.hand.hand_sum:
            print("Push...\n")
            return True
        
    # Checks if the player won
    def check_if_player_won(self):
        # If the player lost to the dealer, print losing statement and return False
        if self.dealer.hand.hand_sum > self.player.hand.hand_sum:
            self.player.wallet -= self.bet_amount
            print(f"Dealer wins. You lose ${self.bet_amount} to the house (WALLET= ${self.player.wallet})\n")
            return False
        # If the player won against the dealer, print winning statement and return True
        if self.dealer.hand.hand_sum < self.player.hand.hand_sum:
            self.player.wallet += self.bet_amount
            print(f"You won ${self.bet_amount} from the house (WALLET= ${self.player.wallet})\n")
            return True

    # Method to handle calling the main methods of gameplay
    # Called when starting a new game or starting a new round
    def start_game(self):
        if self.check_if_cant_bet():
            self.play_again = False
            return
        # Deal a new hand
        self.deal_new_hand()
        # Before recording a bet, check if both dealer and player have blackjack
        if self.check_if_both_blackjack():
            self.go_to_next_round()
            return
        # Asks for bet amount and records it in self.bet_amount
        self.get_player_bet()
        # If either player has blackjack, go to next round
        if self.check_if_either_blackjack():
            self.go_to_next_round()
            return
        # Print what the dealer is showing
        print(f"\nDEALER is showing {self.dealer.hand.hand_list[0].get_printed_card()}...\n")
        # If the player busts, go to next round
        if self.player_turn():
            self.go_to_next_round()
            return
        # Dealer starts to draw cards based off of hand sum
        while self.dealer.hand.hand_sum < 17:
            self.deck.deal_cards(1, self.dealer.hand)
        # Prints Dealer's final hand
        print(f"DEALER\n{self.dealer.hand.get_printed_hand()}\n")
        # If the dealer busts, go to next round
        if self.check_if_dealer_busts():
            self.go_to_next_round()
            return
        # If there is a tie, go to next round
        if self.check_if_push():
            self.go_to_next_round()
            return
        # If the player won against the dealer, go to next round
        if self.check_if_player_won():
            self.go_to_next_round()
            return
        # If the dealer won against the player, go to next round
        else:
            self.go_to_next_round()
            return

    # This method will be called to initialize the whole game
    def play(self):
        # Creates a play again loop so the player can continue 
        # playing or stop if they so choose
        while self.play_again:
            self.start_game()
        # If the player does not want to play again,
        # end program and clear the terminal
        else:
            self.clear_terminal()
        
def main():
    Blackjack().play()
    
if __name__ == "__main__":
    main()