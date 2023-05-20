# The player and the dealer each have an instance of the Hand class
# in their respective objects
class Hand():

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