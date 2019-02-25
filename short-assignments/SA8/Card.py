card_list = ["Jack", "Queen", "King"]
suit_list = ["clubs", "spades", "diamonds", "hearts"]

class Card:
    def __init__(self, value, suit):
        # handle suit input
        self.suit = suit_list[suit - 1]

        # handle value input
        if value <= 10:
            self.value = value
        else:
            self.value = card_list[value-11]

    def __str__(self):
        return str(self.value) + " of " + str(self.suit)