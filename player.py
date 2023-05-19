# import hand.py
from hand import Hand

# Create Player class constructor
class Player():
    def __init__(self, rules):
        self.rules = rules
        self.wallet = self.rules.starting_amount
        self.hand = Hand()