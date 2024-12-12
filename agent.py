import random

class ZeroOrderAgent:
    """Zero-Order Agent that reasons based on statistics."""
    def __init__(self, num_dice):
        self.num_dice = num_dice
        self.dice = []

    def roll_dice(self):
        """Roll the dice and store the results."""
        self.dice = [random.randint(1, 6) for _ in range(self.num_dice)]

    def calculate_expected_count(self, total_dice, bid_face):
        """
        Calculate the expected count of dice matching the bid face across all players' dice.
        Each face (1-6) is equally likely, so expected count is total_dice / 6.
        """
        expected_count = total_dice / 6
        return expected_count

    def challenge_bid(self, bid, total_dice):
        """
        Decide whether to challenge the current bid based on its statistical likelihood.
        """
        bid_quantity, bid_face = bid
        own_count = sum(1 for die in self.dice if die == bid_face or die == 1)
        expected_count = self.calculate_expected_count(total_dice, bid_face)

        # Challenge if the bid seems statistically improbable
        return own_count + expected_count < bid_quantity

    def place_bid(self, current_bid):
        """
        Place a bid based on the current bid and the dice in hand.
        The bid increases the quantity if possible or changes the face value otherwise.
        """
        if current_bid:
            current_quantity, current_face = current_bid
            if current_quantity < self.num_dice + 1:
                return (current_quantity + 1, current_face)
            else:
                new_face = current_face + 1 if current_face < 6 else 1
                return (1, new_face)
        else:
            return (1, random.randint(1, 6))