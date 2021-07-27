import random


class Card:
    """Card class."""

    def __init__(self, value, color):
        self.value = value
        self.color = color


class Deck:
    """Deck class."""

    def __init__(self):
        values = [n for n in range(2, 11)] + ['Jack', 'Queen', 'King', 'Ace']
        colors = ['hearts', 'diamonds', 'spades', 'clubs']
        self.cards = [Card(value, color)
                      for value in values for color in colors]

    def shuffle(self):
        """Shuffle the cards in the deck."""
        random.shuffle(self.cards)

    def pull(self):
        """Return a card and remove it from the deck."""
        card = self.cards[0]
        self.cards = self.cards[1:]
        return card

    def show(self):
        """Show the remaining cards in the deck in the terminal."""
        print("Remaining cards in the deck:\n----------------------------")
        for card in self.cards:
            print(f"Value: {card.value}, Color: {card.color}")

    def size(self):
        """Return amount of remaining cards in the deck."""
        return len(self.cards)


if __name__ == "__main__":
    # Example of use:
    # Initialize the deck, and shuffle the cards
    deck = Deck()
    deck.shuffle()

    # Pull out a card of the deck
    card = deck.pull()
    print(card.value, card.color)

    # Show deck size
    print(deck.size())

    # Show the remaining cards in the deck in the terminal
    deck.show()
