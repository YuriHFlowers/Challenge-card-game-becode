from random import random
import random
from card import Card  # importar Class Card from card.py


class Player:
    def __init__(self, hand_cards, turn_count, number_of_cards, history):
        self.hand_cards = hand_cards  # the cards that player has in his hands
        self.turn_count = turn_count  # is an int starting a 0
        self.number_of_cards = number_of_cards  # is an int starting at 0
        self.history = history  # is a list of `Card` that will contain all the cards played by the player.

    def play(self):
        # **randomly** pick a `Card` in `cards`

        self.history.append(Card)  # Add the `Card` to the `Player`'s `history`.
        print(
            "{} {} played: {} {}".format(
                self.player_name, self.turn_count, self.value, self.icon
            )
        )
        return Card  # Card or card ??"""


class Deck:
    def __init__(self):
        self.cards = []  # is a list []     deck cards different player cards

    def fill_deck(self):
        color = ["red", "black"]
        value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        for color in ["red", "black"]:
            if color == ["red"]:
                for icon in ["\u2660", "\u2663"]:
                    for v in value:
                        self.cards.append(Card(color, icon, v))
                        # print("Hello {} {} of {}".format(color, icon, v))
            else:
                for icon in ["\u2660", "\u2663"]:
                    for v in value:
                        self.cards.append(Card(color, icon, v))
                        print("Hello {} {} of {}".format(color, icon, v))

        return self.cards

    def shuffle(self):
        self.cards = random.sample(self.cards, len(self.cards))
        return self.cards

    def distribute(self, player_names):

        for player in player_names:  # append iteration for loop over the list of player
            player.hand_cards.append(self.cards)
            self.cards.pop()  # take a card from the fill_deck -52 cards  self.cards = object"""

    player_names = ["Yuri", "Tim"]


yuri = Player()
tim = Player()
deck = Deck()
deck.fill_deck()
deck.shuffle()
deck.distribute()


# self.cards.append()
# yuri = Player([], 0, 0, [])    #check Class Payer
# print(yuri)
# deck = Deck()
# deck.fill_deck()
# deck.shuffle()
