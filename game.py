

class Board:

    def __init__(self, player_names, turn_count, active_cards, history_cards):

        self.player_names = player_names  # is a name list of the players
        self.turn_count = turn_count  # that is an int
        self.active_cards = active_cards  #that will contain the last card played by each player.

        self.history_cards = self.cards.pop()  # [] all the cards played since the start of the game, not `active_cards`.

        # The pop() method removes the item at the given index
        # from the list and returns the removed item, the default index -1

player_names = input()
