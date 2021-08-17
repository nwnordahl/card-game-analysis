class Stack:
    """Stack class."""

    def __init__(self):
        self.cards = []

    def previous_card(self):
        """Return most recently added card."""
        return self.cards[-1]

    def add(self, card):
        """Add a card to the stack."""
        self.cards.append(card)

    def empty(self):
        """Empty the stack."""
        self.cards = []

    def size(self):
        """Return the amount of cards in the stack."""
        return len(self.cards)


if __name__ == "__main__":
    pass
