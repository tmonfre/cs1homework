from Card import Card
from random import randint

class Deck:
    def __init__(self):
        self.card_list = []

    def add_standard_cards(self):
        for suit in range(1,5):
            for value in range(1,14):
                self.card_list.append(Card(value, suit))

    def shuffle(self):
        for i in range(0,len(self.card_list)):
            # calculate new index
            new_index = randint(0,len(self.card_list)-1)

            #swap values
            temp = self.card_list[new_index]
            self.card_list[new_index] = self.card_list[i]
            self.card_list[i] = temp

    def deal(self, num):
        new_hand = Deck()

        for i in range(num):
            new_hand.card_list.append(self.card_list.pop())

        return new_hand