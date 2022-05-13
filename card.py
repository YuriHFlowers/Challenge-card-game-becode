class Symbol:
    """Class defining Symbol characterized by:
    its color
    its icon"""

    def __init__(self, color, icon):
        self.color = color
        self.icon = icon


class Card(Symbol):
    def __init__(self, color, icon, value):
        super().__init__(color, icon)
        self.value = value

    def __str__(self):
        return f"{self.color}{self.icon}{self.value}"

    # def show_card(self):
    # print("{} {} of {}".format(self.value, self.color, self.icon))


# yuri = Card("black", "\u2660", "6")
# yuri.show_card()
