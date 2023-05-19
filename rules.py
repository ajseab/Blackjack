# We can use this class to change rules in our Blackjack game.
class Rules():
    def __init__(self):
        # Changes the minumum bet the player can bet.
        self.minbet = 10

        # Changes the starting $ amount in a player's wallet.
        self.starting_amount = 100

        # This is the ratio of increased payout you receive
        # if you have Blackjack at the beginning of the round.
        self.blackjack_payout = 1.5